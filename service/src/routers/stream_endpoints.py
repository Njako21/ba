# src/routers/stream_endpoints.py
import asyncio
from fastapi import APIRouter, Request
from fastapi.responses import StreamingResponse
import json # If you want to send JSON data

# Import the shared PubSubManager instance
from src.pubsub import pubsub_manager

from src.util.logger_config import log

# Define router for streaming endpoints
# Note: Prefix '/api' will be added in main.py
router = APIRouter()

@router.get("/stream")
async def stream_events(request: Request):
    """
    Establishes an SSE connection. Clients subscribing here will receive
    messages published via pubsub_manager.publish().
    """
    log(f"Client {request.client.host}:{request.client.port} connecting to SSE stream.")

    # Create a new queue for this specific client connection
    client_queue = await pubsub_manager.subscribe()

    async def event_generator():
        try:
            while True:
                # Check if client is still connected before blocking on queue
                # This helps clean up faster if the client disconnects abruptly
                # Note: This check might not be foolproof in all network conditions
                disconnect_check = await request.is_disconnected()
                if disconnect_check:
                    log(f"Client {request.client.host}:{request.client.port} disconnected (checked before queue wait).", level="warning")
                    break

                try:
                    # Wait for a message from the publisher
                    message = await asyncio.wait_for(client_queue.get(), timeout=30) # Add timeout
                    # Format message for SSE: 'data: <message>\n\n'
                    # You can send plain text or JSON strings
                    # If sending JSON:
                    # yield f"data: {json.dumps(message)}\n\n"
                    # If sending plain text:
                    yield f"data: {message}\n\n"
                    client_queue.task_done() # Mark task as done for the queue
                except asyncio.TimeoutError:
                    # No message received in timeout period, send a keep-alive comment or check connection again
                    # SSE comments start with ':'
                    yield ": keep-alive\n\n"
                    continue # Continue loop to wait again
                except asyncio.CancelledError:
                    log(f"Event generator cancelled for {request.client.host}:{request.client.port}.")
                    break # Exit loop if task is cancelled
                except Exception as e:
                    log(f"Error getting message from queue for {request.client.host}: {e}", level="error")
                    # Decide if you want to break or continue
                    break

        except asyncio.CancelledError:
             log(f"Event generator task cancelled externally for {request.client.host}:{request.client.port}.")
        finally:
            # Crucial: Unsubscribe the client's queue when they disconnect or an error occurs
            log(f"Cleaning up resources and unsubscribing client {request.client.host}:{request.client.port}.")
            await pubsub_manager.unsubscribe(client_queue)

    # Return the streaming response
    # text/event-stream is the standard MIME type for SSE
    # Add headers to prevent caching and keep connection alive
    return StreamingResponse(event_generator(),
                             media_type="text/event-stream",
                             headers={
                                 'Cache-Control': 'no-cache',
                                 'Connection': 'keep-alive',
                                 'X-Accel-Buffering': 'no' # Useful for Nginx proxying
                                 })
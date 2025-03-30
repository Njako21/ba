# src/pubsub.py
import asyncio
from typing import List, Dict, Any

from loguru import logger

class PubSubManager:
    """Manages WebSocket connections and message broadcasting for Pub/Sub."""

    def __init__(self):
        # Store active connections/queues. Using a list of queues for simplicity.
        # For very high scale, consider different structures or external message brokers.
        self._subscribers: List[asyncio.Queue] = []
        logger.info("PubSubManager initialized.")

    async def subscribe(self) -> asyncio.Queue:
        """Adds a new subscriber queue and returns it."""
        queue = asyncio.Queue()
        self._subscribers.append(queue)
        logger.info(f"New subscriber added. Total: {len(self._subscribers)}")
        return queue

    async def unsubscribe(self, queue: asyncio.Queue):
        """Removes a subscriber queue."""
        try:
            self._subscribers.remove(queue)
            logger.info(f"Subscriber removed. Total: {len(self._subscribers)}")
        except ValueError:
            logger.warning("Attempted to remove a queue that was not subscribed.")

    async def publish(self, message: Any):
        """Sends a message to all active subscribers."""
        if not self._subscribers:
            logger.info("Publish requested, but no subscribers are connected.")
            return

        logger.info(f"Publishing message to {len(self._subscribers)} subscribers.")
        # Use asyncio.gather for potential concurrency benefits if putting is slow,
        # though for simple puts it might be negligible overhead.
        # Handle potential errors during put if queues are bounded or closed.
        tasks = [sub_queue.put(message) for sub_queue in self._subscribers]
        await asyncio.gather(*tasks, return_exceptions=True) # return_exceptions logs errors instead of stopping


# Create a single global instance to be shared across the application
# This simplifies dependency management for this specific use case.
# For more complex apps, consider FastAPI's Dependency Injection system further.
pubsub_manager = PubSubManager()

# Example usage within endpoints:
# from src.pubsub import pubsub_manager
# await pubsub_manager.publish("Hello Subscribers!")
# queue = await pubsub_manager.subscribe()
# await pubsub_manager.unsubscribe(queue)
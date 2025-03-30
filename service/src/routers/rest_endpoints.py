# src/routers/rest_endpoints.py
from fastapi import APIRouter, HTTPException, status
from pydantic import BaseModel

# Import the shared PubSubManager instance
from src.pubsub import pubsub_manager

from loguru import logger

# Define router for REST endpoints
# Note: Prefix '/api' will be added in main.py
router = APIRouter()

# --- GET Endpoints ---

@router.get("/get/hello/{name}")
async def get_hello(name: str):
    """Simple GET endpoint example."""
    logger.info(f"GET /get/hello/{name} called")
    return {"message": f"Hello, {name}!"}

@router.get("/get/data")
async def get_some_data():
    """Another GET endpoint example."""
    logger.info("GET /get/data called")
    # In a real app, you might fetch this from a database
    return {"id": 123, "value": "Some data retrieved", "is_active": True}


# --- POST Endpoints ---

class Item(BaseModel):
    """Example Pydantic model for POST request body."""
    name: str
    description: str | None = None
    price: float
    is_offer: bool | None = None

@router.post("/post", status_code=status.HTTP_201_CREATED)
async def create_item(item: Item):
    """
    POST endpoint example.
    Receives an item and publishes a notification to subscribers.
    """
    logger.info(f"POST /post called with item: {item.model_dump()}")

    # Here you would typically save the item to a database

    # Publish a notification about the new item to all subscribers
    try:
        # You can publish the whole item dict or just a summary string
        await pubsub_manager.publish(f"New item created: {item.name} (Price: {item.price})")
        # Alternatively publish structured data (e.g., JSON string or dict)
        # import json
        # await pubsub_manager.publish(json.dumps({"event": "item_created", "data": item.model_dump()}))
    except Exception as e:
        logger.error(f"Failed to publish message after creating item: {e}")
        # Decide if failure to publish should cause a server error response
        # raise HTTPException(status_code=500, detail="Item created but failed to notify subscribers")

    return {"message": "Item created successfully", "item_received": item}

# Add more GET and POST endpoints as needed following the pattern /get/... or /post
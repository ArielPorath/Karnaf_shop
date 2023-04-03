import logging

import redis
import json
from karnaf_shop.core.config import settings
from fastapi import APIRouter, HTTPException

api_router = APIRouter()

redis_db = redis.StrictRedis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    password=settings.REDIS_PASSWORD,
    decode_responses=True,
)

@api_router.get("/hello")
async def hello_world():
    return {"message": "Hello, world!"}

@api_router.get("/get_item/")
async def get_item(item_name: str):
    item_value = redis_db.hget("items", item_name)
    values = json.loads(item_value)
    if not item_value:
        raise HTTPException(status_code=400, detail="Item not found")
    return {"price": values["price"], "quantity": values["quantity"]}

@api_router.put("/add_item/")
async def add_item(item_name: str, price: int, quantity: int):
    data = json.dumps({"price": price, "quantity": quantity})
    redis_db.hset("items", item_name, data)
    return {"message": f"Item {item_name} added successfully"}

@api_router.get("/list_items/")
async def list_items():
    items = dict()
    for key in redis_db.hkeys("items"):
        try:
            redis_value = redis_db.hget("items", key)
            values = json.loads(redis_value)
            items[key] = values
        except Exception as ex:
            continue
    return {"message": items}
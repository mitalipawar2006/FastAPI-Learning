from fastapi import FastAPI
from pydantic import BaseModel
import asyncio
import time

app = FastAPI(
    title="Simple Message API",
    description="A simple API to demonstrate HTTP methods and routing in FastAPI.",
    version="1.0.0"
)


class Message(BaseModel):
    text: str
    sender: str


messages_db = []


@app.get("/")
async def read_root():
    return {
        "message": "Welcome to the Simple Message API!"
    }


@app.get("/hello")
async def say_hello():
    return {
        "greeting": "Hello there!"
    }


@app.get("/async-example/")
async def get_async_example():
    await asyncio.sleep(3)

    return {
        "status": "success",
        "data": "Async operation completed successfully!",
        "timestamp": time.time()
    }


@app.post("/messages/")
async def create_message(message: Message):

    print(f"Received message from {message.sender}: {message.text}", flush=True)

    messages_db.append(message.model_dump())

    return {
        "status": "success",
        "message_received": message.text,
        "from_sender": message.sender,
        "total_messages_stored": len(messages_db)
    }


@app.get("/messages/")
async def get_all_messages():
    return {
        "messages": messages_db
    }


@app.get("/sync-example/")
def get_sync_example():
    time.sleep(5)

    return {
        "status": "success",
        "data": "Sync operation completed (blocking)!",
        "timestamp": time.time()
    }
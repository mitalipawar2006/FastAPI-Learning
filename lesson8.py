from fastapi import FastAPI
from pydantic import BaseModel

# Create FastAPI application
app = FastAPI()

# Pydantic model
class Message(BaseModel):
    text: str
    sender: str

# GET endpoint - Home
@app.get("/")
def read_root():
    return {"message": "नमस्ते! FastAPI की दुनिया में आपका स्वागत है।"}

# GET endpoint - Hello
@app.get("/hello")
def say_hello():
    return {"greeting": "Hello from the /hello endpoint!"}

# POST endpoint
@app.post("/messages/")
def create_message(message: Message):
    print(f"Received message from {message.sender}: {message.text}")

    return {
        "status": "success",
        "received_message": message.text,
        "from_sender": message.sender
    }
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
    return {
        "message": "Welcome to the world of FastAPI!"
    }

# GET endpoint - Hello
@app.get("/hello")
def say_hello():
    return {
        "greeting": "Hello from the /hello endpoint!"
    }

# POST endpoint
@app.post("/messages/")
def create_message(message: Message):

    # Print the received message in the terminal
    print(f"Received message from {message.sender}: {message.text}")

    # Return a response to the client
    return {
        "status": "success",
        "received_message": message.text,
        "from_sender": message.sender
    }
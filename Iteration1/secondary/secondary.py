# secondary.py
from fastapi import FastAPI, HTTPException
import time

app = FastAPI()
replicated_messages = []


@app.post("/replicate")
def replicate_message(message: str):
    # Simulate a delay in receiving the message for testing blocking replication
    time.sleep(2)

    # Append the replicated message to the in-memory list
    replicated_messages.append(message)

    return {"message": "Message replicated successfully"}


@app.get("/get_replicated_messages")
def get_replicated_messages(message: str):
    return {"replicated_messages": replicated_messages}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8001)

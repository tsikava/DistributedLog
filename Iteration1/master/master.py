# master.py
from fastapi import FastAPI, HTTPException
import requests
import time

app = FastAPI()
messages = []

SECONDARIES = ["http://localhost:8001"]  


@app.post("/append_message")
def append_message(message: str):
    # Append the message to the in-memory list
    messages.append(message)

    # Replicate the message to all Secondaries
    for secondary_url in SECONDARIES:
        try:
            response = requests.post(f"{secondary_url}/replicate", json={"message": message})
            response.raise_for_status()
        except requests.exceptions.RequestException as e:
            raise HTTPException(status_code=500, detail=f"Failed to replicate message to {secondary_url}: {str(e)}")

    return {"message": "Message appended and replicated successfully"}


@app.get("/get_messages")
def get_messages():
    return {"messages": messages}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)

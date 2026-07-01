import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI

load_dotenv()

prefix = os.environ.get("STAGE", "dev")

app = FastAPI()

@app.get("/")
async def get():
    return {"status": 200, "message": "Dummy function"}

@app.get("/second")
async def get():
    return {"status": 200, "message": "Second Dummy function"}

if __name__ == "__main__":
    uvicorn.run("api:app", port=80, log_level="info")
    
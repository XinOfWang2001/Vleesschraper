import os

from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import URL
# Just for the sake of testing
from src.logic import DataLoader, WebPage

load_dotenv()

app = FastAPI()

# Connection string from collection database.
connection_string_collect= URL.create(
    drivername=os.environ.get("DRIVER"),
    username=os.environ.get("USER_NAME"),
    password=os.environ.get("PASSWORD"),
    host=os.environ.get("HOST"),
    port=os.environ.get("PORT"),
    database=os.environ.get("DATABASE")
)

data_loader = DataLoader(connection_string_collect)

@app.get("/synchronise")
async def get():
    return {"status": 200, "message": "Dummy function"}
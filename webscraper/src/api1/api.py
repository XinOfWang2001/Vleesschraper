import os

from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import URL
from src.logic import (AlbertMenuParser, CollectionPipeline, DataLoader,
                       WebRetriever)

AH_URL = "https://www.ah.nl/producten/9344/vlees"
URL_INTERNAL = ""

load_dotenv()

print(f"=== Connection ==: {os.environ.get("COLLECT_DB_ALCHEMY")}")
connection_string_collect= URL.create(
    drivername="postgresql",
    username="hero",
    password="localpassword",
    host="localhost",
    database="hero"
)
web = WebRetriever(AH_URL)
albert_heijn = AlbertMenuParser(web)
data_loader = DataLoader(connection_string_collect)
app = FastAPI()

@app.get("/")
async def get():
    return albert_heijn.parse()

@app.post("/run")
async def run_pipeline():
    pipeline = CollectionPipeline(web, data_loader)
    answer = pipeline.execute()
    return {"status": 200, "successfull": answer}

import os

from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import URL
from src.logic import (AlbertMenuParser, CollectionPipeline, DataLoader,
                       WebRetriever)

AH_URL = "https://www.ah.nl/producten/9344/vlees"

load_dotenv()

connection_string_collect= URL.create(
    drivername=os.environ.get("DRIVER"),
    username=os.environ.get("COLLECT_USER_NAME"),
    password=os.environ.get("COLLECT_PASSWORD"),
    host=os.environ.get("COLLECT_HOST"),
    database=os.environ.get("COLLECT_DATABASE")
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

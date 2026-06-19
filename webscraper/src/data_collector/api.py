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
    username=os.environ.get("USER_NAME"),
    password=os.environ.get("PASSWORD"),
    host=os.environ.get("HOST"),
    port=os.environ.get("PORT"),
    database=os.environ.get("DATABASE")
)
print(connection_string_collect)
web = WebRetriever(AH_URL)
albert_heijn_parser = AlbertMenuParser(web)
data_loader = DataLoader(connection_string_collect)
app = FastAPI()

@app.get("/")
async def get():
    return albert_heijn_parser.parse()

@app.post("/run")
async def run_pipeline():
    try:
        pipeline = CollectionPipeline(albert_heijn_parser, data_loader)
        answer = pipeline.execute()
        return {"status": 200, "successfull": answer}
    except Exception as exc:
        return {"status": 500, "message": exc.args}
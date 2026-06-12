from fastapi import FastAPI

from src.logic import DataLoader, AlbertMenuParser, WebRetriever

URL = "https://www.ah.nl/producten/9344/vlees"
URL_INTERNAL = ""

web = WebRetriever(URL)
albert_heijn = AlbertMenuParser(web)

app = FastAPI()

@app.get("/")
async def get():
    return albert_heijn.parse()
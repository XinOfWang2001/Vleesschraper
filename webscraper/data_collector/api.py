import os

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import URL
from src.logic import (AlbertMenuParser, CollectionPipeline, DataLoader,
                       WebRetriever)

AH_URL = "https://www.ah.nl/producten/9344/vlees"

load_dotenv()

print(os.environ.get("Hond", "Vul hond in!"))
print(os.environ.get("STAGE", "dev"))
stage = os.environ.get("STAGE", "dev")
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
app = FastAPI(root_path=stage)

# Solution scheduled tasks.

# Data collector
# - Lambdas --> Eerste optie, Gefaald, kan niet via FastAPI aangeroepen worden en niet makkelijk te wisselen van implementatie.
# - AWS ECS Tasks -> https://aws.amazon.com/ecs/?nc2=h_prod_cp_ecs&trk=ft_ec2
# - Google Cloud Tasks

# Data Synchronisizer & API
# - AWS CS2
# - Google Cloud compute

# SQL-Database
# - Azure SQL-Server -> https://azure.microsoft.com/en-us/pricing/free-services#Free-service-types
# - AWS Aurora RDS -> https://aws.amazon.com/rds/aurora/?refid=ft_ec2

@app.put("/run-pipeline")
async def run_pipeline():
    try:
        pipeline = CollectionPipeline(albert_heijn_parser, data_loader)
        answer = pipeline.execute()
        return {"status": 200, "successfull": answer}
    except Exception as exc:
        exc.with_traceback()
        return {"status": 500, "message": exc.args}
    
@app.get("/health")
async def health():
    return {"status": 200, "health": os.environ.get("Hond", "Vul hond in!") }
    
if __name__ == "__main__":
    uvicorn.run("main:app", port=5000, log_level="info")
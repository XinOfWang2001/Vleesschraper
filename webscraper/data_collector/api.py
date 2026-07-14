import os

from dotenv import load_dotenv
from fastapi import FastAPI
from sqlalchemy import URL
from src import AlbertMenuParser, CollectionPipeline, DataLoader, WebRetriever

AH_URL = "https://www.ah.nl/producten/9344/vlees"

load_dotenv()

stage = os.environ.get("STAGE", "dev")
connection_string_collect= URL.create(
    drivername=os.environ.get("DRIVER"),
    username=os.environ.get("USER_NAME"),
    password=os.environ.get("PASSWORD"),
    host=os.environ.get("HOST"),
    port=os.environ.get("PORT"),
    database=os.environ.get("DATABASE")
)

web = WebRetriever(AH_URL)
albert_heijn_parser = AlbertMenuParser(web)
data_loader = DataLoader(connection_string_collect)
app = FastAPI(root_path=stage)

# Solution scheduled tasks.

# Data collector
# - Lambdas --> Eerste optie, Gefaald, kan niet via FastAPI aangeroepen worden en niet makkelijk te wisselen van implementatie.
# - AWS ECS Tasks -> https://aws.amazon.com/ecs/?nc2=h_prod_cp_ecs&trk=ft_ec2 || Onhandig opzetten. Andere manier vinden.
# - Google Cloud Tasks

# Data Synchronisizer & API
# - AWS CS2
# - Google Cloud compute

# SQL-Database
# - Azure SQL-Server -> https://azure.microsoft.com/en-us/pricing/free-services#Free-service-types
# - AWS Aurora RDS -> https://aws.amazon.com/rds/aurora/?refid=ft_ec2

def run_pipeline():
    try:
        pipeline = CollectionPipeline(albert_heijn_parser, data_loader)
        pipeline.execute()
    except Exception as exc:
        exc.with_traceback()
    
if __name__ == "__main__":
    # Will be deployed as serverless functions.
    # Can be used within AWS ECS.
    run_pipeline()
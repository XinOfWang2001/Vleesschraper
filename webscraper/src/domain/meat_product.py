from dataclasses import dataclass
from datetime import datetime

from pydantic import BaseModel

class MeatProduct(BaseModel):
    date_time: datetime
    supermarket: str 
    full_title: str 
    capitilized_title: str 
    normal_price: float 
    current_price: float 
    weight: int 
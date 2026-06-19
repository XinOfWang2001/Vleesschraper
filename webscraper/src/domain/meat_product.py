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

    def get_date_code(self):
        return int(f"{self.date_time.year}{self.date_time.month}{self.date_time.day}{self.date_time.hour}{self.date_time.minute}")
    
    def get_unique_name(self):
        return f"{self.full_title.capitalize()} - {self.weight}"
    
    def get_tuple(self):
        return (
            self.get_date_code(), 
            self.supermarket, 
            self.full_title, 
            self.get_unique_name(), 
            self.normal_price, 
            self.current_price, 
            0,
            self.weight)
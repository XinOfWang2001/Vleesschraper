from dataclasses import dataclass
from datetime import datetime

@dataclass
class WebPage:
    url: str 
    date_time: datetime
    html_content: list[str]
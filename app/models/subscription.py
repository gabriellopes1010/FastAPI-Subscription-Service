from pydantic import BaseModel
from datetime import datetime

class Subscription(BaseModel):
    username: str
    monthly_fee: float
    start_date: datetime
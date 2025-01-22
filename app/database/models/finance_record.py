from pydantic import BaseModel
from datetime import datetime
class Asset(BaseModel):
    id:int
    financial_category: str
    asset_code: str
    asset_full_name: str
    currency: str
    open: float
    close: float
    high: float
    low: float
    timestamp: int
    date_and_time: datetime

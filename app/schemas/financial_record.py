from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class FinancialCategory(str, Enum):
    FUTURES = "futures"
    STOCKS = "stocks"

class AssetSchema(BaseModel):
    id: int
    financial_category: FinancialCategory
    asset_code: str
    asset_full_name: str
    currency: str
    open: float
    close: float
    high: float
    low: float
    timestamp: int
    date_and_time: datetime
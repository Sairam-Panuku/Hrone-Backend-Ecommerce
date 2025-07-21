from pydantic import BaseModel
from typing import List, Optional

class ProductModel(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    size: Optional[str] = None
    tags: Optional[List[str]] = []

class ProductInDB(ProductModel):
    id: str

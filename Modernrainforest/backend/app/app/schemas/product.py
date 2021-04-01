from typing import Optional,Any
from datetime import date, datetime, time, timedelta
from pydantic import BaseModel


# Shared properties
class ProductBase(BaseModel):
    category_id: Optional[str] = None
    category: Optional[str] = None
    asin: Optional[str] = None
    plink: Optional[str] = None
    brand: Optional[str] = None
    price: Optional[str] = None
    rating: Optional[str] = None 
    ranking: Optional[int] = None
    msales: Optional[str] = None
    date: Optional[Any] = None
    dimensions: Optional[str] = None
    imagelink: Optional[str] = None
# Properties to receive on Product creation
class ProductCreate(ProductBase):
    pass

# Properties to receive on Product update
class ProductUpdate(ProductBase):
    pass


# Properties shared by models stored in DB
class ProductInDBBase(ProductBase):
    category_id: int
    category: str
    class Config:
        orm_mode = True


# Additional properties to return via API
class Product(ProductInDBBase):
#    productimages: Optional[str] = None
    pass

# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass

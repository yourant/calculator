from typing import Optional

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
    first_date: Optional[str] = None
    dimensions: Optional[str] = None



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


# Properties to return to client
class Product(ProductInDBBase):
    pass


# Properties properties stored in DB
class ProductInDB(ProductInDBBase):
    pass

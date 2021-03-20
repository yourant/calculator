from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import relationship

from app.db.base_class import Base

if TYPE_CHECKING:
    from .productimage import ProductImage  # noqa: F401

class Product(Base):
    category_id = Column(String)
    category = Column(String)
    asin = Column(String, primary_key=True, index=True)
    plink = Column(String)
    brand = Column(String)
    price = Column(String)
    rating = Column(String)
    ranking = Column(Integer)
    msales = Column(String)
    date = Column(DateTime)
    dimensions = Column(String)
    imagelink = Column(String)
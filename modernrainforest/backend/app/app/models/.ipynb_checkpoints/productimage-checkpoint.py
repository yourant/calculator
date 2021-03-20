from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.relationships import foreign

from app.db.base_class import Base

if TYPE_CHECKING:
    from .product import Product

class ProductImage(Base):
    index = Column(Integer, primary_key=True, index=True)
    category_id = Column(String)
    asin = Column(String, ForeignKey("product.asin"))
    imageLink = Column(String)
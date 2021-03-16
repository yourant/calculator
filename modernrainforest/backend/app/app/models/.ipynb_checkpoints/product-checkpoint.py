from typing import TYPE_CHECKING

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from app.db.base_class import Base



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
    first_date = Column(String)
    dimensions = Column(String)

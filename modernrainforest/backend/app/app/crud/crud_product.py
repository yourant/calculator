from typing import List

from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session

from app.crud.base import CRUDBase
from app.models.product import Product
from app.models.productimage import ProductImage
from app.schemas.product import ProductCreate, ProductCreate


class CRUDProduct(CRUDBase[Product, ProductCreate, ProductCreate]):
    def get_multi_by_category(
        self, db: Session, *, category: str, skip: int = 0, limit: int = 100
    ) -> List[Product]:
        return (
            db.query(self.model)
            .filter(Product.category == category)
            .offset(skip)
            .limit(limit)
            .all()
        )


product = CRUDProduct(Product)

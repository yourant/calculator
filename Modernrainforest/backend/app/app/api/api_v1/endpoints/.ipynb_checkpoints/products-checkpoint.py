from typing import Any, List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, models, schemas
from app.api import deps

router = APIRouter()


@router.get("/{category}", response_model=List[schemas.Product])
def read_products(
    db: Session = Depends(deps.get_db),
    skip: int = 0,
    limit: int = 100,
    category: str = None,
) -> Any:
    """
    Retrieve products.
    """

    products = crud.product.get_multi_by_category(
        db=db, category=category, skip=skip, limit=limit
    )
    return products
from fastapi import APIRouter
from passlib.context import CryptContext
from ..import schemas, models
from sqlalchemy.orm import Session
from fastapi.params import Depends
from ..database import get_db

router = APIRouter(
    tags=["Seller"],
    prefix="/seller"
)

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Sellers
@router.post("", response_model=schemas.DisplaySeller)
def create_seller(request: schemas.Seller, db: Session = Depends(get_db)):
    hashed_password = pwd_context.hash(request.password)
    new_seller = models.Seller(
        username=request.username,
        email = request.email,
        password = hashed_password
    )
    db.add(new_seller)
    db.commit()
    db.refresh(new_seller)
    return new_seller
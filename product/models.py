from sqlalchemy import Column, Integer, String, ForeignKey
from .database import Base
from sqlalchemy.orm import Relationship

class Product(Base):
    __tablename__ = 'products'
    id = Column(Integer, primary_key = True, index= True)
    name = Column(String)
    description = Column(String)
    price = Column(Integer)
    seller_id = Column(Integer, ForeignKey("sellers.id"))
    seller = Relationship("Seller", back_populates="products")


class Seller(Base):
    __tablename__ = "sellers"
    id = Column(Integer, primary_key = True, index= True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    products = Relationship("Product", back_populates="seller")

from fastapi import FastAPI
from .import models
from .database import engine
from .router import product, seller

app = FastAPI(
    title="Products API",
    description="Get details for all the products on our website",
    terms_of_service="http://www.google.com",
    contact={
        "Dev name": "Vaibhav Chichmalkar",
        "website": "http://www.google.com",
        "email": "demo@gmail.com"
    },
    license_info={
        "name": "XYZ",
        "url": "http://www.google.com"
    },
)

app.include_router(product.router)
app.include_router(seller.router)

models.Base.metadata.create_all(engine)


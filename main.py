from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models
import schemas
from database import engine, SessionLocal

# Create tables in PostgreSQL
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# ----------------------
# DB Dependency
#which means when a paricular api call that time it will creae session and after finsihing call it will automaitcally close
# ----------------------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ----------------------
# CREATE PRODUCT
# ----------------------
#here we send data from the use as json body and it will be converted to pydantic model by fastapi and then we will convert it to sqlalchamy model then send it to database

@app.post("/products", response_model=schemas.ProductResponse)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
     #here the data type of produc is like productcreate(name="abc", description="xyz", price=10.0, quantity=5) and we convert it to dict and then send it to sqlalchamy model
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


# ----------------------
# GET ALL PRODUCTS
# ----------------------
@app.get("/products", response_model=list[schemas.ProductResponse])
def get_products(db: Session = Depends(get_db)):

    return db.query(models.Product).all()


# ----------------------
# GET SINGLE PRODUCT
# ----------------------
@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(product_id: int, db: Session = Depends(get_db)):

    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    return product


# ----------------------
# UPDATE PRODUCT
# ----------------------
@app.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(
    product_id: int,
    updated: schemas.ProductCreate,
    db: Session = Depends(get_db)
):

    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    for key, value in updated.dict().items():
        setattr(product, key, value)

    db.commit()
    db.refresh(product)

    return product


# ----------------------
# DELETE PRODUCT
# ----------------------
@app.delete("/products/{product_id}")
def delete_product(product_id: int, db: Session = Depends(get_db)):

    product = db.query(models.Product).filter(models.Product.id == product_id).first()

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    db.delete(product)
    db.commit()

    return {"message": "Product deleted successfully"}

#----CLEAR SUMMARY OF WHAT HAPPENING IN THIS CODE----

#frontend send json
#     {
#   "name": "Phone",
#   "price": 500
# }
    
#fast api converted to pydentic model
# ProductCreate(name="Phone", price=500)

#then we convert it to sqlalchamy model
# Product(name="Phone", price=500)

#then we send it to database and after that we get response from database with id as well
# Product(id=1, name="Phone", price=500)


#when we get response from database we convert it to pydantic model and then send it to frontend as json
# ProductResponse(id=1, name="Phone", price=500) -> {"id": 1, "name": "Phone", "price": 500} actually python fastapi is changing 



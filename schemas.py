from pydantic import BaseModel

# input (create product)
#it is creation of product it is based on the pydantic it handle data validation even if i give wrong data type it recreate it correctly 
#and send it to database
class ProductCreate(BaseModel):
    name: str
    description: str
    price: float
    quantity: int


# output (response)
#this is the output response from the database it give response with id aswell 
class ProductResponse(ProductCreate):
    id: int

    class Config:
        from_attributes = True
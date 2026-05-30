from sqlalchemy import Column, Integer, String, Float
from database import Base


#it is for postgresql it gives instruction to pgsql to how to create the table which one is primary key which one 
#how other datas should be bla bla 
class Product(Base):
    __tablename__ = "products1"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    quantity = Column(Integer)
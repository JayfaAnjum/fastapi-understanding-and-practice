# this is the orm when u have it u dont need to write any queries of postgresql
from sqlalchemy import create_engine;
from sqlalchemy.orm import sessionmaker,declarative_base;
from dotenv import load_dotenv;
import os;

# this is the function
load_dotenv()
DATABASE_URL=os.getenv("DATABASE_URL")
print(DATABASE_URL)
engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()
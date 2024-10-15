from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

SQLALCHEMY_DATABASE_URL = "postgresql://sit722_postgresql_9w3y_user:IDG6pPXNMHoajzPHmNdwy6I8zUQHc5sz@dpg-cs6fend6l47c73fdgrrg-a.oregon-postgres.render.com/sit722_postgresql_9w3y" #os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from common.config import DATABASE_URL

# Create DB engine using the DATABASE_URL from config.py
engine = create_engine(DATABASE_URL, echo=True)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base model for ORM models
Base = declarative_base()

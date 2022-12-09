from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseSettings

DATABASE_URL = 'sqlite:///./database.db'
connect_args = {"check_same_thread": False}

engine = create_engine(DATABASE_URL, connect_args=connect_args, echo=True)

session = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

class Settings(BaseSettings):
    DATABASE_URL: Optional[str] = None
    SECRET_KEY: Optional[str] = "default"
    ALGORTIM: Optional[str] = "HS256"

    class Config:
        env_file = ".env"

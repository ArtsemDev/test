from os import getenv

from sqlalchemy import INT, Column, VARCHAR, create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

__all__ = [
    "Base",
    "Request",
    "engine",
    "session_maker"
]


class Base(DeclarativeBase):
    pass


class Request(Base):
    __tablename__ = "requests"
    
    id = Column(INT, primary_key=True)
    name = Column(VARCHAR, nullable=False)
    
    def __str__(self):
        return self.name
    

engine = create_engine(getenv("DB_URL"))
session_maker = sessionmaker(bind=engine)

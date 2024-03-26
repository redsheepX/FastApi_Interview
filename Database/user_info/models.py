from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

db = declarative_base()


class User(db):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

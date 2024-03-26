from pathlib import Path

if __name__ == "__main__":
    import sys

    sys.path.append(str(Path.cwd()))

from sqlalchemy import Column, Integer, String
from Database.user_info.database import db


class User(db):
    __tablename__ = "user"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    password = Column(String)

    def __str__(self):
        return self.name

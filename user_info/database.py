from pathlib import Path

if __name__ == "__main__":
    import sys

    sys.path.append(str(Path.cwd()))

from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from setting import setup

db = declarative_base()
ENGINE_PATH = setup.USER_INFO_DATABASE_PATH
ENGINE_URL = f"sqlite:///{str(ENGINE_PATH)}"
engine = create_engine(ENGINE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

from pathlib import Path

if __name__ == "__main__":
    import sys

    sys.path.append(str(Path.cwd()))

from sqlalchemy.orm import Session
from Database.user_info import models, schemas
from Database.user_info.database import create_session
from setting.setup import logger


def add_new_user(db: Session, user: schemas.UserCreate):
    user_data = {
        "name": user.name,
        "email": user.email,
        "password": user.password,
    }
    try:
        db_user = models.User(**user_data)
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    except Exception as e:
        logger.error(f"{e.__class__.__name__} : {str(e)}")
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def get_data(db: Session, search_filter: dict):
    try:
        result = db.query(models.User).filter_by(**search_filter).first()
    except Exception as e:
        logger.error(f"{e.__class__.__name__} : {str(e)}")
    return result


def get_user_by_id(db: Session, user_id: int):
    try:
        result = db.query(models.User).filter_by(models.User.id == user_id).first()
    except Exception as e:
        logger.error(f"{e.__class__.__name__} : {str(e)}")
    return result


def update_data(db: Session): ...


def delete_data(db: Session): ...

from pathlib import Path

if __name__ == "__main__":
    import sys

    sys.path.append(str(Path.cwd()))

from sqlalchemy.orm import Session
from user_info import models, schemas
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


def get_users(db: Session, skip: int = 0, limit: int = 100) -> list[models.User]:
    return db.query(models.User).offset(skip * limit).limit(limit).all()


def get_data(db: Session, search_filter: dict) -> models.User | None:
    try:
        result = db.query(models.User).filter(**search_filter).first()
    except Exception as e:
        logger.error(f"{e.__class__.__name__} : {str(e)}")
    return result


def get_user_by_id(db: Session, user_id: int) -> models.User | None:
    try:
        result = db.query(models.User).filter(models.User.id == user_id).first()
        return result
    except Exception as e:
        logger.error(f"{e.__class__.__name__} : {str(e)}")


def get_user_by_email(db: Session, user_email: int):
    try:
        result = db.query(models.User).filter(models.User.email == user_email).first()
    except Exception as e:
        logger.error(f"{e.__class__.__name__} : {str(e)}")
    return result


def update_user_data(db: Session, user_id: int, user: schemas.UserUpdate) -> models.User | None:
    try:
        db.query(models.User).filter(models.User.id == user_id).update(user)
        db.commit()
        return get_user_by_id(db, user_id)
    except Exception as e:
        logger.error(f"{e.__class__.__name__} : {str(e)}")


def delete_user_data(db: Session, user_id: int) -> bool:
    try:
        db.query(models.User).filter(models.User.id == user_id).delete()
        db.commit()
        return True
    except Exception as e:
        logger.error(f"{e.__class__.__name__} : {str(e)}")
        return False


if __name__ == "__main__":
    ...

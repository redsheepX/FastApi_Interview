from pathlib import Path

if __name__ == "__main__":
    import sys

    sys.path.append(str(Path.cwd()))

from fastapi import FastAPI, Request, Depends, HTTPException
from sqlalchemy.orm import Session
from setting.setup import logger
from user_info import models, CRUD, schemas
from user_info.database import SessionLocal, engine
from FastApi import error_code
from email_validator import validate_email, EmailNotValidError

models.db.metadata.create_all(bind=engine)
app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/")
async def read_root(request: Request):
    return {"Hello": "World"}


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = CRUD.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=error_code.en_US.USER_NOT_FOUND)
    return db_user


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    try:
        email_info = validate_email(user.email, check_deliverability=True)
        user.email = email_info.normalized
    except EmailNotValidError as e:
        raise HTTPException(status_code=400, detail=f"{error_code.en_US.EMAIL_NOT_VALID} : {e}")
    db_user = CRUD.get_user_by_email(db, user_email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail=error_code.en_US.EMAIL_ALREADY_REGISTERED)
    return CRUD.add_new_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = CRUD.get_users(db, skip=skip, limit=limit)
    return users


def get_language_setup(language): ...

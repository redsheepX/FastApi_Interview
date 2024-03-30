from pathlib import Path

if __name__ == "__main__":
    import sys

    sys.path.append(str(Path.cwd()))

from fastapi import FastAPI, Depends, HTTPException, Request, Response
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from user_info import models, CRUD, schemas
from user_info.database import SessionLocal, engine
from FastApi.error_code import error_hint
from email_validator import validate_email, EmailNotValidError
from markdown import markdown
from setting import setup
from setting.setup import logger

models.db.metadata.create_all(bind=engine)
app = FastAPI()


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    logger.debug(f"{request.client.host}:{request.client.port} | {request.url}")
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)

    finally:
        request.state.db.close()
    return response


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.get("/", response_class=HTMLResponse)
async def show_readme(request: Request):
    """顯示readme_for_FastAPI.md的內容"""

    try:
        with open(setup.READ_ME_MD_PATH, "r", encoding="utf-8") as f:
            markdown_content = f.read()

        html_content = markdown(markdown_content)

        html_response = f"""
        <html>
            <head>
                <title>使用說明</title>
            </head>
            <body>
                {html_content}
            </body>
        </html>
        """

        return html_response

    except FileNotFoundError:
        raise HTTPException(status_code=404, detail="File not found")


@app.get("/user/{user_id}", response_model=schemas.User)
def get_user(user_id: int, db: Session = Depends(get_db)):
    """依照id列出user"""

    db_user = CRUD.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=error_hint.USER_NOT_FOUND)
    return db_user


@app.patch("/user/{user_id}", response_model=schemas.User)
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    """依照id更新user資訊"""
    db_user = CRUD.get_user_by_id(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail=error_hint.USER_NOT_FOUND)
    user_data = user.model_dump(exclude_unset=True)
    db_user = CRUD.update_user_data(db, user_id=user_id, user=user_data)
    return db_user


@app.delete("/user/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """依照id刪除user"""
    try:
        assert CRUD.get_user_by_id(db, user_id=user_id) is not None
    except Exception:
        raise HTTPException(status_code=400, detail=f"{error_hint.USER_NOT_FOUND}")

    delete_success = CRUD.delete_user_data(db, user_id=user_id)
    if delete_success:
        return HTTPException(status_code=200, detail=f"{error_hint.SUCCESS}")
    else:
        return HTTPException(status_code=400, detail=f"{error_hint.DELETE_FAIL}")


@app.post("/user/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """創建新的user"""
    try:
        email_info = validate_email(user.email, check_deliverability=True)
        user.email = email_info.normalized
    except EmailNotValidError as e:
        raise HTTPException(status_code=400, detail=f"{error_hint.EMAIL_NOT_VALID} : {e}")
    db_user = CRUD.get_user_by_email(db, user_email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail=error_hint.EMAIL_ALREADY_REGISTERED)
    return CRUD.add_new_user(db=db, user=user)


@app.get("/users/", response_model=list[schemas.User])
def get_users(page: int = 1, limit: int = 100, db: Session = Depends(get_db)):
    """查看user列表"""
    users = CRUD.get_users(db, skip=page - 1, limit=limit)
    return users

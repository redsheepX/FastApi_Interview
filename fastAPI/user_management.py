from pathlib import Path

if __name__ == "__main__":
    import sys

    sys.path.append(str(Path.cwd()))

from fastapi import FastAPI, Request
from setting import setup
from setting.setup import logger
from Database.user_info.CRUD import user_info_database_control

app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/user/{user_id}")
async def get_user_by_id(request: Request, user_id: int):
    logger.info(f"GET   {request.client.host}:{request.client.port}")
    print(request.client)
    return {f"user_id:{user_id}": user_info_database_control().get_user_by_id(user_id)}

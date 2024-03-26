from pathlib import Path

if __name__ == "__main__":
    import sys

    sys.path.append(str(Path.cwd()))

from fastapi import FastAPI, Request
from setting.setup import logger


app = FastAPI()


@app.get("/")
async def read_root(request: Request):
    return {"Hello": "World"}

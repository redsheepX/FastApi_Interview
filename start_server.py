import uvicorn
from setting import setup

if __name__ == "__main__":
    uvicorn.run(app="fastAPI.user_management:app", host=setup.SERVER_HOST_IP, port=setup.SERVER_PORT, reload=True)

from pathlib import Path
from loguru import logger
from datetime import datetime

logger.add(f"log/{datetime.date(datetime.now())}.log", retention="2 days")

SERVER_HOST_IP = "127.0.0.1"
SERVER_PORT = 8010

USER_INFO_DATABASE_FILE_NAME = "user_info.db"
USER_INFO_PATH = Path(__file__).parent.parent.joinpath("user_info")
USER_INFO_DATABASE_PATH = Path(__file__).parent.parent.joinpath(USER_INFO_PATH, USER_INFO_DATABASE_FILE_NAME)

# for test db
TEST_USER_INFO_DATABASE_FILE_NAME = "test_user_info.db"
TEST_USER_INFO_PATH = Path(__file__).parent.parent.joinpath("user_info", "test")
TEST_USER_INFO_DATABASE_PATH = Path(__file__).parent.parent.joinpath(
    TEST_USER_INFO_PATH, TEST_USER_INFO_DATABASE_FILE_NAME
)

READ_ME_MD_PATH = Path(__file__).parent.parent.joinpath("readme.md")

from pathlib import Path

if __name__ == "__main__":
    import sys

    sys.path.append(str(Path.cwd()))

from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from user_info import models
from FastApi.user_management import app, get_db
import allure
import pytest

DATABASE_URL = "sqlite://"
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False},
    poolclass=StaticPool,
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

models.db.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)


class Test_database:
    @allure.step("create_user")
    def test_create_user(self):
        """測試創建用戶"""
        response = client.post(
            "/user/",
            json={"name": "oliver", "email": "oliver@gmail.com", "password": "interview1234"},
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["email"] == "oliver@gmail.com", "email比對異常"
        assert "id" in data, "id欄位異常"
        user_id = data["id"]

        response = client.get(f"/user/{user_id}")
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["email"] == "oliver@gmail.com"
        assert data["id"] == user_id

    @allure.step("update_user")
    def test_update_user(self):
        response = client.patch(
            "/user/1",
            json={"name": "oliver_2", "email": "oliver_2@gmail.com"},
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["email"] == "oliver_2@gmail.com", "email比對異常"
        assert "id" in data, "id欄位異常"
        response = client.get("/user/1")
        assert response.status_code == 200, response.text
        data = response.json()
        assert data["email"] == "oliver_2@gmail.com"
        assert data["name"] == "oliver_2"
        assert data["id"] == 1

    @allure.step("get_users")
    def test_get_users(self):
        response = client.get(
            "/users/",
        )
        assert response.status_code == 200, response.text
        data = response.json()
        assert isinstance(data, list)
        assert data[0]["email"] == "oliver_2@gmail.com"
        assert data[0]["name"] == "oliver_2"
        assert data[0]["id"] == 1

    @allure.step("delete_user")
    def test_delete_user(self):
        response = client.delete(
            "/user/1",
        )
        assert response.status_code == 200, response.text
        assert response.json()
        response = client.get("/user/1")
        assert response.status_code == 404, response.text


def allure_test():
    import os

    from allure_combine import combine_allure

    pytest.main(["-q", "--alluredir=allure-results", "--clean-alluredir"])
    os.system("allure generate -c -o allure-report")
    combine_allure("allure-report", remove_temp_files=True)


if __name__ == "__main__":

    try:
        allure_test()
    except Exception:
        pytest.main(["-q"])

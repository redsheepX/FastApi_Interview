from pydantic import BaseModel


class UserBase(BaseModel):
    name: str | None = None
    email: str | None = None


class UserCreate(UserBase):
    password: str | None = None


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: str | None = None
    email: str | None = None
    password: int | None = None

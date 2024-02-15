from pydantic import BaseModel


class UserEntity(BaseModel):
    name: str
    email: str = None
    password: str

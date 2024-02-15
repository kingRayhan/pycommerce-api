import typing
from pydantic import BaseModel, Field, EmailStr


class CreateUserDto(BaseModel):
    name: str = Field(description="The name of the user", example="John Doe")
    email: EmailStr = Field(description="The email of the user", max_length=100, min_length=5)
    age: int = None
    password: str
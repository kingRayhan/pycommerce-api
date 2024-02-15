from pydantic import BaseModel, EmailStr


class LoginDTO(BaseModel):
    """
        Login Data Transfer Object
    """
    email: EmailStr
    password: str

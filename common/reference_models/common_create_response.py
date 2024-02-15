from pydantic import BaseModel


class CommonCreateResponse(BaseModel):
    id: str = None
    message: str = None

    class Config:
        orm_mode = True

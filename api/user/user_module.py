import typing

from fastapi import APIRouter, Body

from api.user.dtos.create_user_dto import CreateUserDto
from common.reference_models.common_create_response import CommonCreateResponse
from common.utils.encrypt import encrypt
from .user_service import UserService

routes = APIRouter()
user_service = UserService()


@routes.get("/")
async def users():
    return {"users": []}


@routes.post('/', response_model=CommonCreateResponse, status_code=201, description="Create a new user")
async def user(payload: typing.Annotated[CreateUserDto, Body(embed=True)]):
    res = await user_service.create_one({
        "name": payload.name,
        "email": payload.email,
        "password": encrypt(payload.password)
    })
    return CommonCreateResponse(id=str(res.inserted_id), message="User created successfully")

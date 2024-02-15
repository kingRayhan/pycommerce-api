from fastapi import APIRouter, Depends
from typing import Annotated

from fastapi.security import OAuth2PasswordBearer

from api.auth.auth_service import AuthService
from api.auth.dtos.login_dto import LoginDTO

routes = APIRouter()
auth_service = AuthService()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    # credentials_exception = HTTPException(
    #     status_code=status.HTTP_401_UNAUTHORIZED,
    #     detail="Could not validate credentials",
    #     headers={"WWW-Authenticate": "Bearer"},
    # )
    # try:
    #     payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    #     username: str = payload.get("sub")
    #     if username is None:
    #         raise credentials_exception
    #     token_data = TokenData(username=username)
    # except JWTError:
    #     raise credentials_exception
    # user = get_user(fake_users_db, username=token_data.username)
    # if user is None:
    #     raise credentials_exception
    return {
        "name": "John Doe",
    }


async def get_current_active_user(
        current_user: Annotated[any, Depends(get_current_user)]
):
    return current_user


@routes.post("/login")
async def login(payload: LoginDTO):
    token = await auth_service.login(email=payload.email, password=payload.password)
    return {"message": "Logged in successfully", "token": token}


@routes.post("/me")
async def me(current_user: Annotated[any, Depends(get_current_active_user)]):
    return current_user

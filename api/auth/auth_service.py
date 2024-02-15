from fastapi import HTTPException, status
from api.user.user_service import UserService
from common.utils.encrypt import compare
import jwt


class AuthService:
    def __init__(self):
        self.user_service = UserService()

    async def login(self, email, password):
        user = await self.user_service.find_one({"email": email})

        matched = compare(password, user["password"])

        if not matched:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

        return jwt.encode(
            payload={
                "sub": str(user["_id"]),
                "email": user["email"],
                "name": user["name"]
            }, key="secret", algorithm="HS256"
        )

from fastapi import FastAPI

from api.user.user_module import routes as user_routes
from api.auth.auth_module import routes as auth_routes

app = FastAPI(title="Ecommerce API", version="0.1")


@app.get("/")
def read_root():
    return {"Hello": "World"}

"""
    ------------------------------------------------------
    Api Routes
    ------------------------------------------------------
    |  Route   |   Description                             |
    ------------------------------------------------------
    | /users   |  User routes                              |
    ------------------------------------------------------  
"""
app.include_router(user_routes, prefix="/users", tags=["User"])
app.include_router(auth_routes, prefix="/auth", tags=["Auth"])

if __name__ == "__main__":
    import uvicorn
    import os
    from dotenv import load_dotenv

    load_dotenv()
    port = int(os.getenv("PORT", 4001))
    env = os.getenv("ENV", "development")

    uvicorn.run('main:app', port=port, reload=env == "development")

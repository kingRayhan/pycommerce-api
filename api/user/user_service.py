from common.database.database_repository import DatabaseRepository


class UserService(DatabaseRepository):
    def __init__(self):
        super().__init__("users")


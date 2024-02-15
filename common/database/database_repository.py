import typing

from common.database.mongodb import MongoDB


class DatabaseRepository:
    def __init__(self, collection_name: str):
        if collection_name is None:
            raise ValueError("collection_name is required")
        mongodb = MongoDB()
        self.database = mongodb.get_collection(collection_name)

    def create_one(self, data: typing.Dict):
        return self.database.insert_one(data)

    def find_one(self, query: typing.Dict):
        return self.database.find_one(query)

    def find(self, query: typing.Dict):
        return self.database.find(query)

    def update_one(self, query: typing.Dict, data: typing.Dict):
        return self.database.update_one(query, data)

    def delete_one(self, query: typing.Dict):
        return self.database.delete_one(query)
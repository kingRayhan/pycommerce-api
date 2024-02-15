import motor.motor_asyncio
import os
from dotenv import load_dotenv

load_dotenv()


class MongoDB:
    def __init__(self):
        self.url = os.getenv("MONGO_URI")
        self.db = os.getenv("MONGO_DB")

        self.client = motor.motor_asyncio.AsyncIOMotorClient(self.url)
        self.database = self.client[self.db]

    def get_collection(self, collection: str):
        return self.database[collection]

    async def close(self):
        self.client.close()


if __name__ == "__main__":
    db = MongoDB()
    print("Connected to MongoDB")
    print(f"MONGO_URL: {db.url}")
    print(f"MONGO_DB: {db.db}")

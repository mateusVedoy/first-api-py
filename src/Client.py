from pymongo.mongo_client import MongoClient
from pymongo.database import Database


class Client:
    access: MongoClient
    db: Database

    def __init__(self):
        self.access = MongoClient("mongodb://mongodb:27017")
        self.db = self.access["db"]
        try:
            self.access.admin.command('ping')
            print("Connected to MongoDB")
        except Exception as e:
            print(e)

    async def disconnect(self):
        try:
            self.access.close()
        except Exception as e:
            print(e)

    def getCollection(self, collection_name: str):
        return self.db[collection_name]

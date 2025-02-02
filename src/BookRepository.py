from bson import ObjectId
from Book import Book
from fastapi import HTTPException
from pymongo.collection import Collection
from Client import Client


class BookRepository:
    collection: Collection

    def __init__(self, client: Client):
        self.collection = client.getCollection("books")

    def addBook(self, book: Book) -> None:
        existing_register = self.collection.find_one(
            {"title": book.title, "author": book.author})

        if existing_register:
            raise HTTPException(
                status_code=400,
                detail="Book already exists from given title and author"
            )

        result = self.collection.insert_one(book.dict())

        if result is None:
            raise HTTPException(
                status_code=400,
                detail="Some error occured while trying to store book"
            )

        return str(result.inserted_id)

    def findBookByTitleAndAuthor(self, title: str, author: str) -> Book:
        result = self.collection.find_one(
            {"title": title, "author": author})

        if result is None:
            raise HTTPException(
                status_code=404,
                detail="There's no book for given title and author"
            )

        if result:
            return self._deserialize_each(result)

        return result

    def findBookById(self, identifier: str) -> Book:
        result = self.collection.find_one(
            {"_id": ObjectId(identifier)})

        if result is None:
            raise HTTPException(
                status_code=404,
                detail="There's no book for given title and author"
            )

        if result:
            return self._deserialize_each(result)

        return None

    def _deserialize_each(self, result):
        return {
            "id": str(result["_id"]),
            "title": str(result["title"]),
            "author": str(result["author"]),
            "year": str(result["year"]),
            "price": str(result["price"]),
        }

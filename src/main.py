from fastapi import FastAPI
from pydantic import BaseModel
import random

app = FastAPI()


class BookDTO(BaseModel):
    title: str
    author: str
    year: str
    price: float


class Book:
    def __init__(self, title: str, author: str, year: str, price: float) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.price = price

    def __str__(self) -> str:
        return f"title: {self.title}, author: {self.author}, year: {self.year}, price: {self.price}"

    def set_id(self, id: int):
        self.id = id


database: Book = []


@app.get("/")
def home():
    return {"Message": "Book api version 1.0"}


@app.get("/books/all")
def getAllBooks():
    return database


@app.get("/book/{book_id}")
def getBookById(book_id: int):
    id = book_id - 1
    book = database[id]
    return book


@app.post("/books/add")
def addBook(dto: BookDTO):
    book: Book = convertToBook(dto)
    id = len(database) + 1
    book.set_id(id)
    database.append(book)
    return {"Message": "Book added to library", "BookId": book.id}


@app.delete("/books/remove/{book_id}")
def removeBook(book_id: int):
    id = book_id - 1
    database.pop(id)
    return {"Message": "Book removed from library"}


def convertToBook(dto: BookDTO) -> Book:
    return Book(dto.title, dto.author, dto.year, dto.price)

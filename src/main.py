from fastapi import FastAPI
from Book import Book, BookDTO
from BookRepository import BookRepository
from Client import Client

app = FastAPI()

client = Client()
repository = BookRepository(client)

# GET Request Method


@app.get("/")
def home():
    return {"Message": "Book api version 1.0"}

# GET Request Method


@app.get("/book/{book_id}")
def getBookById(book_id: str):
    book = repository.findBookById(book_id)
    return {
        "Message": "Book retrivied",
        "content": [
            book
        ]
    }

# GET Request Method


@app.get("/book")
def getBookByTitleAndAuthor(title: str, author: str):
    book: Book = repository.findBookByTitleAndAuthor(title, author)
    return {
        "Message": "Book retrivied",
        "content": [
            book
        ]
    }


# POST Request Method


@app.post("/books/add")
def addBook(dto: BookDTO):
    book: Book = convertToBook(dto)
    result = repository.addBook(book)
    return {"Message": "Book added to library", "BookId": result}


def convertToBook(dto: BookDTO) -> Book:
    return Book(dto.title, dto.author, dto.year, dto.price)

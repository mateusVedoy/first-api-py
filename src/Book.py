from pydantic import BaseModel


class BookDTO(BaseModel):
    title: str
    author: str
    year: str
    price: float


class Book(BaseModel):
    title: str
    author: str
    year: str
    price: float
    id: str

    def __init__(self, title: str, author: str, year: str, price: float, id) -> None:
        self.title = title
        self.author = author
        self.year = year
        self.price = price
        self.id = id

    def __str__(self) -> str:
        return f"title: {self.title}, author: {self.author}, year: {self.year}, price: {self.price}"

    def set_id(self, id: int):
        self.id = id

    def dict(self) -> dict:
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "price": self.price,
        }

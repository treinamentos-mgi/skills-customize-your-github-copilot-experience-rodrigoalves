from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI(title="Books API")


class BookInput(BaseModel):
    title: str = Field(min_length=1)
    author: str = Field(min_length=1)
    year: int = Field(gt=0)


class Book(BookInput):
    id: int


books: dict[int, Book] = {
    1: Book(id=1, title="The Hobbit", author="J. R. R. Tolkien", year=1937),
    2: Book(id=2, title="Frankenstein", author="Mary Shelley", year=1818),
}


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}


# Add the book endpoints described in the assignment below.

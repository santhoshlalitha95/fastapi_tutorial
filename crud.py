from fastapi import FastAPI,status
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

books = [
    {
        "id": 1, 
        "title": "1984",
        "author": "George Orwell",
        "publish_date": "1949-06-08",
    },
    {
        "id": 2,
        "title": "To Kill a Mockingbird", 
        "author": "Harper Lee",
        "publish_date": "1960-07-11",
    },
    {
        "id": 3,
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "publish_date": "1925-04-10",
    },
    {
        "id": 4,
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "publish_date": "1813-01-28",
    }
]

app = FastAPI()

@app.get("/books")
def get_books():
    return books;

@app.get("/books/{book_id}")
def get_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            return book
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")

class Book(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str

@app.post("/books")
def create_book(book: Book):
    new_book = book.model_dump()
    books.append(new_book)
    return new_book

class BookUpdate(BaseModel):
    title: str
    author: str
    publish_date: str

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: BookUpdate):
    for book in books:
        if book["id"] == book_id:
            book["title"] = updated_book.title
            book["author"] = updated_book.author
            book["publish_date"] = updated_book.publish_date
            raise HTTPException(status_code=status.HTTP_200_OK, detail="Book updated successfully") 
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found") 

@app.delete("/books/{book_id}")
def delete_book(book_id: int):
    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            raise HTTPException(status_code=status.HTTP_200_OK, detail="Book deleted successfully")
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Book not found")
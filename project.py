from fastapi import Depends, FastAPI, HTTPException
from database import get_db, engine
from sqlalchemy.orm import Session
import model
from pydantic import BaseModel

app = FastAPI()

class BookStore(BaseModel):
    id: int
    title: str
    author: str
    publish_date: str

@app.post("/books")
def create_book(book: BookStore, db: Session=Depends(get_db)):
    new_book = model.Book(
        id=book.id, 
        title=book.title, 
        author=book.author, 
        publish_date=book.publish_date
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

@app.get("/books")
def get_books(db: Session=Depends(get_db)):
    books = db.query(model.Book).all()
    return books

@app.get("/books/{book_id}")
def get_book(book_id: int, db: Session=Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

class BookStoreUpdate(BaseModel):
    title: str
    author: str
    publish_date: str

@app.put("/books/{book_id}")
def update_book(book_id: int, updated_book: BookStoreUpdate, db: Session=Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    book.title = updated_book.title
    book.author = updated_book.author
    book.publish_date = updated_book.publish_date
    
    db.commit()
    db.refresh(book)
    return book

@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session=Depends(get_db)):
    book = db.query(model.Book).filter(model.Book.id == book_id).first()
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    
    db.delete(book)
    db.commit()
    return {"message": "Book deleted successfully"}
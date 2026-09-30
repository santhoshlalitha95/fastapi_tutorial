from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def read_root():
    return {"Message": "Hello Sam"}

@app.get("/greet")
def greet():
    return {"Message": "Hello, World!"}


@app.get("/greet/{name}")
def greet_name(name: str, age: Optional[int] = None, dob: Optional[str] = None):
    return {"Message": f"Hello, {name}!. You are {age} years old., and your date of birth is {dob}."}



class Student(BaseModel):
    name: str
    age: int
    dob: str

@app.post("/create_student")
def create_student(student: Student):
    return {
        "name": student.name,
        "age": student.age,
        "dob": student.dob
    }
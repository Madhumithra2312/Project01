from fastapi import FastAPI
from pydantic import BaseModel
app =FastAPI()

students = {
    1: {"name": "john",
        "age": 19
       },
    2: {"name": "jessy",
        "age": 20
}
}

class Student(BaseModel):
    name:str
    age: int

@app.get("/")
def func():
    return {'name': 'data'}

@app.get("/student/{id}")
def student(id: int):
    return students[id]



@app.get("/student-by-name")
def stud(name:str=None):
    for i in students:
        if students[i]["name"]==name:
            return students[i]

    return {"file":"not found"}

@app.post("/create/{id}")
def create(id:int,student:Student):
    if id in students:
        return {"error":"id already exists"}
    students[id]= student
    return students[id]
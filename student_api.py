from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    year: str

students = {
    1: {
        "name": "John",
        "age": 17,
        "class": "12"
    }
}

# uvicorn myapi:app --reload
@app.get("/") # just '/' means home page
def index():
    return {"message": "Hello, World!"}

# Get method
# Path parameters
@app.get("/get-students/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):
    return students[student_id]

# path attributes
# gt - greater than
# ge - greater than or equal to
# lt - less than
# le - less than or equal to
# ne - not equal to
# eq - equal to

# Query parameters
@app.get("/get-by-name")
def get_student(name: Optional[str] = None): # Optional is used to make the parameter optional
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data": "Not found"}

# Query + path parameters
@app.get("/get-by-name-id/{student_id}")
def get_student( *, student_id: Optional[int] = None, name: Optional[str] = None): # * is used so that it is okay to add non-optional parameters after optional parameters
    if name:
        if students[student_id]["name"] == name:
            return students[student_id]
        return {"Data": "Not found"}
    return students[student_id]

# Request body and post

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student exists"}
    students[student_id] = student
    return students[student_id]

# Put method
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Student not found"}
    if student.name != None:
        students[student_id].name = student.name
    if student.age != None:
        students[student_id].age = student.age
    if student.year != None:
        students[student_id].year = student.year
    return students[student_id]

# Delete method
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    if student_id not in students:
        return {"Error": "Student not found"}
    del students[student_id]
    return {"message": "Student deleted"}

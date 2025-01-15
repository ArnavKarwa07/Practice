from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.orm import declarative_base

app = FastAPI()

DATABASE_URL = "sqlite:///./employees.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class Employee(Base):
    __tablename__ = "employees"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    age = Column(Integer)
    department = Column(String)

Base.metadata.create_all(bind=engine)

# Dependency for getting the DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.post("/employees/", response_model=dict)
def create_employee(name: str, age: int, department: str, db: Session = Depends(get_db)):
    new_employee = Employee(name=name, age=age, department=department)
    db.add(new_employee)
    db.commit()
    db.refresh(new_employee)
    return {"id": new_employee.id, "name": new_employee.name, "age": new_employee.age, "department": new_employee.department}

@app.get("/employees/{employee_id}", response_model=dict)
def read_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    return {"id": employee.id, "name": employee.name, "age": employee.age, "department": employee.department}

@app.get("/employees/", response_model=list)
def list_employees(db: Session = Depends(get_db)):
    employees = db.query(Employee).all()
    return [{"id": emp.id, "name": emp.name, "age": emp.age, "department": emp.department} for emp in employees]

@app.put("/employees/{employee_id}", response_model=dict)
def update_employee(employee_id: int, name: str, age: int, department: str, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    employee.name = name
    employee.age = age
    employee.department = department
    db.commit()
    db.refresh(employee)
    return {"id": employee.id, "name": employee.name, "age": employee.age, "department": employee.department}

@app.delete("/employees/{employee_id}", response_model=dict)
def delete_employee(employee_id: int, db: Session = Depends(get_db)):
    employee = db.query(Employee).filter(Employee.id == employee_id).first()
    if employee is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(employee)
    db.commit()
    return {"detail": "Employee deleted successfully"}

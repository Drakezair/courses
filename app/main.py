from fastapi import FastAPI, UploadFile, File, Depends
from fastapi.middleware.cors import CORSMiddleware
from db import engine, Base, Session, get_db
from students import router as students
from guardians import router as guardians
from courses import router as courses
from groups import router as groups
from rooms import router as rooms
from teachers import router as teachers
from enrollments import router as enrollments
import pandas as pd
import io
from students.model import Student
from guardians.model import Guardians
from courses.model import Course
from groups.model import Group
from rooms.model import Room
from teachers.model import Teacher
from enrollments.model import Enrollment


app = FastAPI()
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
Base.metadata.create_all(bind=engine)

app.include_router(students.router, prefix="/students", tags=["students"])
app.include_router(guardians.router, prefix="/guardians", tags=["guardians"])
app.include_router(courses.router, prefix="/courses", tags=["courses"])
app.include_router(groups.router, prefix="/groups", tags=["groups"])
app.include_router(rooms.router, prefix="/rooms", tags=["rooms"])
app.include_router(teachers.router, prefix="/teachers", tags=["teachers"])
app.include_router(enrollments.router, prefix="/enrollments", tags=["enrollments"])

# create endpoint to charge a excel file and save guardians to database
@app.post("/uploadfile/{model}")
async def create_upload_file(model ,file: UploadFile = File(...), db: Session = Depends(get_db)):
    df = pd.read_excel(io.BytesIO(file.file.read()))
    df = df.where(pd.notnull(df), None)
    for index, row in df.iterrows():
        if model == "students":
            student = Student(**row.to_dict())
            db.add(student)
            db.commit()
            db.refresh(student)
        elif model == "guardians":
          guardian = Guardians(**row.to_dict())
          db.add(guardian)
          db.commit()
          db.refresh(guardian)
        elif model == "courses":
          course = Course(**row.to_dict())
          db.add(course)
          db.commit()
          db.refresh(course)
        elif model == "groups":
          group = Group(**row.to_dict())
          db.add(group)
          db.commit()
          db.refresh(group)
        elif model == "rooms":
          room = Room(**row.to_dict())
          db.add(room)
          db.commit()
          db.refresh(room)
        elif model == "teachers":
          teacher = Teacher(**row.to_dict())
          db.add(teacher)
          db.commit()
          db.refresh(teacher)
    return {"message": "Guardians added successfully!"}
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse
from . import crud, models, schemas
from .database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def main():
    return {"Api": "World"}


@app.post("/genders/", response_model=schemas.Gender, status_code=status.HTTP_201_CREATED)
def create_gender(gender: schemas.GenderCreate, db: Session = Depends(get_db)):
    return crud.create_gender(db=db, gender=gender)


@app.get("/genders/", response_model=List[schemas.Gender])
def read_genders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    genders = crud.get_genders(db, skip=skip, limit=limit)
    return genders

@app.delete("/genders/{gender_id}", response_model=schemas.Gender, status_code=202)
def delete_gender(gender_id: int, db: Session = Depends(get_db)):
    db_gender = crud.get_gender(db, gender_id=gender_id)
    if db_gender is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return crud.delete_gender(db, gender=db_gender)    

@app.put("/genders/{gender_id}", response_model=schemas.Gender, status_code=202)
def update_gender(gender: schemas.GenderCreate, gender_id: int, db: Session = Depends(get_db)):
    db_gender = crud.get_gender(db, gender_id=gender_id)
    if db_gender is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return crud.update_gender(db, gender=db_gender, update_data=gender.dict())    

@app.get("/genders/{gender_id}", response_model=schemas.Gender)
def read_gender(gender_id: int, db: Session = Depends(get_db)):
    db_gender = crud.get_gender(db, gender_id=gender_id)
    if db_gender is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return db_gender
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


# ------------------------------ Gender --------------------


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


# ------------------------------ Category --------------------


@app.post("/categories/", response_model=schemas.Category, status_code=status.HTTP_201_CREATED)
def create_category(category: schemas.CategoryCreate, db: Session = Depends(get_db)):
    return crud.create_category(db=db, category=category)


@app.get("/categories/", response_model=List[schemas.Gender])
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    genders = crud.get_categories(db, skip=skip, limit=limit)
    return genders

@app.delete("/categories/{category_id}", response_model=schemas.Category, status_code=202)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return crud.delete_category(db, category=db_category)    

@app.put("/categories/{category_id}", response_model=schemas.Category, status_code=202)
def update_category(category: schemas.CategoryCreate, category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return crud.update_category(db, category=db_category, update_data=category.dict())    

@app.get("/categories/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return db_category


# ------------------------------ Director --------------------


@app.post("/directors/", response_model=schemas.Director, status_code=status.HTTP_201_CREATED)
def create_director(director: schemas.DirectorCreate, db: Session = Depends(get_db)):
    return crud.create_director(db=db, director=director)


@app.get("/directors/", response_model=List[schemas.Director])
def read_directors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    directors = crud.get_directors(db, skip=skip, limit=limit)
    return directors

@app.delete("/directors/{category_id}", response_model=schemas.Director, status_code=202)
def delete_director(director_id: int, db: Session = Depends(get_db)):
    db_director = crud.get_director(db, director_id=director_id)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return crud.delete_director(db, director=db_director)    

@app.put("/directors/{director_id}", response_model=schemas.Director, status_code=202)
def update_director(director: schemas.DirectorCreate, director_id: int, db: Session = Depends(get_db)):
    db_director = crud.get_director(db, director_id=director_id)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return crud.update_director(db, director=db_director, update_data=director.dict())    

@app.get("/directors/{director_id}", response_model=schemas.Director)
def read_director(director_id: int, db: Session = Depends(get_db)):
    db_director = crud.get_director(db, director_id=director_id)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return db_director


# ------------------------------ Country --------------------

@app.post("/countries/", response_model=schemas.Country, status_code=status.HTTP_201_CREATED)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_country(db=db, country=country)


@app.get("/countries/", response_model=List[schemas.Gender])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    genders = crud.get_countries(db, skip=skip, limit=limit)
    return genders

@app.delete("/countries/{category_id}", response_model=schemas.Country, status_code=202)
def delete_country(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return crud.delete_country(db, country=db_country)    

@app.put("/countries/{country_id}", response_model=schemas.Country, status_code=202)
def update_country(country: schemas.CountryCreate, country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return crud.update_country(db, country=db_country, update_data=country.dict())    

@app.get("/countries/{country_id}", response_model=schemas.Country)
def read_country(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Gender not found")
    return db_country
from typing import List

from fastapi import Depends, FastAPI, HTTPException, status, Response
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
    expose_headers=["*"]
)

# Dependency
def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
def root_path():
    return {"Api": "U-zave"}


# ------------------------------ Gender --------------------


@app.post("/genders/", response_model=schemas.Gender, status_code=status.HTTP_201_CREATED)
def create_gender(gender: schemas.GenderCreate, db: Session = Depends(get_db)):
    return crud.create_gender(db=db, gender=gender)


@app.get("/genders/", response_model=List[schemas.Gender], response_model_exclude={'collections'})
def read_genders(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), response: Response = Response):
    genders = crud.get_genders(db, skip=skip, limit=limit)
    response.headers["Content-Range"] = str(len(genders))
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


@app.get("/categories/", response_model=List[schemas.Gender], response_model_exclude={'collections'})
def read_categories(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), response: Response = Response):
    genders = crud.get_categories(db, skip=skip, limit=limit)
    response.headers["Content-Range"] = str(len(genders))
    return genders

@app.delete("/categories/{category_id}", response_model=schemas.Category, status_code=202)
def delete_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.delete_category(db, category=db_category)    

@app.put("/categories/{category_id}", response_model=schemas.Category, status_code=202)
def update_category(category: schemas.CategoryCreate, category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return crud.update_category(db, category=db_category, update_data=category.dict())    

@app.get("/categories/{category_id}", response_model=schemas.Category)
def read_category(category_id: int, db: Session = Depends(get_db)):
    db_category = crud.get_category(db, category_id=category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category


# ------------------------------ Director --------------------


@app.post("/directors/", response_model=schemas.Director, status_code=status.HTTP_201_CREATED)
def create_director(director: schemas.DirectorCreate, db: Session = Depends(get_db)):
    return crud.create_director(db=db, director=director)


@app.get("/directors/", response_model=List[schemas.Director], response_model_exclude={'collections'})
def read_directors(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), response: Response = Response):
    directors = crud.get_directors(db, skip=skip, limit=limit)
    response.headers["Content-Range"] = str(len(directors))
    # print (len(directors))
    return directors

@app.delete("/directors/{director_id}", response_model=schemas.Director, status_code=202)
def delete_director(director_id: int, db: Session = Depends(get_db)):
    db_director = crud.get_director(db, director_id=director_id)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return crud.delete_director(db, director=db_director)    

@app.put("/directors/{director_id}", response_model=schemas.Director, status_code=202)
def update_director(director: schemas.DirectorCreate, director_id: int, db: Session = Depends(get_db)):
    db_director = crud.get_director(db, director_id=director_id)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return crud.update_director(db, director=db_director, update_data=director.dict())    

@app.get("/directors/{director_id}", response_model=schemas.Director)
def read_director(director_id: int, db: Session = Depends(get_db)):
    db_director = crud.get_director(db, director_id=director_id)
    if db_director is None:
        raise HTTPException(status_code=404, detail="Director not found")
    return db_director


# ------------------------------ Country --------------------

@app.post("/countries/", response_model=schemas.Country, status_code=status.HTTP_201_CREATED)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    return crud.create_country(db=db, country=country)


@app.get("/countries/", response_model=List[schemas.Country], response_model_exclude={'collections'})
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), response: Response = Response):
    countries = crud.get_countries(db, skip=skip, limit=limit)
    response.headers["Content-Range"] = str(len(countries))
    return countries

@app.delete("/countries/{category_id}", response_model=schemas.Country, status_code=202)
def delete_country(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return crud.delete_country(db, country=db_country)    

@app.put("/countries/{country_id}", response_model=schemas.Country, status_code=202)
def update_country(country: schemas.CountryCreate, country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return crud.update_country(db, country=db_country, update_data=country.dict())    

@app.get("/countries/{country_id}", response_model=schemas.Country)
def read_country(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return db_country


# ------------------------------ Collection --------------------

@app.post("/collections/", response_model=schemas.Collection, status_code=status.HTTP_201_CREATED)
def create_collection(collection: schemas.CollectionCreate, db: Session = Depends(get_db)):
    return crud.create_collection(db=db, collection=collection)


@app.get("/collections/", response_model=List[schemas.Collection])
def read_collections(skip: int = 0, limit: int = 100, db: Session = Depends(get_db), response: Response = Response):
    collections = crud.get_collections(db, skip=skip, limit=limit)
    response.headers["Content-Range"] = str(len(collections))
    return collections

@app.delete("/collections/{collection_id}", response_model=schemas.Collection, status_code=202)
def delete_collection(collection_id: int, db: Session = Depends(get_db)):
    db_collection = crud.get_collection(db, collection_id=collection_id)
    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    return crud.delete_collection(db, collection=db_collection)    

@app.put("/collections/{collection_id}", response_model=schemas.Collection, status_code=202)
def update_collection(collection: schemas.CollectionCreate, collection_id: int, db: Session = Depends(get_db)):
    db_collection = crud.get_collection(db, collection_id=collection_id)
    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    return crud.update_collection(db, collection=db_collection, update_data=collection.dict())    

@app.get("/collections/{collection_id}", response_model=schemas.Collection)
def read_collection(collection_id: int, db: Session = Depends(get_db)):
    db_collection = crud.get_collection(db, collection_id=collection_id)
    if db_collection is None:
        raise HTTPException(status_code=404, detail="Collection not found")
    return db_collection
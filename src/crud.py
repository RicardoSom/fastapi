from sqlalchemy.orm import Session

from . import models, schemas

# ------------------------------ Gender --------------------


def get_gender(db: Session, gender_id: int):
    return db.query(models.Gender).filter(models.Gender.id == gender_id).first()

def get_genders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Gender).offset(skip).limit(limit).all()

def delete_gender(db: Session, gender: schemas.Gender):
    db.delete(gender)
    db.commit()
    return gender

def update_gender(db: Session, gender: schemas.GenderCreate, update_data: dict):
    db.query(models.Gender).filter(models.Gender.id == gender.id).update(update_data)
    db.commit()
    db.refresh(gender)
    return gender

def create_gender(db: Session, gender: schemas.GenderCreate):
    db_gender = models.Gender(title=gender.title, description=gender.description)
    db.add(db_gender)
    db.commit()
    db.refresh(db_gender)
    return db_gender

# ------------------------------ Category --------------------

def get_category(db: Session, category_id: int):
    return db.query(models.Category).filter(models.Category.id == category_id).first()

def get_categories(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Category).offset(skip).limit(limit).all()

def delete_category(db: Session, category: schemas.Category):
    db.delete(category)
    db.commit()
    return category

def update_category(db: Session, category: schemas.Category, update_data: dict):
    db.query(models.Category).filter(models.Category.id == category.id).update(update_data)
    db.commit()
    db.refresh(category)
    return category

def create_category(db: Session, category: schemas.CategoryCreate):
    db_category = models.Category(title=category.title, description=category.description)
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category    


# ------------------------------ Director --------------------

def get_director(db: Session, director_id: int):
    return db.query(models.Director).filter(models.Director.id == director_id).first()

def get_directors(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Director).offset(skip).limit(limit).all()

def delete_director(db: Session, director: schemas.Director):
    db.delete(director)
    db.commit()
    return director

def update_director(db: Session, director: schemas.Director, update_data: dict):
    db.query(models.Director).filter(models.Director.id == director.id).update(update_data)
    db.commit()
    db.refresh(director)
    return director

def create_director(db: Session, director: schemas.DirectorCreate):
    db_director = models.Director(name=director.name, last_name=director.last_name)
    db.add(db_director)
    db.commit()
    db.refresh(db_director)
    return db_director  


# ------------------------------ Country --------------------

def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()

def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()

def delete_country(db: Session, country: schemas.Country):
    db.delete(country)
    db.commit()
    return country

def update_country(db: Session, country: schemas.Country, update_data: dict):
    db.query(models.Country).filter(models.Country.id == country.id).update(update_data)
    db.commit()
    db.refresh(country)
    return country

def create_country(db: Session, country: schemas.CountryCreate):
    db_country = models.Country(name=country.name, code=country.code, capital=country.capital, region=country.region )
    db.add(db_country)
    db.commit()
    db.refresh(db_country)
    return db_country


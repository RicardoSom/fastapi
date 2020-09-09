from sqlalchemy.orm import Session

from . import models, schemas


def get_gender(db: Session, gender_id: int):
    return db.query(models.Gender).filter(models.Gender.id == gender_id).first()

def get_genders(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Gender).offset(skip).limit(limit).all()

def delete_gender(db: Session, gender: schemas.Gender):
    db.delete(gender)
    db.commit()
    return gender

def create_gender(db: Session, gender: schemas.GenderCreate):
    db_gender = models.Gender(title=gender.title, description=gender.description)
    db.add(db_gender)
    db.commit()
    db.refresh(db_gender)
    return db_gender

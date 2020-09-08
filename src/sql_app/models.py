from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.types import Date
from sqlalchemy.orm import relationship

from .database import Base


class Collection(Base):
    __tablename__ = "collection"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    release_year = Column(Date)
    gender_id = Column(Integer, ForeignKey("gender.id"))
    category_id = Column(Integer, ForeignKey("category.id"))
    director_id = Column(Integer, ForeignKey("director.id"))
    country_id = Column(Integer, ForeignKey("country.id"))

    category = relationship("Category", back_populates="collections")
    gender = relationship("Gender", back_populates="collections")
    director = relationship("Director", back_populates="collections")
    country = relationship("Country", back_populates="collections")


class Gender(Base):
    __tablename__ = "gender"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

    collections = relationship("Collection", back_populates="gender")

class Category(Base):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)

    collections = relationship("Collection", back_populates="category")

class Director(Base):
    __tablename__ = "director"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    last_name = Column(String)

    collections = relationship("Collection", back_populates="director")  

class Contry(Base):
    __tablename__ = "director"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    code = Column(String)
    region = Column(String)
    capital = Column(String)

    collections = relationship("Collection", back_populates="country")          
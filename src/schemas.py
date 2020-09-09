from typing import List, Optional
from datetime import date

from pydantic import BaseModel


class CollectionBase(BaseModel):
    title: str
    release_year: date
    

class CollectionCreate(CollectionBase):
    pass


class Collection(CollectionBase):
    id: int
    gender_id : int
    category_id : int
    director_id : int
    country_id : int

    class Config:
        orm_mode = True


class GenderBase(BaseModel):
    title: str
    description: Optional[str] = None


class GenderCreate(GenderBase):
    pass


class Gender(GenderBase):
    id: int
    collections: List[Collection] = []

    class Config:
        orm_mode = True


class CategoryBase(BaseModel):
    title: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    collections: List[Collection] = []

    class Config:
        orm_mode = True  

class DirectorBase(BaseModel):
    name: str
    last_name: str


class DirectorCreate(DirectorBase):
    pass


class Director(DirectorBase):
    id: int
    collections: List[Collection] = []

    class Config:
        orm_mode = True     

class CountryBase(BaseModel):
    name: str
    code: str
    region: str
    capital: str


class CountryCreate(CountryBase):
    pass


class Country(CountryBase):
    id: int
    collections: List[Collection] = []

    class Config:
        orm_mode = True                     
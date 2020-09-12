from typing import List, Optional
from datetime import date

from pydantic import BaseModel


class CollectionBase(BaseModel):
    title: str
    release_year: Optional[date] = None
    gender_id : Optional[int] = None
    category_id : Optional[int] = None
    director_id : Optional[int] = None
    country_id : Optional[int] = None
    gender_desc: Optional[str] = None
    category_desc: Optional[str] = None
    director_desc: Optional[str] = None
    country_desc: Optional[str] = None
    

class CollectionCreate(CollectionBase):
    pass


class Collection(CollectionBase):
    id: int
    
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
from fastapi.testclient import TestClient
from . import schemas
from .main import app
from typing import List

client = TestClient(app)


def test_root_path():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Api": "U-zave"}

def test_read_genders():
    response = client.get("/genders/")
    assert response.status_code == 200

def test_read_categories():
    response = client.get("/categories/")
    assert response.status_code == 200

def test_create_category():
    response = client.post(
        "/categories/",
        json={"title": "Foo", "description": "Fighters"},
    )
    assert response.status_code == 201
    assert response.json() == {
        "title": "Foo",
        "description": "Fighters",
        "id": response.json().get('id'),
        "collections": []
    }


def test_create_director():
    response = client.post(
        "/directors/",
        json={"name": "Joe", "last_name": "Strummer"},
    )
    assert response.status_code == 201
    assert response.json() == {
        "name": "Joe",
        "last_name": "Strummer",
        "id": response.json().get('id'),
        "collections": []
    }


def test_read_directors():
    response = client.get("/directors/")
    assert response.status_code == 200

def test_read_countries():
    response = client.get("/countries/")
    assert response.status_code == 200    

def test_read_collections():
    response = client.get("/collections/")
    assert response.status_code == 200        

def test_read_inexsistent_gender():
    response = client.get("/genders/abc")
    assert response.status_code == 422
    assert response.json() == {'detail': [{'loc': ['path', 'gender_id'], 'msg': 'value is not a valid integer', 'type': 'type_error.integer'}]}

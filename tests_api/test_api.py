import requests
from tests_api import random_select_categorie


def test_get_request():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    assert response.status_code == 200, 'Wrong status code'


def test_get_request_check_value():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    j = response.json()
    assert j["value"] is not None


def test_get_random_categories():
    r = requests.get(f'https://api.chucknorris.io/jokes/random?category={random_select_categorie.random_select_categories()}')
    assert r.status_code == 200, 'Wrong status code'



def test_check_categorie_in_response():
    r = random_select_categorie.random_select_categories()
    response = requests.get(f'https://api.chucknorris.io/jokes/random?category'
                      f'={r}')
    j = response.json()
    assert r in j['categories']


def test_get_categories():
    response = requests.get("https://api.chucknorris.io/jokes/categories")
    assert response.status_code == 200, 'Wrong status code'


def test_number_of_elements_in_categories():
    response = requests.get("https://api.chucknorris.io/jokes/categories")
    res = response.json()
    assert len(res) == 16




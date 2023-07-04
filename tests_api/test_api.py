import requests
import allure
from tests_api import random_select_categorie

@allure.title('Test get request')
def test_get_request():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    assert response.status_code == 200, 'Wrong status code'

@allure.title('Test get request (check value)')
def test_get_request_check_value():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    j = response.json()
    assert j["value"] is not None

@allure.title('Test get random categories')
def test_get_random_categories():
    r = requests.get(f'https://api.chucknorris.io/jokes/random?category={random_select_categorie.random_select_categories()}')
    assert r.status_code == 200, 'Wrong status code'


@allure.title('Test check categories in response')
def test_check_categorie_in_response():
    r = random_select_categorie.random_select_categories()
    response = requests.get(f'https://api.chucknorris.io/jokes/random?category'
                      f'={r}')
    j = response.json()
    assert r in j['categories']

@allure.title('Test get categories')
def test_get_categories():
    response = requests.get("https://api.chucknorris.io/jokes/categories")
    assert response.status_code == 200, 'Wrong status code'

@allure.title('Test number of elements in categories')
def test_number_of_elements_in_categories():
    response = requests.get("https://api.chucknorris.io/jokes/categories")
    res = response.json()
    assert len(res) == 16




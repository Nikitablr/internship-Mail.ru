import requests
import random


def test_get_request():
    response = requests.get("https://api.chucknorris.io/jokes/random")
    assert response.status_code == 200, 'Wrong status code'
    print(response.text)


def test_get_random_categories():
    categories = ["animal","career","celebrity","dev","explicit","fashion","food","history","money","movie","music",
                  "political","religion","science","sport","travel"]
    random_categories = random.choice(categories)
    response = requests.get(f"https://api.chucknorris.io/jokes/random?category={random_categories}")
    print(response.json())
    assert response.status_code == 200, 'Wrong status code'


def test_get_categories():
    response = requests.get("https://api.chucknorris.io/jokes/categories")
    print(response.json())
    assert response.status_code == 200, 'Wrong status code'



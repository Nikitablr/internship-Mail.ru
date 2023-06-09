import random
import requests


def random_select_categories():
    categories = ["animal", "career", "celebrity", "dev", "explicit", "fashion", "food", "history", "money", "movie",
                  "music",
                  "political", "religion", "science", "sport", "travel"]
    random_categories = random.choice(categories)
    return random_categories

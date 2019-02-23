from secrets import PETFINDER_API_KEY
import requests

BASE_URL = "http://api.petfinder.com"


def get_random_pet():
    """ make the GET API call to get a random pet,
    basic info in json format
    we return the name, age, and phot_url of the pet to display on homepage"""

    response = requests.get(f"{BASE_URL}/pet.getRandom",
                            params={"key": PETFINDER_API_KEY,
                                    "output": "basic",
                                    "format": "json"})
    response_data = response.json()

    pet_profile = response_data['petfinder']['pet']

    pet_data = {"name": pet_profile['name']['$t'],
                "age": pet_profile['age']['$t'],
                "photo_url": pet_profile['media']['photos']['photo'][3]['$t']}

    return pet_data



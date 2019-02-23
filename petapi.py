from secrets import PETFINDER_API_KEY
import requests

BASE_URL = "http://api.petfinder.com"


def get_random_pet():
""" make the GET API call to get a random pet,
basic info in json format
we return the name, age, and phot_url of the pet to display on homepage"""

    response = requests.get(f"{BASE_URL}/pet.getRandom", 
                       params={ "key": PETFINDER_API_KEY, 
                                "output" : "basic",
                                "format" : "json"})
    pet_data = response.json()
    pet_name = pet_data['petfinder']['pet']['name']['$t']
    pet_age = pet_data['petfinder']['pet']['age']['$t']
    pet_photo_url = pet_data['petfinder']['pet']['media']['photos']['photo'][3]['$t']

   
    return pet_phot_url



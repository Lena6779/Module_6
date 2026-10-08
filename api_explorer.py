"""
Fetch data from the PokéAPI (https://pokeapi.co/api/v2/) using requests.

Prints the name, height, weight, and types of several Pokemon, and handles
a misspelled name by checking for a 404 status code!

To run please follow these steps below: 

Install the dependency first:
    pip install requests

Run:
    python api_explorer.py
"""

import requests

def get_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 404: # 404: Requested Pokemon does not exist
        print(f"Error: '{name}' was not found. Please check the spelling and try again.")
        return
    data = response.json()

    types = []
    for t in data["types"]:
        types.append(t["type"]["name"])
    
    print(f"Name:   {data['name']}")
    print(f"Height: {data['height'] / 10} m") # API gives decimetres so conversion /10 is needed for m 
    print(f"Weight: {data['weight'] / 10} kg") # API gives hectograms so conversion / 10 is needed for kg
    print(f"Types:  {', '.join(types)}")
    print()


for pokemon_name in ["pikachu", "charizard", "bulbasaur", "pikacu"]: # pikacu is a misspelling to demonstrate the error handling 
    get_pokemon(pokemon_name)
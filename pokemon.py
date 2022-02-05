import random
from queue import LifoQueue

from bs4 import BeautifulSoup

from req import *


API_POKEMON = "https://pokeapi.co/api/v2/"


class Pokemon:
    def __init__(self, species, type, abilities = [], level=None):
        self.type = type
        self.species = species
        self.abilities = abilities
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)
            
        self.health = self.level*10
        self.power = self.level*5
            
    def __str__(self):
        return "{} - Level: {}".format(self.species, self.level)
    
    def attack(self, pokemon):
        effective_attack = int((self.power * random.random() *1.3))
        pokemon.health -= effective_attack
        
        print("{} used {}".format(self, random.choice(self.abilities)))
        print("{} lost {} life points - New Health: {}\n".format(pokemon, effective_attack, pokemon.health))
        
        if pokemon.health <= 0:
            print("\n{} is dead \n".format(pokemon))
            return True
        else:
            return False
        
def search_pokemon(pokemon):
    try:
        request_pokemon = request(API_POKEMON + 'pokemon/' + pokemon)
        json_pokemon = parsing(request_pokemon)
        return json_pokemon
    except:
        print("This Pokemon doesn't exist")

def create_pokemon(pokemon_name):
    json_pokemon = search_pokemon(pokemon_name)
    specie = json_pokemon['species']['name']
    type = json_pokemon['types'][0]['type']['name']
    abilities = json_pokemon['abilities']
    abilities_list = []
    
    for abilitie in abilities:
        abilities_list.append(abilitie['ability']['name'])
        
    return specie, type, abilities_list



def get_random_pokemon():
    POKEMON_API_NAMES = request('https://pokeapi.co/api/v2/pokemon?limit=400&offset=500')
    POKEMON_API_NAMES = parsing(POKEMON_API_NAMES)

    LIST_POKEMON = []

    for pokemon in POKEMON_API_NAMES['results']:    
        LIST_POKEMON.append(pokemon['name'])
        
    return random.choice(LIST_POKEMON)
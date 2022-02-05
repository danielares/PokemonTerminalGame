import random
import json

from pokemon import *
from req import *

class People:
    def __init__(self, name=None, pokemons=[], money=100, pokeball=1):
        if  name:
            self.name = name
        else:
            self.name = get_random_name()
        self.pokemons = pokemons
        self.money = money
        self.pokeball = pokeball
        
    def __str__(self):
        return self.name
    
    def show_pokemons(self):
        if self.pokemons:
            print("Pokemons of {}: ".format(self))
            for index, pokemon in enumerate(self.pokemons):
                if pokemon.health <= 0:
                    print("{} - {} Health: {} (DEAD) ".format(index, pokemon, pokemon.health))
                elif pokemon.health > 0:
                    print("{} - {} Health: {}".format(index, pokemon, pokemon.health))
        else:
            print("{} don't have pokemons".format(self))
         
    def random_pokemon(self):
        choice_pokemon = random.choice(self.pokemons)
        return choice_pokemon
    
    def choose_pokemon(self, message):
        self.show_pokemons()
        while True:
            choice = input("Choose a pokemon {}: ".format(message))
            try:
                choice = int(choice)
                choice_pokemon = self.pokemons[choice]
                return choice_pokemon
            except:
                print("This pokemon doesn't exist")
        
        
    def battle(self, person):
        print("\nA battle has begun!!! {} VERSUS {} \n".format(self, person))
        
        person.show_pokemons()
        
        enemy_pokemon = person.random_pokemon()
        print("{} choose {} !!!\n".format(person, enemy_pokemon))
        
        while True:
            choosen_pokemon = self.choose_pokemon("to fight")
            if choosen_pokemon.health < 0:
                print("\nThis pokemons is dead! you need to choice another pokemon or visit shopping and heal your pokemon\n")

            elif choosen_pokemon.health > 0:
                print("\n{} choose {} !!!\n".format(self, choosen_pokemon))
                break
        
        if enemy_pokemon and choosen_pokemon:
            while True:
                win = choosen_pokemon.attack(enemy_pokemon)
                if win:
                    print("{} win the battle".format(self))
                    self.money += enemy_pokemon.level * 10
                    print("You won {} coins!".format(enemy_pokemon.level * 10))
                    print("Now you have {} coins".format(self.money))
                    break
                enemy_win = enemy_pokemon.attack(choosen_pokemon)
                if enemy_win:
                    print("{} win the battle".format(person))
                    break
        else:
            print("There was an error when choosing pokemon.")
          
            
class Player(People):
    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print("\n{} catch {}".format(self, pokemon))
    
    def explore(self):
        if random.random() <= 0.9:
            pokemon_random = create_pokemon(get_random_pokemon())
            pokemon_random = Pokemon(pokemon_random[0],pokemon_random[1],pokemon_random[2],random.randint(1, 100))
            print("\nA wild Pokemon appeared: {}".format(pokemon_random))
            escolha = input("Ddo you wanna catch this pokemon? (s/n): ")
            if self.pokeball:
                if escolha == "s":
                    self.pokeball -= 1
                    if random.random() <= 0.9:
                        self.capturar(pokemon_random)
                    else:
                        print("\n{} ran away".format(pokemon_random))
                elif escolha == "n":
                    print("OK! Have a nice trip")
                else:
                    print("Invalid choice")
            else:
                print("You don't have pokeballs. Visit the shop and buy some")
        else:
            print("Nothing...")    

class Enemy(People):
    def create_enemy(self, name=None, power=100):
        number_of_pokemons = random.randint(1, 5)
        list_pokemons = []
        for pokemon in range(number_of_pokemons):
            pokemon = create_pokemon(get_random_pokemon())
            list_pokemons.append(Pokemon(pokemon[0],pokemon[1],pokemon[2],random.randint(1,power)))
        if not name:
            enemy = Enemy(get_random_name(), list_pokemons)
        else:
            enemy = Enemy(name, list_pokemons)
        return enemy
            
def get_random_name():
    answer = requests.get('https://api.namefake.com')
    if answer.status_code == 200:
        json_answer = json.loads(answer.text)
        name = json_answer['name']
        return name
        
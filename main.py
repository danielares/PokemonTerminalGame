import pickle

from pokemon import *
from people import *
from req import *
from shop import *

def load_game():
    try:
        with open("database.db", "rb") as arquivo:
            player = pickle.load(arquivo)
            print("Loading done!")
            return player
    except Exception as error:
        print("Your saves can't be found")
        
def save_game(player):
    try:
        with open("database.db", "wb") as arquivo:
            pickle.dump(player, arquivo)
            print("The game has been saved!")
    except Exception as error:
        print("Unable to save game")
        print(error)

def escolher_pokemon_inicial(player):
    print("Hello {}, you can now choose the pokemon that will accompany you on this journey!".format(player))

    pikachu = create_pokemon("pikachu")
    pikachu = Pokemon(pikachu[0],pikachu[1],pikachu[2],1)

    charmander = create_pokemon("charmander")
    charmander = Pokemon(charmander[0],charmander[1],charmander[2],1)
    
    squirtle = create_pokemon("squirtle")
    squirtle = Pokemon(squirtle[0],squirtle[1],squirtle[2],1)

    print("You have 3 choices")
    print("1 - ",pikachu)
    print("2 - ",charmander)
    print("3 - ", squirtle)

    while True:
        option = input("Choose your pokemon: ")

        if option =="1":
            player.capturar(pikachu)
            break
        elif option =="2":
            player.capturar(charmander)
            break
        elif option == "3":
            player.capturar(squirtle)
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    print("\n---------------------------------------------")
    print("WELCOME TO TERMINAL POKEMON GAME!")
    print("---------------------------------------------\n")
    
    player = load_game()
    
    if not player: 
        name = input("Hello!! What's your name: ")
        player = Player(name)
        print("Hello {} this is a world inhabited by pokemons, from now on your mission is to become a pokemon master".format(player))
        
        if player.pokemons:
            print("You already have some pokemons")
            player.show_pokemons()
        else:
            print("You don't have a pokemon.... You need to choose one")
            escolher_pokemon_inicial(player)
            
        
        print("Now that you already have a pokemon fight an enemy")
        
        garry = Enemy().create_enemy(name = "Garry", power =1)
        player.battle(garry)
        save_game(player)
        

    while True:
        print("\n---------------------------------------------")
        print("OPTIONS")
        print("1 - Explore the world")
        print("2 - Fight an enemy")
        print("3 - PokeDex")
        print("4 - Shopping")
        print("5 - My items")
        print("0 - Exit game")
        option = input("\noption: ")
        
        if option == "0":
            print("Exiting the game...")
            break
        elif option == "1":
            player.explore()
            save_game(player)
        elif option == "2":
            enemy = Enemy().create_enemy()
            player.battle(enemy)
            save_game(player)
        elif option == "3":
            player.show_pokemons()
        elif option == "4":
            show_menu_shopping(player)
            save_game(player)
        elif option == "5":
            print("You have: {} coins".format(player.money))
            print("You have {} pokeballs".format(player.pokeball))
        else:
            print("Invalid choice")
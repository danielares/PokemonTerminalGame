from people import *

class Item():
    def __init__(self, name, price):
        self.name = name
        self.price = price
        
    def __str__(self):
        return self.name
       
def show_menu_shopping(player):
    while True:
        print("\n---------------------------------------------")
        print("OPTIONS:")
        print("1 - Heal a pokemon (1000 coins)")
        print("2 - Level Up a Pokemon (10.000 coins)")
        print("3 - 10 Poké Balls (150 coins)")   
        print("0 - Exit shop") 
        escolha = input("\noption: ")
        
        if escolha == "0":
            print("Thank you, come again, {}".format(player))
            break
        elif escolha == "1":
            if not player.money < heal.price:
                player.money -= heal.price
                choice = player.choose_pokemon("to heal")
                choice.health = choice.level * 10
                print("\n{} was healed to its maximum life ({} Points of health)".format(choice, choice.health))
            else:
                print("You don't have money!")
                
        elif escolha == "2":
            if not player.money < heal.price:
                player.money -= heal.price
                choice = player.choose_pokemon("to level up")
                choice.level += 1
                choice.health  += 10
                print("\n{} was uped".format(choice))
            else:
                print("You don't have money!")
                
        elif escolha == "3":
            if not player.money < poke_ball.price:
                player.money -= poke_ball.price
                player.pokeball += 10
                print("Now you have {} Poké Balls".format(player.pokeball))
            else:
                print("You don't have money")
    
        else:
            print("Invalid choice")
    
heal = Item("Heal pokemon", 1)
level_up = Item("Level up a Pokemon", 1)
poke_ball = Item("10 Poké Balls", 100)
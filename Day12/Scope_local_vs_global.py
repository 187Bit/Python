# Image a house with a fence around it. If you plant a tree inside the fence the only people who can access the tree is your family. But if you plant a tree outside the fence anyone can access the tree

################### Scope ####################

enemies = 1

def increase_enemies():
  enemies = 2
  print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local scope:

def drink_potion():
    potion_strentgh = 2 # Local scope (local variable): only valid inside the function
    print(potion_strentgh)

drink_potion()
# print(potion_strength) # Will give you a name error, because it is not defined globally -> it is a local scope inside the function

# Global scope: (only difference is where the variable is defined)
player_health = 100 # Global scope (global variable): available anywhere in your file (outside of any function) (but only for print-statements)

def drink_potion():
    potion_strentgh = 2 
    print(potion_strentgh)
    print(player_health)

drink_potion()

def game():
  def potion():
    potion_strentgh = 2 
    print(potion_strentgh)
    print(player_health)

# potion() # You can not call the function potion() because it is nested inside another function (the function call can not "see" the function)

#There is no block scope in python:
game_level = 3
enemies = ["Skeleton", "Zombie", ["Alien"]]
if game_level < 5:
  new_enemy = enemies[0] 
print(new_enemy) # You can still access new_enemy although it is indented inside an if-statement (block)
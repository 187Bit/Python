# To modify a global variable you have to explicitly tell the function that you want to modify this global variable
enemies = 1

def increase_enemies():
    global enemies # This tells the function that you want to modify the global variable "enemies"
    # !It is better not to modify a variable with global scope inside a function. Prone to errors and problems!
    # Better alternative is to return the value 
    return enemies + 1
  
    print(f"enemies inside function: {enemies}")

new_enemies = increase_enemies()
print(f"enemies outside function: {new_enemies}")
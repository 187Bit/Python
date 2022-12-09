from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

### ADD COMMENTS TO THE CODE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!####

def coffee_machine(): # Defines the coffee_machine function
    """Models the functions of a cofffee machine. A virtual coffee machine. """

    # You cannot print methods, only attributes

    coffee = True
    coffee_machine = CoffeeMaker() # creates coffee machine object from the CoffeeMaker() class
    money_machine = MoneyMachine() # creates money_machine object from the MoneyMachine() class
    menu = Menu() # Creates the menu object from the Menu() class
    
    while coffee: # while loop as long as coffee is True
    
        coffee_type = input("What would you like? (Espresso/Latte/Cappuccino):\n").lower() # Aks the user for the type of coffee and stores it in the variable coffee_type

        if coffee_type == "report": # checks if the string stored in coffee_type is equal to "report"

            coffee_machine.report() # Prints a report of the resources of the coffee_machine by using the coffee_machine object and the .report() method
            money_machine.report() # Prints a report of the money of the money_machine by using the coffee_machine object and the .report() method

        elif coffee_type == "off": # Checks if the string in coffee_type is equal to "off", if coffee_type is not "report" (elif)
            print("Machine has been turned off!")
            coffee = False
        else: # If coffee_type is not "report" or "off"
            
            ordered_coffee = menu.find_drink(coffee_type) # Returns an object with attributes (name, water, milk, coffee, cost), uses the menu object and the find_drink() method with the argument coffee_type to find the selected drink and returns it as an object with attributes and stores it in the varaible ordered_coffee

            if ordered_coffee != False: # Checks if ordered_coffee is not False
                
                sufficient_resources = coffee_machine.is_resource_sufficient(ordered_coffee) # uses the coffee_machine object and the is_resource_sufficient() method with the argument ordered_coffee to check if the resources in the machine are sufficient to make the coffee and the returns True or False and stores it in the variable sufficient_resouces
                
                if sufficient_resources == True: # Checks if sufficient_resources is True
                    print(f"The {ordered_coffee.name} will be $ {ordered_coffee.cost} please. You can insert your coins now!")
                    enough_money = money_machine.make_payment(ordered_coffee.cost) # uses the money_machine object and the make_payment() method with the argument (ordered_coffee.cost) to check if the user has enough money to pay for the coffee and calculates the change if necessary, returns True of False which will be stored in the variable enough_money 
                    if enough_money == True: # Checks if the boolean in enough_money is True
                        coffee_machine.make_coffee(ordered_coffee) # uses the coffee_machine object and the make_coffee() method with the argument ordered_coffee to make the coffee and subtract the used resources and add the earned money
                    else:
                        coffee = False
                else: 
                    print("Sorry, not enough resources to make the drink!")
            else:
                coffee = False
            

coffee_machine() # Calls the coffee_machine function
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def coffee_machine(resources):

    coffee = True

    while coffee:
    
        coffee_type = input("What would you like? (Espresso/Latte/Cappuccino):\n").lower()

        if coffee_type == "report":
            print(resources)
        elif coffee_type == "off":
            print("Machine has been turned off!")
            coffee = False
        else:
            coffee_name = coffee_type
            coffee_type = assign_coffee(coffee_type, MENU)
            if coffee_type == "NONE":
                print("This drink does not exist.")
                coffee = False
            else:

                price = MENU[coffee_name]["cost"]
                required_water = coffee_type["ingredients"]["water"]
                required_coffee = coffee_type["ingredients"]["coffee"]
                required_milk = coffee_type["ingredients"]["milk"]
                sufficient = check_resources(resources, required_water, required_coffee, required_milk)

                if sufficient == True:
                    returned = payment(price)
                elif sufficient == "No water":
                    print("Sorry, there is not enough water in the tank.")
                    coffee = False
                elif sufficient == "No coffee":
                    print("Sorry, there is not enough coffee in the tank.")
                    coffee = False
                elif sufficient == "No milk":
                    print("Sorry there is not enough milk in the tank.")
                    coffee = False

                if returned == False:
                    coffee = False
                else: 
                    resources["money"] = returned
                    resources = make_coffee(coffee_name, resources, required_water, required_coffee, required_milk)
                

def assign_coffee(coffee_type, MENU):

    if coffee_type == "espresso":
        coffee_type = MENU["espresso"]
    elif coffee_type == "latte":
        coffee_type = MENU["latte"]
    elif coffee_type == "cappuccino":
        coffee_type = MENU["cappuccino"]
    else: 
        coffee_type = "NONE"

    return coffee_type

def check_resources(resources, required_water, required_coffee, required_milk):
    
    if resources["water"] > required_water:

        if resources["coffee"] > required_coffee:

            if resources["milk"] > required_milk:
                return True
            else:
                return "No milk"
        else: 
            return "No coffee"
    else:
        return "No water"

def payment(price):

    total_money = 0 

    print(f"This will be {price} cents please! You can insert you coins now!")
    amount_of_quarters = int(input("Amount of quarters (0,25):\n"))
    amount_of_dimes = int(input("Amount of dimes(0.10):\n"))
    amount_of_nickels = int(input("Amount of nickels(0.05):\n"))
    amount_of_pennis =int(input("Amount of pennies(0.01):\n"))

    total_money = amount_of_quarters * 0.25 + amount_of_dimes * 0.10 + amount_of_nickels * 0.05 + amount_of_pennis * 0.01

    if total_money >= price:
        change = round(total_money - price, 2)
        print(f"You have inserted {total_money}. You get {change} back.")
        total_money = total_money - change
        return total_money
    else:
        print("Sorry that is not enough money. The inserted coins have been refunded.")
        return False

def make_coffee(coffee_name, resources, required_water, required_coffee, required_milk):

        resources["water"] -= required_water
        resources["milk"] -= required_milk
        resources["coffee"] -= required_coffee
        print(f"Here is your {coffee_name}. Enjoy!")

        return resources
    

coffee_machine(resources)
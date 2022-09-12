# If you a for example modelling a waiter you need to think about what he has and what he does
# A waiter might have a plate: is_holding_plate = True and he might be responsible for certain tables: tables_responsible = [4,5,6]
# A waiter should be able to take orders: def take_order(table, order): and take payments: def take_payment(amount):
# In oop the things something has are called "attributes" (variable) and the actions it can perform are called "methods" (function)
# Called attribute although it is just a variable, because it is assigned to a specific "module" or person in that example
# Called methods although they are clearly functions because you again need a specific module or person to perform that action, a cleaner will not take orders
# You can generate multiple "instances" of a waiter for example from the blueprint "waiter"
# The blueprint is called a "class" and the "instances" created from it are called "objects" 
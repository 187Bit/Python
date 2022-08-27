# Nesting lists and dictionaries

# Instead of using a value as the value for the key, you can use a list or a dictionary as a value
# Example:
# dictionary_name = {
# Key_1: [List_name],
# Key_2: [Dictionary_name],
# }

capitals = {

    "France": "Paris",
    "Germany": "Berlin"
}

# Nesting a List inside a dictionary

travel_log = {

    "France": ["Paris","Lille","Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nest a dictionary in a dictionary:


travel_log_extended = { # Dictionary_1
    # Dictionary      Key           Values in form of list   Key_2         Value_2
    "France": {"cities_visited": ["Paris","Lille","Dijon"], "total_visits": 12}, # Dictionary_2
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 5}
}

print(travel_log_extended)

# Nesting a dictionary inside a list:

travel_log_list = [ # List with two items that are dictionaries
{
    "country": "France", # Key-Value-Pair
    "cities_visited": ["Paris","Lille","Dijon"],
    "total_visits": 12
},

{
    "country": "Germany",
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
},
]
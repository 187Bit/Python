travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country_name, number_of_visits, cities_visited): # Defines a new function called add_new_country with the parameters: country_name, number_of_visits, cities_visited
    
    travel_log.append({"country": country_name, "visits": number_of_visits, "cities": cities_visited}) # Extends the list with a new dictionary while using the data provided by the parameters

    # Step by step code
    # new_country = {}
    # new_country["country"] = country_name
    # new_country["number_of_visits"] = number_of_visits
    # new_country["cities_visited"] = cities_visited
    
#🚨 Do not change the code below
add_new_country(country_name = "Russia", number_of_visits = 2, cities_visited = ["Moscow", "Saint Petersburg"])
print(travel_log)
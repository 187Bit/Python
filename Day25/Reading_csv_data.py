# import csv

# # CSV stands for Comma Separated Values

# with open("Day25/weather_data.csv") as file:

#     data = csv.reader(file) # returns a csv object that can be looped, multiple list (rows)
#     temperatures = []

#     # for row in data:
#     #     print(row)

#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

#     print(temperatures)

# The way of working with data above is really frustrating so you would instead use the pandas library

import pandas

data = pandas.read_csv("Day25/weather_data.csv") # reads the csv file as save it into the variable data
print(data["temp"]) # prints out every temperature in the temperature row
print(data)
import pandas

data = pandas.read_csv("Day25/weather_data.csv")
# print(data)

# Pandas uses two object types: Series and DataFrame
# DataFrame is basically the table in excel
# Series is basically a list, so in that example "temperature" would be a series

# data_dict = data.to_dict() # converst the "data" Dataframe into a dictionary where each key is the heading of each column
# print(data_dict)

# temp_list = data["temp"].tolist() # convertes the Series data["temp"] to a list
# print(temp_list)


# for temp in temp_list:

#     # With sum function:

#     temperature_value = sum(temp_list)
#     amount_of_temps = len(temp_list)
#     average_temperature = temperature_value / amount_of_temps

#     # Better way -> with pandas:

#     average_temperature = data["temp"].mean() # gets the mean of the Series data["temp"] and saves it to the variable average_temperature

# print(round(average_temperature,1))

# # Maximum value of a Series: 

# max_temp = data["temp"].max()
# print(max_temp)

# # Instead of writing data["temp"] you can simply use data.columnname because pandas has already created an attribute for this

# # Get data in columns:

# print(data.condition)

# # Get data in rows:

# data[data.day == "Monday"] # looks through the rows in the column "day" and checks where it is equal to "Monday"

# Row with the highest temperature in the week:

# print(data[data.temp == data.temp.max()]) # look through the rows in the column "temp" and checks where it is equal to the highest temperature in the whole DataFrame
# # Basically you are taking the whole DataFrame and then you access the column "temp" and add a condition where the temperature in that row is equal to the highest temperature -> you strip it down

# monday = data[data.day == "Monday"] # takes the whole DataFrame and then gets the column day and checks where it is equal to "Monday" and then saves it to monday
# print(monday.condition) # with monday you then can access the columns

# temp_in_celsius = int(monday.temp)
# temp_in_fahrenheit = temp_in_celsius * 1.8 + 32
# print(temp_in_fahrenheit)

# Creating a DataFrame from scratch: 
data_dict = {

    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65],
}

# print(data_dict["students"][1]) quick reminder on how to print out values inside dictionaries
# print(data_dict["scores"][1]) quick reminder on how to print out values inside dictionaries

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("Day25/new_data.csv") # saves the DataFrame as a csv file in a given PATH
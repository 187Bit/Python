import pandas

data = pandas.read_csv("Day25/2018_Central_Park_Squirrel_Data.csv") # reads the csv file and save it to the DataFrame "data"
colors = ["Gray","Cinnamon","Black"] # list of all three primary fur colors that the squirrles can have
amounts = [] # empty list for the amounts

for color in colors: # loops through each color in the list

    color = data[data.Primary_Fur_Color == f"{color}"].count() # selects the DataFrame "data" and then the column "Primary_Fur_Color" and goes trough each row and checks if the value in that row is equal to "Black", counts the values in that row
    amounts.append(color.Primary_Fur_Color) # appends the amount of the same "Primary_Fur_Color" to the list amounts

# Alternative with len() function:

# gray_squirrels_amount = len(data[data.Primary_Fur_Color == "Gray"])

# Create a new dictionary:

fur_color_count = { # creates a new dictionary called "fur_color_count"

    "Fur Color": colors, # creates a new key called "Fur Color" and adds the value in the list "colors" to it
    "Count": amounts # creates a new key called "Count" and adds the values in the list "amounts" to it
}

Squirrel_data_frame = pandas.DataFrame(fur_color_count) # creates a new DataFrame from the dictionary "fur_color_count" and save it to the "Squirrel_data_frame"
Squirrel_data_frame.to_csv("Day25/squirell_color_data.csv") # save the "Squirrel_data_frame" as a .csv file to "Day25/squirell_color_data.csv"

# If you have a column header that has space you can use the data["string"] notation rather than data.xyz notation
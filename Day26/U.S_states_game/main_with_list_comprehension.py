import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(width= 725, height= 491)
image = "Day25/U.S_states_game/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

amount_of_right_guesses = 0
correct_guesses = []

# Gets the x and y values of the states

# def get_mouse_click_coor(x,y):
#     print(x,y)

# turtle.onscreenclick(get_mouse_click_coor)

# turtle.mainloop()

data = pandas.read_csv("Day25/U.S_states_game/50_states.csv")
all_states = data.state.to_list()

while amount_of_right_guesses < len(all_states):

    user_input = screen.textinput(title= f"{amount_of_right_guesses}/50 Guess the state", prompt= "What is another's states name?").title() # opens a 
    row = data[data.state == user_input]

    if user_input not in correct_guesses:

        if user_input == "Exit":
            break

        if user_input in all_states:

            row = data[data.state == user_input]
            x_pos = int(row.x)
            y_pos = int(row.y)

            writer.setposition(x_pos,y_pos)
            writer.write(user_input, align = "center", font= ("Calibri", 10, "normal"))
            # or writer.write(row.state.item())
            amount_of_right_guesses += 1
            correct_guesses.append(user_input)

# with list comprehension: 

states_to_learn = [state for state in all_states if state not  in correct_guesses]

states_dataframe = pandas.DataFrame(states_to_learn)
states_dataframe.to_csv("Day26/U.S_states_game/states_to_learn.csv")


# def turn_right():
    
#     turn_left()
#     turn_left()
#     turn_left()

# def go_around():
    
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
   
# def jump():
    
#     move()
#     turn_left()
#     move()
#     turn_right()
#     move()
#     turn_right()
#     move()
#     turn_left()
    
   
# while not at_goal():

#     if front_is_clear() == True:
#         move()
#     elif wall_in_front() == True:
#         go_around()

# or:

# while not at_goal():

#     if wall_in_front() == True:
#         go_around()
#     else:
#         move()
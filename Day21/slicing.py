# Example: List of piano keys = ["a", "b", "c", "d", "e", "f", "g"]
# Want to get hold of a part of the whole list "piano keys" -> c to e

# Do do this you can do:
# piano_keys[2:5] # slices the list from position 2 to the position 5 
# Slices work in between of the numbers, so "c" is 2 but the slice stops at "e" although it is written as [2:5]

# You can also slice the list without and ending -> to get all value excluding the ones before the first slice
# Works in the opposite direction as well

# You can also set an increment for how often do you want slice, so the step size

# If you want to go from the beginning to the end in increments of 2 you can write:
# piano_keys[::2]

# Additionally you can also reverse the list by writing -1 as the increment
# piano_key[::-1]

# Method of slicing is also working for slices
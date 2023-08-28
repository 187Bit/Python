# Documentation for our code
# Docstrings are the explanations of what the function does (shows up if you hover over it)

# Example:

def format_name(first_name, last_name):
    """Take a first and a last name and format it to return the title case version of the name. """
    
    formatted_name = first_name.title() + " " + last_name.title() # Concatenates the two variables and stores it in the variable formatted_name, also make it title case

    return formatted_name # returns the variable formatted_name

print(format_name("joel", "bauer"))
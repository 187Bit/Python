

def format_name(first_name, last_name):

    if first_name == "" or last_name == "":
        return "You did not provide valid inputs." # You can have multiple returns in one function, but remember that everything that comes after the the executed return will not be executed

    formatted_name = first_name.title() + " " + last_name.title() # Concatenates the two variables and stores it in the variable formatted_name, also make it title case

    return formatted_name # returns the variable formatted_name
    # Everything that comes after the return key will not be executed

print(format_name(input("What is your first name?\n"), input("What is your last name?\n")))
# To create a class you simply type:
# class class_name:
#   everything else goes here (indented)

class User:
    pass 

user_1 = User()

# Adding an attribute to your object: (the longer way)

user_1.id = "001"
user_1.username = "Joel"

print(user_1.id)


# Constructor: Part of the blueprint that allow us to specify when our object in being constructed (also known as "initialise")

# To create a constructor you use a special function: init function

# Structure:
# def __init__(self):
#   initialise attributes

class User_new:

    def __init__(self, user_id, username) -> None: # To add attributes to an object you can add parameters to your _init__ function
        print("New user has been created!")
        self.id = user_id # Adds the attribute id to the User class and assign the value of the parameter user_id to it
        self.username = username
        self.followers = 0 # Sometimes it makes sense to not provide a value and rather set a default value for an attribute. You can do this by providing a value after the equal sign instead of the parameter


user_new_1 = User_new("001", "Joel") # Creates a new user called user_new_1 from the class "User" and initialises it with the attributes user_id ("001") and the username ("Joel")
user_new_2 = User_new("002", "Ole")

print(user_new_1.id)
print(user_new_1.username)
print(user_new_1.followers)
print(user_new_2.id)
print(user_new_2.username)

# Adding methods to your class:

class User_with_method:

    def __init__(self, user_id, username) -> None: # To add attributes to an object you can add parameters to your _init__ function
        print("New user has been created!")
        self.id = user_id # Adds the attribute id to the User class and assign the value of the parameter user_id to it
        self.username = username
        self.followers = 0 # Sometimes it makes sense to not provide a value and rather set a default value for an attribute. You can do this by providing a value after the equal sign instead of the parameter
        self.following = 0

    def follow(self, user): # Defines the method follow(self, user) with the parameters self (object), user 
        user.followers += 1 # Adds one to the attribute followers of the provided user
        self.following += 1 # Adds one to the attribute following to yourself


new_user_1 = User_with_method("003", "Joel")
new_user_2 = User_with_method("004", "Ole")

new_user_1.follow(new_user_2)
print(f"User 2 has {new_user_2.followers} followers.")
print(f"User 1 follows {new_user_1.following} account.")
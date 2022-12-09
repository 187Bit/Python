# Class inheritance: Means that classes can "inherit" methods of other classes
# Example: Restaurant with a chef (class), want a new chef with specialises in pastry, this "pastry chef" also needs the methods of the normal chef, so it "inherits" them 
# Methods but also attributes can be inherited

# Code example:
# class Fish (Animal): # Animal is the class that the class "Fish" should inherit (inserted as a parameter)
    # def __init__(self): # initialisation of the "Fish" class
        # super().__init() # super() initialisation -> initialises everything that the animal function has

class Animal:
    def __init__(self) -> None:
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):

    def __init__(self) -> None:
        super().__init__()

    def swim(self):
        print("Moving in the water")

    # To modify a certain class from the super class you can do:

    def breathe(self):
        super().breathe() # Does everything that the super class does 
        print("Doing this underwater. Please help me I am under the water!") # New added code to the breathe() method of the fish class, you basically build on top of it


nemo = Fish()

nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

# Object from "Fish" class now has access to all attributes and methods of the "Animal" class (super class)
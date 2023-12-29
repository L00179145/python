'''
Anatomy of a simple class
By: Rahul Kharade
17 DEC 2023
'''


class Dog:
    # Class variable
    species = "Bulldog"

    # Constructor (initializer) method
    def __init__(self, name, age):
        # Instance variables
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        print("Woof!")

    # Another instance method
    def describe(self):
        print(f"{self.name} is {self.age} years old.")

# Creating an instance of the Dog class
my_dog = Dog(name="Shera", age=4)

# Accessing instance variables
print(f"{my_dog.name} is a {my_dog.species}")

# Calling instance methods
my_dog.bark()
my_dog.describe()


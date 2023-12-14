#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self):
        self._name = None

    def __init__(self):    
        self._breed = None

    def get_name(self):
        print("Retrieving name.")
        return self._name
    
    def get_breed(self):
        print("retrieving breed")
        return self._breed
    
    def set_name(self, name):
        if(type(name) in (str,)) and (1 <= len(name) <= 25):
            print(f"setting name to {name}.")
            self._name = name

        else:
            print("Name must be string between 1 and 25 characters.")

    
    def set_breed(self, breed):
        if breed in APPROVED_BREEDS:
            print(f"setting breed to {breed}.")
            self._breed = breed

        else:
            print("Breed must be in list of approved breeds." )    



    name = property(get_name, set_name,)   
    breed = property(get_breed, set_breed,)

# Example usage:
my_dog = Dog()

# Setting a valid name
my_dog.name = "Buddy"
print(my_dog.name)  # Output: Buddy

# Attempting to set an invalid name
my_dog.name = ""

my_dog = Dog()

my_dog.breed = "French"
print(my_dog.breed)



#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self):
        self._name = None

    def get_name(self):
        print("retrieving name")
        return self._name
    
    def set_name(self, name):
        if (type(name) in (str)) and(0< len(name) < 25):
            name.title()
            print(f"setting name to {name}.")
            self._name = name

        else:
            print( "Name must be string under 25 characters.")

    name = property(get_name, set_name,)   

my_person = Person()
my_person.name = "tish"
print(my_person.name)  
my_person.name = "7767"             

            

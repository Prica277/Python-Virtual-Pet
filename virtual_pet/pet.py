"""
Filename: pet.py
Author: Alex Price
Description: A virtual pet complete with pet emotions, and behavior. 
"""

class Pet:
    """A virtual pet (can be used as a base class for other pet types).
    
    Attributes:
        name: str
        breed: str
        nicknames: list (a list strings of given nicknames for your pet)
        happiness: int (how happy is the pet from 0-10, with 10 is happiest)
        hunger: int (how hungery the pet is, the higher the number the 
            hungrier the pet)
        health: int (how healthy is the pet)
    """

    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.breed = breed
        self.nicknames = []
        self.happiness = 5
        self.hunger = 4
        self.health = 50

# global scope
if __name__ == "__main__":
    # Construct 2 pet instances
    fluffy = Pet("Fluffy", "rock")
    lesser_fluffy = Pet("Lesser Fluffy", "mole")

    # Show some pet stats
    print(f"Our first pet is {fluffy.name}.")
    print(f"{fluffy.name} is a {fluffy.breed}.")
    print(f"Our second pet is {lesser_fluffy.name}.")
    print(f"{lesser_fluffy.name} is a {lesser_fluffy.breed}.")
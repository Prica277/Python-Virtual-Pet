""" 
Filename: possible_pets.py
Author: Alex Price
Description: A virtual pet complete with emotions!
"""
import random
import uuid
import utilities

breeds = ( "bird", "snake", "hampster")

class Pet:
    """A virtual pet (can be used as a base class for other pet types).
    
    Attributes:
        name: str
        breed: str
        nicknames: list (a list strings of given nicknames for your pet)
        happiness: int (how happy is the pet from 0-10, with 10 is happiest)
        hunger: int (how hungry the pet is, the higher the number the 
            hungrier the pet)
        health: int (how healthy is the pet)
    """
    # constructor method
    def __init__(self, name: str, breed: str) -> None:
        self.name = name
        self.ID = uuid.uuid().hex
        self.breed = breed
        self.nicknames = []
        self.happiness = 5
        self.hunger = 4
        self.health = 50
        self.exhaustion = 0

    def store_pet_data(self) -> None:
        """Insert pet information into the pets.json file"""

    def load_data(self) -> None: 
        """Grab pet data from the pets.json file and get the attributes"""

        # Get all pets from pet.json

    def play(self):
        """Let the user choose how to play with the pet."""
        menu = f"\nChoose how you would like to play with {self.name}:\n"
        menu += "\n\t1 - Fetch\n\t2 - Tug-Of-War"
        menu += "\n\t3 - Stroke Pet\n\t4 - Quit"

        choice = ""
        while choice != "4":
            choice = utilities.get_menu_choice(menu, ("1", "2", "3", "4"))
            if choice == "1":
                description = (f"{self.name} goes after the toy you toss. ")
                if random.choice("01") == "1":
                    description = f"{self.name} grabs the toy and runs away " 
                    description += "with it. "
                    self.happiness += 1
                    # quit since the pet ran off with the toy
                    choice = "4"
                else:
                    description = f"{self.name} goes after the toy you toss. "
                    description += f"{self.name} drops the toy at your feet. "
                    description += f"{self.name} seems to really like this game!"
                    self.happiness += 2
            elif choice == "2":
                description = f"{self.name} gladly grabs the rope toy and "
                description += "begins to pull on it."
                if random.choice("01") == "1":
                    description = f"{self.name} sucessfully pulls the rope toy "
                    description += "out of your hands and runs away with it. "
                    self.happiness += 1
                    # quit since the pet ran off with the toy
                    choice == "4"
                else: 
                    description = f"{self.name} loses its grip on the rope toy "
                    description += "and falls over into your lap. "
                    description += f"{self.name} seems to like this game!"
                    self.happiness += 1
            elif choice == "3":
                description = f"You stroke {self.name}'s back."
                if random.choice("01") == "1":
                    description = f"{self.name} huffs and pulls away. It seems "
                    description += "that it doesn't want to be petted right now."
                    self.happiness -= 1
                    # quit because the pet is upset
                    choice == "4"
                else: 
                    description = f"{self.name} becomes a happy puddle on the "
                    description += "floor. It likes being petted!"
                    self.happiness += 1
            elif choice == "4":
                description = f"{self.name} seems disappointed, but goes back to "
                description += "their favorite spot. You are done playing."
            else:
                description = f"{self.name} looks very pleased! "

                # hunger and exhaustion increase
                self.hunger += 1
                self.exhaustion += 1

                #keep happiness capped at 10
                if self.happiness > 10:
                    self.happiness = 10
                print(description)
            # after play, provide update
            description += f"{self.name}'s happiness is at {self.happiness}"

    def feed(self):
        """Let the user choose how to feed the pet."""
        menu = f"\nChoose how you would like to feed {self.name}:\n"
        menu += "\n\t1 - Pet Food\n\t2 - Human Food"
        menu += "\n\t3 - Treats\n\t4 - Quit"

        choice = ""
        while choice != "4":
            choice = utilities.get_menu_choice(menu, ("1", "2", "3", "4"))
            if choice == "1":
                description = (f"{self.name} happily starts to eat.")
                if random.choice("01") == "1":
                    description = f"{self.name} makes a disgusted expression. " 
                    description += "It seems the food is not to their taste."
                    self.happiness -= 1
                    # quit because the pet is upset
                    choice = "4"
                else:
                    description = f"{self.name} finishes their meal and "
                    description += "looks very pleased!"
                    self.hunger -= 2
            elif choice == "2":
                description = (f"{self.name} seems happy that you're sharing ")
                description += "with them and starts to eat."
                if random.choice("01") == "1":
                    description = f"{self.name} gives you a betrayed look and "
                    description += "wanders off. It seems that the food made them "
                    description += "feel sick."
                    self.health -= 5
                    # quit because the pet is upset
                    choice = "4"
                else: 
                    description = f"{self.name} finishes their meal and "
                    description += "looks very pleased!"
                    self.hunger -= 2
            elif choice == "3":
                description = (f"You give {self.name} a treat. They seem to ")
                description += "really enjoy it!"
                self.hunger -= 1
                self.happiness += 1
            else: 
                description = f"{self.name} looks like it's done eating. "

                #keep happiness capped at 10
                if self.happiness > 10:
                    self.happiness = 10
                print(description)
                
                #keep hunger from going below 0
                if self.hunger < 0:
                    self.hunger = 0
                print(description)

            # after feeding, provide update
            description += f"{self.name}'s hunger is at {self.hunger}"    

    def __str__(self) -> str:
        rep = f"Name: {self.name} \nBreed: {self.breed}"
        return rep
        


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
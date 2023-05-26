import utilities
import json
from possible_pets import Pet

def main():
    active_pets = []
    # Create a menu for pet playground
    new_menu = """
    Here is your list of options:

        1 - Option 1: Create a new pet
        2 - Option 2: Select your pet to interact with
        3 - Option 3: Save pet data
        4 - Option 4: Quit
    """
    options = ("1", "2", "3", "4")
    choice = ""
    while choice != "4":
        choice = utilities.get_menu_choice(new_menu, options)
        if choice == "1":
            pet = create_new_pet()
            active_pets.append(pet)
        elif choice == "2":
            pet = get_pets()
            get_active_pets(active_pets, pets)

            if not active_pets:
                print("\nYou have no pets to play with.")
                print("Try creating a new pet.")
                break
            current_pet = get_current_pet(active_pets)

        elif choice == "3":
            if active_pets:
                for pet in active_pets:
                    pet.store_pet_data()

def get_current_pet(pets):
    """Show all pets and have user select which pet to interact with."""
    # If there is only one active pet, return it
    if len(pets) == 1:
        return pets[0]
    
    choice = ""

    #build menu
    menu = "Which pet would you like to interact with?\n"
    legal_choices = []
    for i in range(len(pets)):
        legal_choices.append(str(i))
        menu += "\n" + str(i) + f"\t{pets[i]}"
    while choice not in legal_choices:
        choice = utilities.get_menu_choice(menu, tuple(legal_choices))
    return pets[int(choice)]


def get_active_pets(active_pets, pets):


def create_new_pet():
    """ creates and returns a new pet object"""
    name = input("Select a name for your pet: ")
    breed = input("Select a pet breed: ")
    pet = Pet(name, breed)
    return pet

    print("\nThanks for playing.")


if __name__ == "__main__":
    main()
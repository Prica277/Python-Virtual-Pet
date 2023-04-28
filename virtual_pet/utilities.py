""" 
Filename: utilities.py
Author: Alex Price
Description: A set of functions to be used to make the program more useful and 
be used in similar projects.
"""

# import statements
import possible_pets as pets

def get_menu_choice(menu: str, legal_choices: tuple) -> str:
    """displays a menu of options, and asks the user to make a choice.
    
    Args:
        menu: a formatted string of choices for the user
        legal_choices: a tuple of only choices the user is allowed to 
            make

    Returns:
        user_choices: a single character that must be one of the legal choices
    """

    user_choice = ""
    while user_choice not in legal_choices:
        print(menu)
        user_choice = input("Your Choice: ")
        # Give feedback if user didn't use proper choice
        if user_choice not in legal_choices:
            print("Sorry, that is not an option. Please select one of the following: ")
            print(legal_choices)

    return user_choice


def get_pet() -> pets.Pet:
    """Picks a pet for the user
    """
    name = input("Enter a name for your pet: ")
    breed_menu = "Choose a breed: "
    num = 1
    choices = []
    for breed in pets.breeds: 
        breed_menu += f"\n\t{num} - {breed} "
        choices.append(str(num))
        num += 1
    breed = get_menu_choice(breed_menu, tuple(choices))
    user_pet = pets.Pet(name, breed)
    return user_pet

if __name__ == "__main__":
    my_pet = get_pet()
    print(my_pet)

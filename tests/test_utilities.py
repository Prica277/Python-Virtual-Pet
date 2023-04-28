import virtual_pet.utilities

def test_get_menu_choice_for_legitimite_output():
    menu = "Options: 1, 2, or 3"
    legal_choices = ("1", "2", "3")
    result = utilities.get_menu_choice(menu, legal_choices)
    assert result in legal_choices
# Affrimation
wrong_response = ["Better luck next time!",  "Keep trying!", "Almost!", "Don't give up"]
right_response = ["Well-done", "Good job!", "Excellent", "Your getting the hang of this!"]
phon_alpha_choice = 0
sub_menu_choice = 0
# Main menu function for the user to choose hiragana or katakana
def main_menu():
    """ This function is giving the user a choice of which phonetic alphabet they want to practice. """
    global phon_alpha_choice
    phon_alpha_choice = input(int("What Japanese alphabet would you like to practice (enter number of choice)? \n 1. Hiragana \n 2. Katakana"))
    return
# Sub menu function of what the user wants to do with chosen alphabet
def sub_menu():
    global sub_menu_choice
    sub_menu_choice = input(int("What would you like to do with this alphabet:\n 1. preview/ learning \n 2. Game/ test \n 3. game rules"))
    return




# Introduce the game and ask the user for their name
print("Welcome to Ni Hon Go!")
name = input("what is your name?")
print("Hello {}".format(name).title())
main_menu()
sub_menu()

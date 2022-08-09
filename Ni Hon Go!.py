# Affrimation
wrong_response = ["Better luck next time!",  "Keep trying!", "Almost!", "Don't give up"]
right_response = ["Well-done", "Good job!", "Excellent", "Your getting the hang of this!"]

# Main menu function for the user to choose hiragana or katakana
def main_menu():
    """ This function is giving the user a choice of which phonetic alphabet they want to practice. """
    phon_alpha_choice = input("What Japanese alphabet would you like to practice (enter number of choice)? \n 1. Hiragana \n 2. Katakana \n :")
    return phon_alpha_choice

# Sub menu function of what the user wants to do with chosen alphabet
def sub_menu():
    sub_menu_choice = input("What would you like to do with this alphabet:\n 1. preview/ learning \n 2. Game/ test \n 3. game rules\n:")
    return sub_menu_choice
# Menu of levels the user can choose from




# Introduce the game and ask the user for their name
print("Welcome to Ni Hon Go!")
name = input("what is your name?\n:")
print("Hello {}".format(name).title())

# Call menus for user
phon_alpha_result = main_menu()
sub_menu_result = sub_menu()

# Print preview of hiragana and katakana
if sub_menu_result == "1":
    if phon_alpha_result == "1":
        print("Hiragana Chart: \n あ = a, い = i　う = u,　え = e,　お = o ")
    if phon_alpha_result == "2":
        print("Katakana Chart: \n waiting for keyboard")



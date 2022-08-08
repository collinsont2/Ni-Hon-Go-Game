# Affrimation
wrong_response = ["Better luck next time!",  "Keep trying!", "Almost!", "Don't give up"]
right_response = ["Well-done", "Good job!", "Excellent", "Your getting the hang of this!"]


# Main menu function for the user to choose hiragana or katakana
def main_menu():
    """ This function is giving the user a choice of which phonetic alphabet they want to practice. """
    phon_alpha_choice = input(int("What Japanese alphabet would you like to practice (enter number of choice)? \n 1. Hiragana \n 2. Katakana"))

    return

# Introduce the game and ask the user for their name
print("Welcome to Ni Hon Go!")
name = input("what is your name?")
print("Hello {}".format(name).title())
main_menu()

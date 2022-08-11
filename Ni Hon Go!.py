# Affrimation
wrong_response = ["Better luck next time!",  "Keep trying!", "Almost!", "Don't give up"]
right_response = ["Well-done", "Good job!", "Excellent", "Your getting the hang of this!"]

# Keep score of the users progress for each hiragana level
level_1_hir_score = 0
level_2_hir_score = 0
level_3_hir_score = 0
level_4_hir_score = 0
level_5_hir_score = 0
level_6_hir_score = 0
level_7_hir_score = 0
level_8_hir_score = 0

# Keep score of the users progress for each katakana level
level_1_kat_score = 0
level_2_kat_score = 0
level_3_kat_score = 0
level_4_kat_score = 0
level_5_kat_score = 0
level_6_kat_score = 0
level_7_kat_score = 0
level_8_kat_score = 0

level_1_hir_dic = {"あ":"a", "い":"i", "う":"u", "え":"e", "お": "o", "か":"ka", "き": "ki", "く":"ku", "け":"ke", "こ":"ko"}
#level_2 =
#level_3 =
#level_4 =
#level_5 =
#level_6 =
#level_7 =
#level_8 =

#give the overall score to the user
overall_score = 0

# Main menu function for the user to choose hiragana or katakana
def main_menu():
    """ This function is giving the user a choice of which phonetic alphabet they want to practice. """
    phon_alpha_choice = input("What Japanese alphabet would you like to practice (enter number of choice)? \n 1. Hiragana \n 2. Katakana \n Alphabet:")
    return phon_alpha_choice

# Sub menu function of what the user wants to do with chosen alphabet
def sub_menu():
    """ This """
    sub_menu_choice = input("What would you like to do with this alphabet:\n 1. preview/ learning \n 2. Game/ test \n 3. game rules\n Choice:")
    return sub_menu_choice
# Menu of levels the user can choose from
def level_menu(phon_alpha_result):
    if phon_alpha_result == "1":
        level_menu_choice = input("Enter the number of the level you want to play.\n Level 1 [{0}/10] \n Level 2 [{1}/10] \n Level 3 [{2}/10] \n Level 4 [{3}/10] \n Level 5 [{4}/6] \n Level 6 [{5}/10] \n Level 7 [{6}/8] \n Level 8 [{7}/5]\n Final Level (9)\n Level:".format(level_1_hir_score, level_2_hir_score, level_3_hir_score, level_4_hir_score, level_5_hir_score, level_6_hir_score, level_7_hir_score, level_8_hir_score))
    elif phon_alpha_result == "2":
        level_menu_choice = input("Enter the number of the level you want to play.\n Level 1 [{0}/10] \n Level 2 [{1}/10] \n Level 3 [{2}/10] \n Level 4 [{3}/10] \n Level 5 [{4}/6] \n Level 6 [{5}/10] \n Level 7 [{6}/8] \n Level 8 [{7}/5]\n Final Level (9)\n Level:".format(level_1_kat_score, level_2_kat_score, level_3_kat_score, level_4_kat_score, level_5_kat_score, level_6_kat_score, level_7_kat_score, level_8_kat_score))
    return level_menu_choice

# Introduce the game and ask the user for their name
print("Welcome to Ni Hon Go!")
name = input("what is your name?\n:")
print("Hello {}".format(name).title())

# Call menus for user
phon_alpha_result = main_menu()
sub_menu_result = sub_menu()
chosen_level = level_menu(phon_alpha_result)

# Print preview of hiragana and katakana
if sub_menu_result == "1":
    if phon_alpha_result == "1":
        print("Hiragana Chart: \n あ = a, い = i　う = u,　え = e,　お = o ")
    if phon_alpha_result == "2":
        print("Katakana Chart: \n waiting for keyboard")
if sub_menu_result == "2":
    if chosen_level == "1":
       print("In this level we will be practicing:\n {}".format(level_1_hir_dic))
    if chosen_level == "2":
        if level_1_hir_score != 10:
            print("Try making sure you have got all questions right in the previous level")
        else:
            print("you do not have enough points to move on try redoing any you dont have full score")



# Write game rules
if sub_menu_result == "3":
    print(",ljgfklutf")



import random
# Affirmations
wrong_response = ["Better luck next time!",  "Keep trying!", "Almost!", "Don't give up"]
right_response = ["Well-done", "Good job!", "Excellent", "Your getting the hang of this!"]

# Track the overall score the user has for each alphabet
hir_overall_score = 0
kat_overall_score = 0
pate = True
# Create a dictionary for each level of hiragana
level_1_hir_dic = {"あ": "a", "い": "i", "う": "u", "え": "e", "お": "o", "か": "ka", "き": "ki", "く": "ku", "け": "ke", "こ": "ko"}
level_2_hir_dic = {"さ": "sa", "し": "shi", "す": "su", "せ": "se", "そ": "so", "た": "ta", "ち": "chi", "つ": "tsu", "て": "te", "と": "to"}
level_3_hir_dic = {"な": "na", "に": "ni", "ぬ": "nu", "ね": "ne", "の": "no", "は": "ha", "ひ": "hi", "ふ": "fu", "へ": "he", "ほ": "ho"}
level_4_hir_dic = {"ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo", "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro"}
level_5_hir_dic = {"や": "ya", "ゆ": "yu", "よ": "yo", "わ": "wa", "ん": "n", "を": "wo"}
level_6_hir_dic = {"が": "ga", "ぎ": "gi", "ぐ": "gu", "げ": "ge", "ご": "go", "ざ": "za", "じ": "ji", "ず": "zu", "ぜ": "ze", "そ": "zo"}
level_7_hir_dic = {"ば": "ba", "び": "bi", "ぶ": "bu", "べ": "be", "ぼ": "bo", "だ": "da", "で": "de", "ど": "do"}
level_8_hir_dic = {"ぱ": "pa", "ぴ": "pi", "ぷ": "pu", "ぺ": "pe", "ぽ": "po"}

# Create a dictionary for each level of katakana
level_1_kat_dic = {"ア": "a", "イ": "i", "ウ": "u", "エ": "e", "オ": "o", "カ": "ka", "キ": "ki", "ク": "ku", "ケ": "ke", "コ": "ko"}
level_2_kat_dic = {"サ": "sa", "シ": "shi", "ス": "su", "セ": "se", "ソ": "so", "タ": "ta", "チ": "chi", "ツ": "tsu", "テ": "te", "ト": "to"}
level_3_kat_dic = {"ナ": "na", "ニ": "ni", "ヌ": "nu", "ネ": "ne", "ノ": "no", "ハ": "ha", "ヒ": "hi", "フ": "fu", "ヘ": "he", "ホ": "ho"}
level_4_kat_dic = {"ま": "ma", "み": "mi", "む": "mu", "め": "me", "も": "mo", "ら": "ra", "り": "ri", "る": "ru", "れ": "re", "ろ": "ro"}
level_5_kat_dic = {"ヤ": "ya", "ユ": "yu", "ヨ": "yo", "ワ": "wa", "ン": "n", "ヲ": "wo"}
level_6_kat_dic = {"ガ": "ga", "ギ": "gi", "グ": "gu", "ゲ": "ge", "ゴ": "go", "ザ": "za", "ジ": "ji", "ズ": "zu", "ゼ": "ze", "ゾ": "zo"}
level_7_kat_dic = {"バ": "ba", "び": "bi", "ブ": "bu", "ベ": "be", "ボ": "bo", "ダ": "da", "デ": "de", "ド": "do"}
level_8_kat_dic = {"パ": "pa", "ピ": "pi", "プ": "pu", "ペ": "pe", "ポ": "po"}

# Create a list of the keys from the level dictionaries

level_1_hir_keys = list(level_1_hir_dic.keys())
level_2_hir_keys = list(level_2_hir_dic.keys())
level_3_hir_keys = list(level_3_hir_dic.keys())
level_4_hir_keys = list(level_4_hir_dic.keys())
level_5_hir_keys = list(level_5_hir_dic.keys())
level_6_hir_keys = list(level_6_hir_dic.keys())
level_7_hir_keys = list(level_7_hir_dic.keys())
level_8_hir_keys = list(level_8_hir_dic.keys())

level_1_kat_keys = list(level_1_kat_dic.keys())
level_2_kat_keys = list(level_2_kat_dic.keys())
level_3_kat_keys = list(level_3_kat_dic.keys())
level_4_kat_keys = list(level_4_kat_dic.keys())
level_5_kat_keys = list(level_5_kat_dic.keys())
level_6_kat_keys = list(level_6_kat_dic.keys())
level_7_kat_keys = list(level_7_kat_dic.keys())
level_8_kat_keys = list(level_8_kat_dic.keys())

# Main menu function for the user to choose hiragana or katakana
def main_menu():
    """ This function is giving the user a choice of which phonetic alphabet they want to practice. """
    phon_alpha_choice = input("What Japanese alphabet would you like to practice (enter number of choice)? \n 1. Hiragana \n 2. Katakana \n Alphabet:")
    return phon_alpha_choice

# Sub menu function of what the user wants to do with chosen alphabet
def sub_menu():
    """ This function is giving the user a choice on what to do with the chosen alphabet, as well as going back to choose a different alphabet."""
    sub_menu_choice = input("What would you like to do with this alphabet:\n 1. preview/ learning \n 2. Game/ test \n 3. game rules\n 4. Go back to main menu \n CHOICE:")
    return sub_menu_choice
# Menu of hiragana levels the user can choose from
def hir_level_menu(hir_overall_score):
    """This function shows the user the number of levels they can choose from and let them select. This also marks a level as complete when the needed score is reached."""
    hir_level_menu_choice = input(
        "Enter the number of the level you want to play.\n Level 1 \n Level 2 \n Level 3 \n Level 4 \n Level 5 \n Level 6 \n Level 7 \n Level 8 \n Final Level (9)\n"
        " Go back to main menu (10) \n LEVEL:")
    # Show the user if they have completed a level or not
    if hir_overall_score >= 100:
        hir_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 \n Level 3 \n Level 4 \n Level 5 \n Level 6 \n Level 7 \n Level 8 \n Final Level (9)\n"
            " Go back to main menu (10) \nLEVEL:")
    if hir_overall_score >= 200:
        hir_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 \n Level 4 \n Level 5 \n Level 6 \n Level 7 \n Level 8 \n"
            " Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if hir_overall_score >= 300:
        hir_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 \n Level 5 \n Level 6 \n Level 7 \n Level 8 \n "
            "Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if hir_overall_score >= 400:
        hir_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 (Complete)\n Level 5 \n Level 6 \n Level 7 \n "
            "Level 8 \n Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if hir_overall_score >= 460:
        hir_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 (Complete)\n Level 5 (Complete)\n Level 6 \n Level 7 \n"
            " Level 8 \n Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if hir_overall_score >= 560:
        hir_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 (Complete)\n Level 5 (Complete)\n Level 6 (Complete)\n"
            " Level 7 \n Level 8 \n Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if hir_overall_score >= 640:
        hir_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 (Complete)\n Level 5 (Complete)\n Level 6 (Complete)\n"
            " Level 7 (Complete)\n Level 8 \n Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if hir_overall_score >= 690:
        hir_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 (Complete)\n Level 5 (Complete)\n Level 6 (Complete)\n"
            " Level 7 (Complete)\n Level 8 (Complete)\n Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    # if hir_overall_score >= 100:
    #     hir_level_menu_choice = input(
    #         "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 \n Level 3 \n Level 4 \n Level 5 \n Level 6 \n Level 7 \n Level 8 \n Final Level (9)\n"
    #         "Go back to main menu (10) \n LEVEL:")
    return hir_level_menu_choice

# Menu of katakana levels the user can choose from
def kat_level_menu(kat_overall_score):
    """This function shows the user the number of levels they can choose from and let them select. This also marks a level as complete when the needed score is reached."""
    kat_level_menu_choice = input(
        "Enter the number of the level you want to play.\n Level 1 \n Level 2 \n Level 3 \n Level 4 \n Level 5 \n Level 6 \n Level 7 \n Level 8 \n Final Level (9)\n"
        " Go back to main menu (10) \n LEVEL:")
    # Show the user if they have completed a level or not
    if kat_overall_score >= 100:
        kat_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 \n Level 3 \n Level 4 \n Level 5 \n Level 6 \n Level 7 \n Level 8 \n Final Level (9)\n"
            " Go back to main menu (10) \nLEVEL:")
    if kat_overall_score >= 200:
        kat_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 \n Level 4 \n Level 5 \n Level 6 \n Level 7 \n Level 8 \n"
            " Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if kat_overall_score >= 300:
        kat_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 \n Level 5 \n Level 6 \n Level 7 \n Level 8 \n "
            "Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if kat_overall_score >= 400:
        kat_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 (Complete)\n Level 5 \n Level 6 \n Level 7 \n "
            "Level 8 \n Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if kat_overall_score >= 460:
        kat_level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 (Complete)\n Level 5 (Complete)\n Level 6 \n Level 7 \n"
            " Level 8 \n Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if kat_overall_score >= 560:
        level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 (Complete)\n Level 5 (Complete)\n Level 6 (Complete)\n"
            " Level 7 \n Level 8 \n Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if kat_overall_score >= 640:
        level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 (Complete)\n Level 5 (Complete)\n Level 6 (Complete)\n"
            " Level 7 (Complete)\n Level 8 \n Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    if kat_overall_score >= 690:
        level_menu_choice = input(
            "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 (Complete)\n Level 3 (Complete)\n Level 4 (Complete)\n Level 5 (Complete)\n Level 6 (Complete)\n"
            " Level 7 (Complete)\n Level 8 (Complete)\n Final Level (9)\n Go back to main menu (10) \n LEVEL:")
    # if kat_overall_score >= 100:
    #     kat_level_menu_choice = input(
    #         "Enter the number of the level you want to play.\n Level 1 (Complete)\n Level 2 \n Level 3 \n Level 4 \n Level 5 \n Level 6 \n Level 7 \n Level 8 \n Final Level (9)\n"
    #         "Go back to main menu (10) \n LEVEL:")
    return kat_level_menu_choice
# Introduce the game and ask the user for their name
print("Welcome to Ni Hon Go!")
name = input("what is your name?\nNAME:")
print("Hello {}".format(name).title())

# Call menus for user
while pate == True:
    phon_alpha_result = main_menu()

    # Hiragana alphabet path
    if phon_alpha_result == "1":
        sub_menu_result = sub_menu()

        # Print preview of hiragana
        if sub_menu_result == "1":
            print("Hiragana Chart: \n あ = a, い = i　う = u,　え = e,　お = o ")
        while sub_menu_result == "2":
            hir_chosen_level = hir_level_menu(hir_overall_score)
# Level one hiragana
            if hir_chosen_level == "1":
                print("In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(level_1_hir_dic))
                print("Please note that if you have already reached the top score in this level it will not add to your score")
                start = input("Enter 'go' to start and enter 'stop' at anytime to quit:")
                random.shuffle(level_1_hir_keys)
                while start == "go":
                    print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    for hir in level_1_hir_keys:
                        answer = input("{}:                    SCORE:{} \nANSWER: ".format(hir, hir_overall_score))
                        if answer == 'stop':
                            start = 'Neutral'
                            break
                        if hir_overall_score < 100:
                            if answer == level_1_hir_dic[hir]:
                                random.shuffle(right_response)
                                print("{}".format(right_response[0]))
                                hir_overall_score += 10
                                # Add affirmations for after the points are reached
                            else:
                                random.shuffle(wrong_response)
                                print("{}".format(wrong_response[0]))
                    if hir_overall_score > 0 and hir_overall_score < 100:
                        print("Good job! you got {} points, but you need 100 points to move to the next level".format(hir_overall_score))
                        start = 'Neutral'
                    elif hir_overall_score == 0:
                        print("Try again")
                        start = 'Neutral'
                    elif hir_overall_score == 100:
                        print("Well done you got 100 points! you can move onto the next level.")
                        start = 'Neutral'
                if start == "stop":
                    hir_chosen_level = "0"
                    start = 'Neutral'
                    # sub_menu()
                    break
# Level 2 hiragana
            if hir_chosen_level == "2":
                if hir_overall_score < 100:
                    print("You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print("In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(level_2_hir_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_2_hir_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for hir in level_2_hir_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(hir, hir_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if hir_overall_score < 200:
                                if answer == level_2_hir_dic[hir]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    hir_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if hir_overall_score > 100 and hir_overall_score < 200:
                            print("Good job! you got {} points, but you need 200 points to move to the next level".format(hir_overall_score))
                            start = 'Neutral'
                        elif hir_overall_score == 100:
                            print("Try again")
                            start = 'Neutral'
                        elif hir_overall_score == 200:
                            print("Well done you got 200 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 3 hiragana
            if hir_chosen_level == "3":
                if hir_overall_score < 200:
                    print("You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print("In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(level_3_hir_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_3_hir_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for hir in level_3_hir_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(hir, hir_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if hir_overall_score < 300:
                                if answer == level_3_hir_dic[hir]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    hir_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if hir_overall_score > 200 and hir_overall_score < 300:
                            print("Good job! you got {} points, but you need 300 points to move to the next level".format(hir_overall_score))
                            start = 'Neutral'
                        elif hir_overall_score == 200:
                            print("Try again")
                            start = 'Neutral'
                        elif hir_overall_score == 300:
                            print("Well done you got 300 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 4 hiragana
            if hir_chosen_level == "4":
                if hir_overall_score < 300:
                    print("You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print("In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(level_4_hir_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_4_hir_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for hir in level_4_hir_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(hir, hir_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if hir_overall_score < 400:
                                if answer == level_4_hir_dic[hir]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    hir_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if hir_overall_score > 300 and hir_overall_score < 400:
                            print("Good job! you got {} points, but you need 400 points to move to the next level".format(hir_overall_score))
                            start = 'Neutral'
                        elif hir_overall_score == 300:
                            print("Try again")
                            start = 'Neutral'
                        elif hir_overall_score == 400:
                            print("Well done you got 400 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 5 hiragana
            if hir_chosen_level == "5":
                if hir_overall_score < 400:
                    print("You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print("In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(level_5_hir_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_5_hir_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for hir in level_5_hir_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(hir, hir_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if hir_overall_score < 460:
                                if answer == level_5_hir_dic[hir]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    hir_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if hir_overall_score > 400 and hir_overall_score < 460:
                            print("Good job! you got {} points, but you need 460 points to move to the next level".format(hir_overall_score))
                            start = 'Neutral'
                        elif hir_overall_score == 400:
                            print("Try again")
                            start = 'Neutral'
                        elif hir_overall_score == 460:
                            print("Well done you got 460 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 6 hiragana
            if hir_chosen_level == "6":
                if hir_overall_score < 460:
                    print("You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print("In this lesson we will be working with the same characters from the last levels but this time the characters have a extra two dashes on "
                          "the top right corner. This is called Dakuten, it alters the sound of a character slightly. E.G when Dakuten is added becomes a K sound becomes a G sound"
                          ", S becomes a Z, H becomes  a B and T becomes D. ")
                    print("In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(level_6_hir_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_6_hir_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for hir in level_6_hir_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(hir, hir_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if hir_overall_score < 560:
                                if answer == level_6_hir_dic[hir]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    hir_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if hir_overall_score > 460 and hir_overall_score < 560:
                            print("Good job! you got {} points, but you need 560 points to move to the next level".format(hir_overall_score))
                            start = 'Neutral'
                        elif hir_overall_score == 460:
                            print("Try again")
                            start = 'Neutral'
                        elif hir_overall_score == 560:
                            print("Well done you got 560 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 7 hiragana
            if hir_chosen_level == "7":
                if hir_overall_score < 560:
                    print("In this level we will practise more of the Dakuten characters.")
                    print("You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print("In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(level_7_hir_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_7_hir_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for hir in level_7_hir_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(hir, hir_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if hir_overall_score < 640:
                                if answer == level_7_hir_dic[hir]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    hir_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if hir_overall_score > 560 and hir_overall_score < 640:
                            print("Good job! you got {} points, but you need 640 points to move to the next level".format(hir_overall_score))
                            start = 'Neutral'
                        elif hir_overall_score == 560:
                            print("Try again")
                            start = 'Neutral'
                        elif hir_overall_score == 640:
                            print("Well done you got 640 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 8 hiragana
            if hir_chosen_level == "8":
                if hir_overall_score < 640:
                    print("You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print("In this lesson we will be working with the same characters from the last levels but this time the characters have a small circle on "
                          "the top right corner. This is called Handakuten, it alters the sound of a character slightly. E.G when Handakuten is added H becomes P")
                    print("In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(level_8_hir_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_8_hir_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for hir in level_8_hir_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(hir, hir_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if hir_overall_score < 690:
                                if answer == level_8_hir_dic[hir]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    hir_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if hir_overall_score > 640 and hir_overall_score < 690:
                            print("Good job! you got {} points, but you need 690 points to move to the FINAL level".format(hir_overall_score))
                            start = 'Neutral'
                        elif hir_overall_score == 640:
                            print("Try again")
                            start = 'Neutral'
                        elif hir_overall_score == 690:
                            print("Well done you got 690 points! you can move onto the FINAL level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
            # Final level
            if hir_chosen_level == "9":
                print("Under construction")
            # go back to main menu
            if hir_chosen_level == "10":
                main_menu()
        # Print game rules
        if sub_menu_result == "3":
            print("Under construction")
        # Return to main menu
        if sub_menu_result == "4":
            main_menu()
        else:
            print("That is not an option")
            main_menu()

    # Katakana alphabet path
    elif phon_alpha_result == "2":
        sub_menu_result = sub_menu()

        # Print preview of katakana
        if sub_menu_result == "1":
            print("Katakana Chart: \n あ = a, い = i　う = u,　え = e,　お = o ")
        while sub_menu_result == "2":
            kat_chosen_level = kat_level_menu(kat_overall_score)
# Level one katakana
            if kat_chosen_level == "1":
                print(
                    "In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(
                        level_1_kat_dic))
                print(
                    "Please note that if you have already reached the top score in this level it will not add to your score")
                start = input("Enter 'go' to start and enter 'stop' at anytime to quit:")
                random.shuffle(level_1_kat_keys)
                while start == "go":
                    print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                    for kat in level_1_kat_keys:
                        answer = input("{}:                    SCORE:{} \nANSWER: ".format(kat, kat_overall_score))
                        if answer == 'stop':
                            start = 'Neutral'
                            break
                        if kat_overall_score < 100:
                            if answer == level_1_kat_dic[kat]:
                                random.shuffle(right_response)
                                print("{}".format(right_response[0]))
                                kat_overall_score += 10
                            else:
                                random.shuffle(wrong_response)
                                print("{}".format(wrong_response[0]))
                    if kat_overall_score > 0 and kat_overall_score < 100:
                        print("Good job! you got {} points, but you need 100 points to move to the next level".format(
                            kat_overall_score))
                        start = 'Neutral'
                    elif kat_overall_score == 0:
                        print("Try again")
                        start = 'Neutral'
                    elif kat_overall_score == 100:
                        print("Well done you got 100 points! you can move onto the next level.")
                        start = 'Neutral'
                if start == "stop":
                    chosen_level = "0"
                    sub_menu()
# Level 2 katakana
            if kat_chosen_level == "2":
                if kat_overall_score < 100:
                    print(
                        "You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print(
                        "In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(
                            level_2_kat_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_2_kat_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for kat in level_2_kat_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(kat, kat_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if kat_overall_score < 200:
                                if answer == level_2_kat_dic[kat]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    kat_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if kat_overall_score > 100 and kat_overall_score < 200:
                            print(
                                "Good job! you got {} points, but you need 200 points to move to the next level".format(
                                    kat_overall_score))
                            start = 'Neutral'
                        elif kat_overall_score == 100:
                            print("Try again")
                            start = 'Neutral'
                        elif kat_overall_score == 200:
                            print("Well done you got 200 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 3 katakana
            if kat_chosen_level == "3":
                if kat_overall_score < 200:
                    print(
                        "You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print(
                        "In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(
                            level_3_kat_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_3_kat_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for kat in level_3_kat_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(kat, kat_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if kat_overall_score < 300:
                                if answer == level_3_kat_dic[kat]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    kat_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if kat_overall_score > 200 and kat_overall_score < 300:
                            print(
                                "Good job! you got {} points, but you need 300 points to move to the next level".format(
                                    kat_overall_score))
                            start = 'Neutral'
                        elif kat_overall_score == 200:
                            print("Try again")
                            start = 'Neutral'
                        elif kat_overall_score == 300:
                            print("Well done you got 300 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 4 katakana
            if kat_chosen_level == "4":
                if kat_overall_score < 300:
                    print(
                        "You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print(
                        "In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(
                            level_4_kat_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_4_kat_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for kat in level_4_kat_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(kat, kat_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if kat_overall_score < 400:
                                if answer == level_4_kat_dic[kat]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    kat_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if kat_overall_score > 300 and kat_overall_score < 400:
                            print(
                                "Good job! you got {} points, but you need 400 points to move to the next level".format(
                                    kat_overall_score))
                            start = 'Neutral'
                        elif kat_overall_score == 300:
                            print("Try again")
                            start = 'Neutral'
                        elif kat_overall_score == 400:
                            print("Well done you got 400 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 5 katakana
            if kat_chosen_level == "5":
                if kat_overall_score < 400:
                    print(
                        "You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print(
                        "In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(
                            level_5_kat_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_5_kat_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for kat in level_5_kat_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(kat, kat_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if kat_overall_score < 460:
                                if answer == level_5_kat_dic[kat]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    kat_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if kat_overall_score > 400 and kat_overall_score < 460:
                            print(
                                "Good job! you got {} points, but you need 460 points to move to the next level".format(
                                    kat_overall_score))
                            start = 'Neutral'
                        elif kat_overall_score == 400:
                            print("Try again")
                            start = 'Neutral'
                        elif kat_overall_score == 460:
                            print("Well done you got 460 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 6 katakana
            if kat_chosen_level == "6":
                if kat_overall_score < 460:
                    print(
                        "You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print(
                        "In this lesson we will be working with the same characters from the last levels but this time the characters have a extra two dashes on "
                        "the top right corner. This is called Dakuten, it alters the sound of a character slightly. E.G when Dakuten is added becomes a K sound becomes a G sound"
                        ", S becomes a Z, H becomes  a B and T becomes D. ")
                    print(
                        "In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(
                            level_6_kat_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_6_kat_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for kat in level_6_kat_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(kat, kat_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if kat_overall_score < 560:
                                if answer == level_6_kat_dic[kat]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    kat_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if kat_overall_score > 460 and kat_overall_score < 560:
                            print(
                                "Good job! you got {} points, but you need 560 points to move to the next level".format(
                                    kat_overall_score))
                            start = 'Neutral'
                        elif kat_overall_score == 460:
                            print("Try again")
                            start = 'Neutral'
                        elif kat_overall_score == 560:
                            print("Well done you got 560 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 7 katakana
            if kat_chosen_level == "7":
                if kat_overall_score < 560:
                    print("In this level we will practise more of the Dakuten characters.")
                    print(
                        "You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print(
                        "In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(
                            level_7_kat_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_7_kat_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for kat in level_7_kat_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(kat, kat_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if kat_overall_score < 640:
                                if answer == level_7_kat_dic[kat]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    kat_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if kat_overall_score > 560 and kat_overall_score < 640:
                            print(
                                "Good job! you got {} points, but you need 640 points to move to the next level".format(
                                    kat_overall_score))
                            start = 'Neutral'
                        elif kat_overall_score == 560:
                            print("Try again")
                            start = 'Neutral'
                        elif kat_overall_score == 640:
                            print("Well done you got 640 points! you can move onto the next level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
# Level 8 katakana
            if kat_chosen_level == "8":
                if kat_overall_score < 640:
                    print(
                        "You dont have access to this level yet, try making sure you have got all questions right in the previous level")
                else:
                    print(
                        "In this lesson we will be working with the same characters from the last levels but this time the characters have a small circle on "
                        "the top right corner. This is called Handakuten, it alters the sound of a character slightly. E.G when Handakuten is added H becomes P")
                    print(
                        "In this level we will be practicing:\n {}\nWe encourage you to repeat the sounds out loud.".format(
                            level_8_kat_dic))
                    start = input("enter 'go' to start and enter 'stop' at anytime to quit:")
                    random.shuffle(level_8_kat_keys)
                    while start == "go":
                        print(" \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n \n")
                        for kat in level_8_kat_keys:
                            answer = input("{}:                    SCORE:{} \nANSWER: ".format(kat, kat_overall_score))
                            if answer == 'stop':
                                start = 'Neutral'
                                break
                            if kat_overall_score < 690:
                                if answer == level_8_kat_dic[kat]:
                                    random.shuffle(right_response)
                                    print("{}".format(right_response[0]))
                                    kat_overall_score += 10
                                else:
                                    random.shuffle(wrong_response)
                                    print("{}".format(wrong_response[0]))
                        if kat_overall_score > 640 and kat_overall_score < 690:
                            print(
                                "Good job! you got {} points, but you need 690 points to move to the FINAL level".format(
                                    kat_overall_score))
                            start = 'Neutral'
                        elif kat_overall_score == 640:
                            print("Try again")
                            start = 'Neutral'
                        elif kat_overall_score == 690:
                            print("Well done you got 690 points! you can move onto the FINAL level.")
                            start = 'Neutral'
                    if start == "stop":
                        sub_menu()
            # Final level
            if kat_chosen_level == "9":
                print("Under construction")
            # go back to main menu
            if kat_chosen_level == "10":
                main_menu()
        # Print game rules
        if sub_menu_result == "3":
            print("Under construction")
        # Return to main menu
        if sub_menu_result == "4":
            main_menu()
        else:
            print("That is not an option")
            main_menu()

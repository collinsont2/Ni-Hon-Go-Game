# Affrimations
wrong_response = ["Better luck next time!",  "Keep trying!", "Almost!", "Don't give up"]
right_response = ["Well-done", "Good job!", "Excellent", "Your getting the hang of this!"]

# Track the overall score the user has
overall_score = 0

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
# Give the overall score to the user

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
def level_menu():
    level_menu_choice = input("Enter the number of the level you want to play.\n Level 1 \n Level 2 \n Level 3 \n Level 4 \n Level 5 \n Level 6 \n Level 7 \n Level 8 \n Final Level (9)\n Level:")
    return level_menu_choice

# Introduce the game and ask the user for their name
print("Welcome to Ni Hon Go!")
name = input("what is your name?\n:")
print("Hello {}".format(name).title())

# Call menus for user
phon_alpha_result = main_menu()
sub_menu_result = sub_menu()
chosen_level = level_menu()

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
        if overall_score <= 100:
            print("Try making sure you have got all questions right in the previous level")
        else:
            print("")



# Write game rules
if sub_menu_result == "3":
    print(",ljgfklutf")



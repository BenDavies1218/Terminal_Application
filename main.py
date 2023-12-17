from functions import game_menu, shuffler, select_case, game, game_finish, double_or_nothing
import csv

file = "gamelog.csv"

try:
    gamelog = open(file, "r")
    gamelog.close()

except FileNotFoundError:
    gamelog = open(file, "w")
    gamelog.write("Deal or No Deal\n")
    gamelog.close()

game_menu()

while True:

    cases = {
        1: 1,
        2: 5,
        3: 10,
        4: 25,
        5: 50,
        6: 75,
        7: 100,
        8: 200,
        9: 500,
        10: 750,
        11: 1000,
        12: 2500,
        13: 5000,
        14: 7500,
        15: 10000,
        16: 15000,
        17: 20000,
        18: 25000,
        19: 50000,
        20: 100000,
        21: 150000,
        22: 200000
    }

    shuffled_cases = shuffler(cases)

    user_case, cases_in_play = select_case()

    user_input_yes, banks_offer, total_money_left = game(cases, shuffled_cases, cases_in_play, user_case)

    play_again = double_or_nothing(user_case, shuffled_cases, user_input_yes, banks_offer)

    if game_finish(play_again) == True:
        break
    else:
        continue
exit()
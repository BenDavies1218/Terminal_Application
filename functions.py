import random
import csv
from colored import fg, attr, bg 
import subprocess

file = "gamelog.csv"

def game_menu():
        # clears the screen
    try:
        subprocess.run('clear')
    except:
        subprocess.run('cls')
    print("Welcome to Deal or No Deal Will you take home the top prize?")
    start_game = input("\npress any button to start... ")
    while True:
        try:
            name = input("\nPlease enter your name:  ")
            if all(letter.isalpha() or letter.isspace() for letter in name):
                break
            else:
                print("\n Invalid name please try again")
        except TypeError:
            print("Error in name variable")
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["Player", name])



def shuffler(cases):
    values = list(cases.values())
    shuffle_list = random.sample(values, len(values))
    shuffle_cases = dict(zip(cases.keys(), shuffle_list))
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["cases shuffled = True\n"])
    with open(file, "a") as f:
        writer = csv.writer(f)
        for key, value in shuffle_cases.items():
            writer.writerow([key, value])        
    return shuffle_cases



def select_case():
    cases_left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]
# print cases left to user
    try:
        subprocess.run('clear')
    except:
        subprocess.run('cls')
    print(cases_left)
    # user will input a number between and including 1-22
    while True:
        try:
            user_case = int(input("\nPlease Select your lucky case:  "))
            if user_case <= 22 and user_case >= 1:
                break
            else:
                print("Please choose a case between 1-22")
                continue
        except ValueError:
            print("Please enter an integer")
            continue
    # remove selected case from cases_left
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["Users_case", user_case])
    for case in cases_left:
        if user_case == case:
            cases_left.remove(case)
            break
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["case_removed", user_case])
    return user_case, cases_left
    # return selected case back to main



def game(cases, shuffle_cases, cases_left, user_case):
    interation = 0
    while interation < 6:
        count = 6 - int(interation)
    # while loop check if count =< 0
        while count != 0:
            # Checks if theres more than one case and breaks loop
            try:
                if len(cases_left) == 1:
                    interation += 6
                    user_input_yes = "no"
                    break
            except:
                continue
            # clears the screen
            try:
                subprocess.run('clear')
            except:
                subprocess.run('cls')
        # print cases_left to user
            print("\nMoney Left: ", *cases.values())
            print("Cases Left to open: ", *cases_left)
            print(f"\nYour Lucky Case Is:  {user_case}")
            try:
                print(f"The last Case opened: No. {rm_case} contained: ${rm_value}")
            except:
                print("")
            print(f"Next bank offer in: {count} cases")
            # ask user to enter a case to be removed
            while True:
                try:
                    tobe_removed = int(input("\nPlease select a Case to be removed:  "))
                    if tobe_removed in cases_left:
                        break
                    else:
                        print("Please enter a number from the list of cases left")
                except ValueError:
                    print("Please enter a valid integer")
            # remove case from cases left
            for case in cases_left:
                if case == tobe_removed:
                    rm_case = case
                    cases_left.remove(case)
                    break
            else:
                continue
            # to print value of removed case to user
            for key, value in shuffle_cases.items():
                if key == tobe_removed:
                    rm_value = value
                    break
            else:
                continue
            # remove value from game
            for key, value in cases.items():
                if value == rm_value:
                    cases.pop(key)
                    break
            else:
                continue
            with open(file, "a") as f:
                writer = csv.writer(f)
                writer.writerow(["case_removed", rm_case])
            count -= 1
        try:
            subprocess.run('clear')
        except:
            subprocess.run('cls')
        # Banks offer = shuffle_cases[value] / cases_left
        total_money_left = 0
        for key, value in shuffle_cases.items():
            if key in cases_left:
                total_money_left = value + total_money_left
        banks_offer = int(total_money_left / ((len(cases_left)) * 0.8))
        print("\nMoney Left: ", *cases.values())
        print("Cases Left to open: ", *cases_left)
        print(f"\n${banks_offer}")
        while True:
            try:
                user_input = input("Do you accept the banks offer? yes/no\n").lower()
                if user_input == "yes" or user_input == "y":
                    user_input_yes = "yes"
                    interation += 6
                    break
                else:
                    interation += 1
                    break
            except ValueError:
                print("Please enter a valid string")
                continue
    last_cases = cases_left
    return last_cases, user_input_yes, banks_offer



def double_or_nothing(user_case, shuffle_cases, user_input_yes, banks_offer):
    try:
        subprocess.run('clear')
    except:
        subprocess.run('cls')
    for key, value in shuffle_cases.items():
        if key == user_case:
            user_case_value = value
            break
    else:
        print("code error")
    try:
        if user_input_yes == "yes":
            print(f"\nBank wishes make you one last offer\n You can accept: ${int(banks_offer)}\n\nOr Risk it all for a chance to win ${int     (banks_offer) * 2}")
            double_chance = input(" What Do You CHOOSE:  \n Yes : Risk it all\n No : I'm Happy\n Answer:  ").lower()
            if double_chance == "y" or double_chance == "yes":
                print("\n   [1]      [2]    \n\n You have a 50/50 Chance of doubling your money")
                while True:
                    try:
                        case_choice = int(input("\nPlease Select your between case 1 and case 2   "))
                        if case_choice <= 2 and user_case >= 1:
                            break
                        else:
                            print("Please choose a between case 1 and case 2")
                            continue
                    except ValueError:
                        print("Please enter an integer")
                        continue
                money = [banks_offer, (banks_offer * 2)]
                print(f"Congratulations you Won ${random.sample(money, k=1)}!!")
                play_again = input("Would you like to play again?  ")
            else:
                print(f"Congratulations you won ${banks_offer}")
                play_again = input("Would you like to play again?  ")
        else:
            print(f"Congratulations you won ${user_case_value}")
            play_again = input("Would you like to play again?  ")
    except:
        return play_again

                
    
def game_finish(play_again):
    try:
        if play_again == "yes" or play_again == "y":
            return True
    except:
        exit = input("Thanks for playing, Press any key to exit...  ")
        return False


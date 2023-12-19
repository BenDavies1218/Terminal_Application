import random
import csv
from colored import fg, attr, bg 
import subprocess
import math
import sys

file = "gamelog.csv"


color_heading: str = f"{attr(1)}{fg(4)}"
color_text: str = f"{attr(3)}{fg(15)}"
color_your_case: str = f"{attr(3)}{fg(1)}"
color_cases_left: str = f"{attr(3)}{fg(11)}"
color_money_left: str = f"{attr(1)}{fg(10)}"
color_input_error: str = f"{attr(4)}{fg(1)}"
color_winnings: str = f"{attr(9)}{fg(220)}"

def game_menu():
        # clears the screen
    try:
        subprocess.run('clear')
    except:
        subprocess.run('cls')
    print(f"{color_heading}Welcome to Deal or No Deal Will you take home the top prize?{attr('reset')}")
    start_game = input(f"\n{color_heading}press any button to start... ")
    while True:
        try:
            name = input(f"\n{color_text}Please enter your name:  {attr('reset')}")
            if all(letter.isalpha() or letter.isspace() for letter in name):
                break
            else:
                print(f"\n{color_input_error}Invalid name please try again{attr('reset')}")
        except TypeError:
            print(f"{color_input_error}Error in name variable{attr('reset')}")
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
            user_case = int(input(f"\n{color_text}Please Select your lucky case:  {attr('reset')}"))
            if user_case <= 22 and user_case >= 1:
                break
            else:
                print(f"{color_input_error}Please choose a case between 1-22{attr('reset')}")
                continue
        except ValueError:
            print(f"{color_input_error}Please enter an integer{attr('reset')}")
            continue
    # remove selected case from cases_left
    for case in cases_left:
        if user_case == case:
            cases_left.remove(case)
            break
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["Users_case", user_case])
        writer.writerow(["case_removed", user_case])
    # return selected case back to main
    return user_case, cases_left
    



def game(cases, shuffle_cases, cases_left, user_case):
    interation = 0
    while interation < 6:
        count = 6 - int(interation)
    # while loop check if count =< 0
        while count != 0:
            # clears the screen
            try:
                subprocess.run('clear')
            except:
                subprocess.run('cls')
        # print cases_left to user
            print(f"\n{color_text}Money Left:{attr('reset')}", color_money_left, *cases.values(), attr('reset'))
            print(f"\n{color_text}Cases Left to open: {attr('reset')}", color_cases_left, *cases_left , attr('reset'))
            print(f"\n{color_text}Your Lucky Case Is:  {attr('reset')}", color_your_case, [user_case], attr('reset'))
            try:
                print(f"{color_text}The last Case opened: No. {rm_case} contained: ${rm_value}{attr('reset')}")
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
        # Calculates the Median Square Root
        banks_offer = math.sqrt(total_money_left**2 / len(cases_left))
        with open(file, "a") as f:
                writer = csv.writer(f)
                writer.writerow(["Bank Offer", (interation + 1), int(banks_offer)])
        print("\nMoney Left: ", *cases.values())
        print("Cases Left to open: ", *cases_left)
        print(f"\nYour Lucky Case Is:  {user_case}")
        # Prints last case value to user
        try:
            print(f"\nThe last Case opened: No. {rm_case} contained: ${rm_value}")
        except:
            print("")
        # prints bank offer
        print(f"\nThe Bank is willing to offer you ${int(banks_offer)}")
        while True:
            try:
                user_input = input("\nDo you accept this offer?:  ")
                if all(letter.isalpha() or letter.isspace() for letter in user_input):
                    break
                else:
                    print("\n Invalid input please try again")
            except TypeError:
                print("Error in user_input variable")
        if user_input == "yes" or user_input == "y":
            with open(file, "a") as f:
                writer = csv.writer(f)
                writer.writerow(["Bank Offer Accepted"])
            user_input_yes = "yes"
            interation = 6
        else:
            with open(file, "a") as f:
                writer = csv.writer(f)
                writer.writerow(["Bank Offer Declined"])
            user_input_yes = "no"
            interation += 1
        try:
            if len(cases_left) == 1:
                interation += 6
                user_input_yes = "yes"
        except:
            continue
    return user_input_yes, banks_offer, total_money_left



def double_or_nothing(user_case, shuffle_cases, user_input_yes, banks_offer):
    try:
        subprocess.run('clear')
    except:
        subprocess.run('cls')
    for key, value in shuffle_cases.items():
        if key == user_case:
            user_case_value = value
            break
    try:
        if user_input_yes == "yes":
            print(f"\n The bank wishes to make you one last offer\n You can accept: ${int(banks_offer)}\n\nOr Risk it all for a chance to win ${int     (banks_offer) * 2}")
            double_chance = input(" What Do You CHOOSE:  \n\n Yes : Risk it all\n No : I'm Happy\n\n Answer:  ").lower()
            if double_chance == "y" or double_chance == "yes":
                with open(file, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Double or nothing offer Accepted"])
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
                money = [0, (banks_offer * 2)]
                winnings = int(random.choice(money))
                print(f"Congratulations you Won ${winnings}!!")
                with open(file, "a") as f:
                    writer = csv.writer(f)
                    if winnings > banks_offer:
                        writer.writerow(["Won Double YAY!"])
                    else:
                        writer.writerow(["Walking away with nothing"])
                play_again = input("Would you like to play again?  ").lower()
            else:
                print(f"Congratulations you won ${banks_offer}")
                play_again = input("Would you like to play again?  ").lower()
                with open(file, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Double or nothing Declined"])
                    writer.writerow(["won", banks_offer])
        else:
            print(f"Congratulations your case {user_case} contained ${user_case_value}")
            play_again = input("Would you like to play again?  ").lower()
            with open(file, "a") as f:
                writer = csv.writer(f)
                writer.writerow(["won", user_case_value])
    except:
        print(f"Congratulations your case {user_case} contained ${user_case_value}")
        play_again = input("Would you like to play again?  ").lower()
        with open(file, "a") as f:
            writer = csv.writer(f)
            writer.writerow(["won", user_case_value])
    return play_again

                
    
def game_finish(play_again):
    if play_again == "yes" or play_again == "y":
        exit = False
        with open(file, "a") as f:
            writer = csv.writer(f)
            writer.writerow(["User playing again"])
    else:
        input("Thanks for playing, Press any key to exit...  ")
        exit = True
        with open(file, "a") as f:
            writer = csv.writer(f)
            writer.writerow(["User exiting application"])
    return exit



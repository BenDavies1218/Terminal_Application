import random
import csv
from colored import foreground, attributes, background 
import sys, subprocess

cases_left = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22]

file = "gamelog.csv"

def game_menu():
        # clears the screen
    try:
        subprocess.run('clear')
    except:
        subprocess.run('cls')
    print("Welcome to Deal or No Deal Will you be a millionaire?")
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
        if case == user_case:
            cases_left.remove(case)
            break
        else:
            continue
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
            # Checks if theres more than one case
            if cases_left[1] == True:
                break
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
        banks_offer = int(total_money_left / len(cases_left))
        print("\nMoney Left: ", *cases.values())
        print("Cases Left to open: ", *cases_left)
        print(f"\n${banks_offer}")
        user_input = input("Do you accept the banks offer? yes/no\n")
        if user_input.lower() == "yes" or "y":
            user_input_yes = True
            interation += 7
        else:
            interation += 1
    last_case = cases_left
    return last_case, user_input_yes, banks_offer

def double_or_nothing(user_case, shuffle_cases, last_case, user_input_yes, banks_offer):
    try:
        subprocess.run('clear')
    except:
        subprocess.run('cls')
    if user_input_yes != True:
        for key, value in shuffle_cases.items():
            if key == user_case:
                user_case_value = value
                break
            else:
                continue
        print(f"\nBank wishes make you one last offer\n You can accept: ${int(user_case_value)}\n Or Risk it all for a chance to win ${int(user_case_value) * 2}")
        double_chance = input("What Do You CHOOSE:  yes/no\n")   

    

def game_finish(cases_left, shuffle_cases, user_case):
    pass

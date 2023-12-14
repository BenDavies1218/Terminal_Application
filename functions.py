import random
import csv
from colored import fg, attr, bg, fore
import sys, subprocess

file = "gamelog.csv"

def game_menu():
    print("Welcome to Deal or No Deal Will you be a millionaire")
    start_game = input("press any button to start")
    while True:
        try:
            name = input("\n Please enter your name:  ")
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

def select_case(cases_left):
    # print cases left to user
    print(cases_left)
    # user will input a number between and including 1-23
    while True:
        try:
            user_case = int(input("Please Select your lucky case:  "))
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

def game(cases, shuffle_cases, cases_left, user_case, interation):
    count = 6 - int(interation)
    print(count)
    # while loop check if count =< 0
    while count != 0:
        # Checks if theres more than one case
        try:
            cases_left[1]
        except:
            break
        # clears the screen
        try:
            subprocess.run('clear')
        except:
            subprocess.run('cls')
    # print cases_left to user
        print("\nMoney Left: ", *cases.values())
        print("Cases Left: ", *cases_left)
        print(f"\nYour Lucky Case Is:  {user_case}")
        try:
            print(f"Case {rm_case} contained: ${rm_value}")
        except:
            print("")
        # ask user to enter a case to be removed
        tobe_removed = int(input("\nPlease select a Case to be removed:  "))
        # remove case from cases left
        for case in cases_left:
            if case == tobe_removed:
                rm_case = case
                cases_left.remove(case)
                break
            else:
                continue
        for key, value in shuffle_cases.items():
            if key == tobe_removed:
                rm_value = value
                break
            else:
                continue
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
    return cases, shuffle_cases, cases_left, user_case, interation

    # prompt user to enter input 
    # loop to check if input is in cases left
    # 

def banker_offer(cases_left, shuffle_cases):
    pass
    # 

def double_or_nothing(user_case, shuffle_cases):
    pass

def game_finish(cases_left, shuffle_cases, user_case):
    pass

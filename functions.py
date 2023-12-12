import random
import csv
from colored import fg, attr, bg 


file = "gamelog.csv"

def game_menu():
    print("Welcome to Deal or No Deal Will you be a millionaire")
    start_game = input("press any button to start")
    name = input("\n Please enter your name:  ")
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["Player", name])

def shuffler(cases):
    values = list(cases.values())
    shuffle_list = random.sample(values, len(values))
    shuffle_cases = dict(zip(cases.keys(), shuffle_list))
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["cases shuffled = True"])
    return shuffle_cases

def select_case(cases_left):
    pass
    # print cases left to user
    print(cases_left)
    # user will input a number between and including 1-22
    while True:
        try:
            user_case = int(input("Please Select your lucky case:  "))
            if user_case <= 22 and user_case >= 1:
                break
            else:
                print("Please choose a case between 1-22")
                continue
        except:
            print("Please enter an integer")
            continue
    # remove selected case from cases_left
    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["Users_choice", user_case])
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

def game(shuffle_cases, cases_left, user_case, count):
    pass
    # loop to remove selected case from cases_left list
    # while loop check if count =< 0
    # print cases_left to user
    # prompt user to enter input 
    # loop to check if input is in cases left
    # 

def banker_offer(cases_left, shuffle_cases):
    pass
    # 

def double_or_nothing():
    pass

def game_finish(cases_left):
    pass
    # if cases left < 2 return True else False

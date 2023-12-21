import random
import csv
from colored import fg, attr, bg
import subprocess
import math
import pytest


class InputIsEmptyError(Exception):
    pass


class InvalidNameError(Exception):
    pass


file = "gamelog.csv"


color_heading: str = f"{attr(1)}{fg(4)}"
color_text: str = f"{attr(3)}{fg(15)}"
color_your_case: str = f"{attr(3)}{fg(188)}"
color_cases_left: str = f"{attr(3)}{fg(11)}"
color_money_left: str = f"{attr(1)}{fg(10)}"
color_input_error: str = f"{attr(4)}{fg(1)}"
color_winnings: str = f"{attr(3)}{fg(220)}"


def game_menu():
    # clears the screen
    try:
        subprocess.run("clear")
    except:
        subprocess.run("cls")
    print(
        f"{color_heading}Welcome to Deal or No Deal Will you take home the top prize?{attr('reset')}"
    )
    start_game = input(
        f"\n{color_heading}Press H to view the game rules\n\nPress any other button to start the game... {attr('reset')}"
    )
    if start_game.lower() == "h":
        start_game()
    while True:
        try:
            name = input(f"\n{color_text}Please enter your name:  {attr('reset')}")
            if len(name) > 0:
                if all(letter.isalpha() or letter.isspace() for letter in name):
                    break
                raise InvalidNameError("Invalid characters")
            raise InputIsEmptyError("Empty String")

        except InvalidNameError:
            print(
                f"\n{color_input_error}Your name can only contain characters from a-z{attr('reset')}"
            )
        except InputIsEmptyError:
            print(
                f"\n{color_input_error}Your name must contain at least 1 character{attr('reset')}"
            )
        except Exception as e:
            print(f"{color_input_error}{e}{attr('reset')}")

    with open(file, "a") as f:
        writer = csv.writer(f)
        writer.writerow(["Player", name])


def game_help():
    print(f"{color_heading}Welcome to Deal or No Deal Rules{attr('reset')}")
    print()


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
    cases_left = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
    ]
    # print cases left to user
    try:
        subprocess.run("clear")
    except:
        subprocess.run("cls")
    print(color_cases_left, *cases_left, attr("reset"))
    # user will input a number between and including 1-22
    while True:
        try:
            user_case = int(
                input(f"\n{color_text}Please Select your lucky case:  {attr('reset')}")
            )
            if user_case <= 22 and user_case >= 1:
                break
            else:
                print(
                    f"{color_input_error}Please choose a case between 1-22{attr('reset')}"
                )
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


def banker_offer(nums, nums_left):
    # Median square root calculator
    # Banks offer = shuffle_cases[value] / cases_left
    total_money_left = 0
    for key, value in nums.items():
        if key in nums_left:
            total_money_left = value + total_money_left
    if len(nums_left) == 1:
        offer = total_money_left / 2
    else:
        offer = (math.sqrt(total_money_left**2)) / len(nums_left)
    return offer


def game(cases, shuffle_cases, cases_left, user_case):
    interation = 0
    while interation < 6:
        count = 6 - int(interation)
        # while loop check if count =< 0
        while count != 0:
            # clears the screen
            try:
                subprocess.run("clear")
            except:
                subprocess.run("cls")
            # print cases_left to user
            print(
                f"\n{color_text}Money Left:{attr('reset')}",
                color_money_left,
                *cases.values(),
                attr("reset"),
            )
            print(
                f"\n{color_text}Cases Left to open: {attr('reset')}",
                color_cases_left,
                *cases_left,
                attr("reset"),
            )
            print(
                f"\n{color_text}Your Lucky Case Is:  {attr('reset')}",
                color_your_case,
                [user_case],
                attr("reset"),
            )
            try:
                print(
                    f"{color_text}The last Case opened: No. ",
                    color_cases_left,
                    rm_case,
                    attr("reset"),
                    f"{color_text}contained: {attr('reset')}",
                    color_money_left,
                    "$",
                    rm_value,
                    attr("reset"),
                )
            except:
                print("")
            print(f"{color_text}Next bank offer in: {count} cases{attr('reset')}")
            # ask user to enter a case to be removed
            while True:
                try:
                    tobe_removed = int(
                        input(f"\n{color_text}Please select a Case to be removed:  ")
                    )
                    if tobe_removed in cases_left:
                        break
                    else:
                        print(
                            color_input_error,
                            "Please enter a number from the list of cases left to open",
                            attr("reset"),
                        )
                except ValueError:
                    print(
                        color_input_error, "Please enter a valid integer", attr("reset")
                    )
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
            subprocess.run("clear")
        except:
            subprocess.run("cls")
        # Calculates the Median Square Root
        banks_offer = banker_offer(shuffle_cases, cases_left)
        with open(file, "a") as f:
            writer = csv.writer(f)
            writer.writerow(["Bank Offer", (interation + 1), int(banks_offer)])
        print(
            f"\n{color_text}Money Left:{attr('reset')}",
            color_money_left,
            *cases.values(),
            attr("reset"),
        )
        print(
            f"\n{color_text}Cases Left to open: {attr('reset')}",
            color_cases_left,
            *cases_left,
            attr("reset"),
        )
        print(
            f"\n{color_text}Your Lucky Case Is:  {attr('reset')}",
            color_your_case,
            [user_case],
            attr("reset"),
        )
        try:
            print(
                f"{color_text}The last Case opened: No. ",
                color_cases_left,
                rm_case,
                attr("reset"),
                f"{color_text}contained: {attr('reset')}",
                color_money_left,
                "$",
                rm_value,
                attr("reset"),
            )
        except:
            print("")
        # prints bank offer
        print(
            f"\n{color_text}The Bank is willing to offer you{attr('reset')}",
            color_money_left,
            "$",
            int(banks_offer),
            attr("reset"),
        )
        while True:
            try:
                user_input = input(
                    f"{color_text}\nDo you accept this offer?: {attr('reset')}"
                )
                if len(user_input) > 0:
                    if all(
                        letter.isalpha() or letter.isspace() for letter in user_input
                    ):
                        if "y" or "yes" or "n" or "no" == user_input.lower():
                            break
                        else:
                            print("Enter yes or no")
                    raise InvalidNameError("invalid string")
                else:
                    print(
                        color_input_error,
                        "\nInvalid input please try again",
                        attr("reset"),
                    )
            except TypeError:
                print(color_input_error, "Error in user input variable", attr("reset"))
            except InvalidNameError:
                print(
                    color_input_error,
                    "Invalid String Please only enter characters from A-Z",
                    attr("reset"),
                )
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
    return user_input_yes, banks_offer


def double_or_nothing(user_case, shuffle_cases, user_input_yes, banks_offer):
    try:
        subprocess.run("clear")
    except:
        subprocess.run("cls")
    for key, value in shuffle_cases.items():
        if key == user_case:
            user_case_value = value
            break
    try:
        if user_input_yes == "yes":
            print(
                f"\n{color_text} The bank wishes to make you one last offer\n You can accept: {attr('reset')}",
                color_money_left,
                "$",
                int(banks_offer),
                attr("reset"),
                "\n\nOr Risk it all for a chance to win ",
                color_money_left,
                "$",
                (int(banks_offer) * 2),
                attr("reset"),
            )
            double_chance = input(
                f"{color_text} What Do You CHOOSE:  \n\n Yes : Risk it all\n No : I'm Happy\n\n Answer:  {attr('reset')}"
            ).lower()
            if double_chance == "y" or double_chance == "yes":
                with open(file, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Double or nothing offer Accepted"])
                print(
                    f"\n{color_cases_left}   [1]      [2]    {attr('reset')}\n\n {color_text}You have a 50/50 Chance of doubling your money{attr('reset')}"
                )
                while True:
                    try:
                        case_choice = int(
                            input(
                                f"\n{color_text}Please Select your between case 1 and case 2   {attr('reset')}"
                            )
                        )
                        if case_choice <= 2 and user_case >= 1:
                            break
                        else:
                            print(
                                f"{color_input_error}Please choose a between case 1 and case 2{attr('reset')}"
                            )
                            continue
                    except ValueError:
                        print(
                            f"{color_input_error}Please enter an integer{attr('reset')}"
                        )
                        continue
                money = [0, (banks_offer * 2)]
                winnings = int(random.choice(money))
                print(
                    f"{color_winnings}Congratulations you Won {attr('reset')}{color_money_left}${winnings}{attr('reset')}"
                )
                with open(file, "a") as f:
                    writer = csv.writer(f)
                    if winnings > banks_offer:
                        writer.writerow(["Won Double YAY!"])
                    else:
                        writer.writerow(["Walking away with nothing"])
                play_again = input(
                    f"{color_text}Would you like to play again?  {attr('reset')}"
                ).lower()
            else:
                print(
                    f"{color_winnings}Congratulations you won {attr('reset')}{color_money_left}${banks_offer}{attr('reset')}"
                )
                play_again = input(
                    f"{color_text}Would you like to play again?  {attr('reset')}"
                ).lower()
                with open(file, "a") as f:
                    writer = csv.writer(f)
                    writer.writerow(["Double or nothing Declined"])
                    writer.writerow(["won", banks_offer])
        else:
            print(
                f"{color_text}Congratulations your case {attr('reset')}{color_your_case}{user_case} {attr('reset')}{color_text}contained{attr('reset')}{color_money_left} ${user_case_value}{attr('reset')}"
            )
            play_again = input(
                f"{color_text}Would you like to play again?  {attr('reset')}"
            ).lower()
            with open(file, "a") as f:
                writer = csv.writer(f)
                writer.writerow(["won", user_case_value])
    except:
        print(
            f"{color_text}Congratulations your case {attr('reset')}{color_your_case}{user_case} {attr('reset')}{color_text}contained{attr('reset')}{color_money_left} ${user_case_value}{attr('reset')}"
        )
        play_again = input(
            f"{color_text}Would you like to play again?  {attr('reset')}"
        ).lower()
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

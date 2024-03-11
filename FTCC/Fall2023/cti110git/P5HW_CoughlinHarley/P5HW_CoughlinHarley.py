#this program has users add or subtract random numbers
#12/12/23
#CTI-110 P5HW - Math Quiz
#Harley Coughlin
#

import main_menu
import random

def math_man(option):
    num1 = random.randint(1, 300)
    num2 = random.randint(1,300)
    
    if option == 1:
        mathed = num1 + num2
        print(f"{num1:>5}\n+ {num2:>3}\n\n")
    else:
        mathed = num1 - num2
        print(f"{num1:>5}\n- {num2:>3}\n\n")

    num_guesses = 0
    retry = True
    while (retry):
        if num_guesses == 0:
            user_input = int(input("Enter answer: "))
            print()
        else:
            user_input = int(input("Try again: "))
            print()

        num_guesses += 1
        retry = check(user_input, mathed)
    
    print(f"Number of guesses: {num_guesses}\n")


def check(user_input, answer):
    if (user_input < answer):
        print("Sorry, guess is too low.\n")
        return True
    elif (user_input == answer):
        print("Congratulations!!!! Your answer is correct.\n")
        return False
    elif (user_input > answer):
        print("Sorry, guess is too high.\n")
        return True

math_man(main_menu.main_menu())

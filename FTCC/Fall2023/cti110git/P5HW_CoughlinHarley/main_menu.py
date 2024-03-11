def main_menu():

    print("Welcome to the Math Quiz\n\n\n\n")

    keep_going = True
    while (keep_going):
        print("MAIN MENU")
        print("-----------------------------")
        print("1. Adding Random Numbers")
        print("2. Subtracting Random Numbers")
        print("3. Exit\n")

        option = int(input("Please choose one of the menu options: "))

        if (option == 1 or option == 2):
            return option
        elif (option == 3):
            print("Thank you for playing")
            keep_going = False
        else:
            print("Please enter a valid choice.\n")
            continue


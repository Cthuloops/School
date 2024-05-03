# this program performs operations on a list of objects
# 05/03/2024
# Final project for CSC121
# Harley Coughlin

import final_project_functions as fpf


def main_menu():
    print()
    print(f"{'Main Menu':^55}")
    print(f"{'':-^55}")
    print("1) Read Student Info and Create Class Objects/Instances")
    print("2) Add a New Student Record")
    print("3) Delete a Student Record (set to inactive)")
    print("4) Search for Student by Last Name")
    print("5) Search for Student by ID")
    print("6) Exit")
    print(f"{'':-^55}")


def get_option():
    option_not_valid = True
    while option_not_valid:
        option = input("Please select an option: ")
        try:
            option = int(option)
            if option in range(1, 7):
                return option
        except ValueError:
            print("Please enter a valid integer.\n")
            continue
        except Exception as err:
            print("Something went wrong: " + str(err))
            continue


def main():
    keep_going = True
    while keep_going:
        main_menu()
        option = get_option()
        if option == 1:
            student_list = fpf.read_content()
        elif option == 6:
            keep_going = False


if __name__ == "__main__":
    main()

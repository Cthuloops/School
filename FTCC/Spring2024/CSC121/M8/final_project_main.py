# this program performs operations on a list of objects
# 05/03/2024
# Final project for CSC121
# Harley Coughlin

import final_project_functions as fpf


def main_menu():
    """Prints the progams main menu"""
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
    # while loop for getting the input
    option_not_valid = True
    while option_not_valid:
        # prompt user for a selection
        option = input("Please select an option: ")
        # check if the input is an int and within range of available options
        try:
            option = int(option)
            if option in range(1, 7):
                return option
            else:
                print("Please enter a valid menu choice (1 - 6)")
                main_menu()
                continue
        except ValueError:
            print("Please enter a valid integer.")
            main_menu()
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
            fpf.write_report(student_list)
        elif option == 2:
            student_list = fpf.add_student_record(fpf.read_content())
            if student_list is None:
                continue
            fpf.write_report(student_list)
        elif option == 6:
            keep_going = False


if __name__ == "__main__":
    main()

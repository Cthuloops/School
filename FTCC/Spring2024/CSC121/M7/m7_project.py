# this program runs functions on list of dicts, feat OOP
# 04/28/2024
# CSC121 M7Project OOP
# Harley Coughlin


import m7_functions as m7fun
import csv

# initializing the dict list (20 dicts)
student_registry = [{"student_id": "12376", "first_name": "Michael", "last_name": "Anderson", "major": "mech", "courses": ["mat143-quantitative literacy", "com120-intro interpersonal communication", "elc228-plc applications", "bpr115-electric/fluid power diagrams"]},

                    {"student_id": "12415", "first_name": "Andrew", "last_name": "Jackson", "major": "UI/UX", "courses": ["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "DME110-Intro to Digital Media", "DME115-Graphic Design Tools"]},

                    {"student_id": "12302", "first_name": "Michelle", "last_name": "Robinson", "major": "UI/UX", "courses": ["ENG111-Writing and Inquiry", "MAT143-Quantitative Literacy", "DME115-Graphic Design Tools", "WEB110-Internet/Web Fundamentals"]},

                    {"student_id": "12252", "first_name": "Carol", "last_name": "Flores", "major": "Mech", "courses": ["ENG111-Writing", "COM120-Intro Interpersonal Communication", "MAT143-Quantitative Literacy", "ELC228-PLC Applications"]},

                    {"student_id": "12338", "first_name": "George", "last_name": "Brown", "major": "UI/UX", "courses": ["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "DME110-Intro to Digital Media", "DME115-Graphic Design Tools"]},

                    {"student_id": "12556", "first_name": "Ronald", "last_name": "Harris", "major": "Mech", "courses": ["COM120-Intro Interpersonal Communication", "ENG114-Prof Research & Reporting", "BPR115-Electric/Fluid Power Diagrams", "HYD110-Hydraulics/Pneumatics I"]},

                    {"student_id": "12645", "first_name": "Rebecca", "last_name": "Mitchell", "major": "Network", "courses": ["ENG111-Writing and Inquiry", "MAT143-Quantitative Literacy", "NOS120-Linux/UNIX Single User", "NOS230-Windows Administration I"]},

                    {"student_id": "12046", "first_name": "Nicholas", "last_name": "Garcia", "major": "Programming", "courses": ["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "CSC121-Python Programming", "CSC151-Java Programming"]},

                    {"student_id": "12082", "first_name": "Brandon", "last_name": "Adams", "major": "Programming", "courses": ["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "CSC121-Python Programming", "CSC151-Java Programming"]},

                    {"student_id": "12366", "first_name": "Debra", "last_name": "Martinez", "major": "UI/UX", "courses": ["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "DME110-Intro to Digital Media", "DME115-Graphic Design Tools"]},

                    {"student_id": "12011", "first_name": "Rachel", "last_name": "Rivera", "major": "Programming", "courses": ["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "CSC121-Python Programming", "CSC151-Java Programming"]},

                    {"student_id": "12116", "first_name": "Diane", "last_name": "Clark", "major": "Network", "courses": ["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "CTS120-Hardware/Software Support", "NOS120-Linux/UNIX Single User"]},

                    {"student_id": "12481", "first_name": "Jose", "last_name": "Lewis", "major": "UI/UX", "courses": ["ENG111-Writing and Inquiry", "COM120-Intro Interpersonal Communication", "DME115-Graphic Design Tools", "CTS115-Information Systems Business Concepts"]},

                    {"student_id": "12931", "first_name": "Victoria", "last_name": "Wright", "major": "Mech", "courses": ["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "ELC112-DC/AC Electricity", "ELC117-Motors & Controls"]},

                    {"student_id": "12283", "first_name": "Henry", "last_name": "Scott", "major": "Mech", "courses": ["MAT143-Quantitative Literacy", "PSY150-General Psychology", "ELC228-PLC Applications", "ISC112-Industrial Safety"]},

                    {"student_id": "12212", "first_name": "Peter", "last_name": "Carter", "major": "Network", "courses": ["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "CTS120-Hardware/Software Support", "NOS120-Linux/UNIX Single User"]},

                    {"student_id": "12018", "first_name": "Evelyn", "last_name": "Wilson", "major": "Mech", "courses": ["PSY150-General Psychology", "COM120-Intro Interpersonal Communication", "ISC112-Industrial Safety", "BPR115-Electric/Fluid Power Diagrams"]},

                    {"student_id": "12165", "first_name": "Austin", "last_name": "Thompson", "major": "Programming", "courses": ["MAT143-Quantitative Literacy", "PSY150-General Psychology", "DBA110-Database Concepts", "DBA120-Database Programming I"]},

                    {"student_id": "12548", "first_name": "Teresa", "last_name": "Martin", "major": "Mech", "courses": ["ACA122-College Transfer Success", "PSY150-General Psychology", "ELC112-DC/AC Electricity", "ISC112-Industrial Safety"]},

                    {"student_id": "12181", "first_name": "Randy", "last_name": "Lopez", "major": "Mech", "courses": ["MAT143-Quantitative Literacy", "PSY150-General Psychology", "ELC228-PLC Applications", "ISC112-Industrial Safety"]}
                    ]


# menu for the progam
def menu():
    print()
    print("Menu------------------------")
    print("1) Display Registry Content")
    print("2) Display Course Roster")
    print("3) List of Students by Major")
    print("4) Student Search by Id")
    print("5) Exit")
    print("----------------------------\n")


# get int input, otherwise reprompt
def get_input():
    valid_option = False
    # loop to obtain input
    while (not valid_option):
        # capturing input as string so no error on incorrect input type
        option = input("Choose an option: ")
        print()
        # checking if string is only digits, otherwise reprompt
        if option.isnumeric():
            # converting option into int
            option = int(option)
            # checking if input is in range of menu options
            if option in range(1, 6):
                valid_option = True
            else:
                print("Invalid option please try again.\n")
        else:
            print("Invalid option please try again.\n")
    return option


# main, calls menu and functions
def main():
    # I know the assignment says to call this for each option but that seems
    # just a bit excessive to me. so call create instance at the start of main
    # and pass the list to all the functions
    student_list = m7fun.create_instances(student_registry)

    keep_going = True
    while (keep_going):
        # print the menu before choosing option and after choosing an option except exit
        menu()
        option = get_input()
        # calls functions depending on the option chosen
        if option == 1:
            # write the list to a file
            m7fun.write_instances(student_list)
            # display the contents of the list
            m7fun.display_registry_content(student_list)
        elif option == 2:
            # displays the student information for a course
            m7fun.display_course_roster(student_list)
        elif option == 3:
            # list of student for a major
            m7fun.list_by_major(student_list)
        elif option == 4:
            # student associated w/ an id
            m7fun.search_by_id(student_list)
        elif option == 5:
            print("Progam will now exit")
            keep_going = False


if __name__ == "__main__":
    main()

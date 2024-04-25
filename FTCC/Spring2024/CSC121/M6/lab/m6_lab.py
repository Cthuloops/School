# this program is a continuation of M4 project and performs functions on a list of dicts
# 04/13/2024
# CSC121 M6Lab
# Harley Coughlin

import m6_functions as m6fun

# initializing the dict list (20 dicts)
student_registry = [{"stu_id":"12376", "first_name":"Michael", "last_name":"Anderson", "major":"Mech", "courses":["MAT143-Quantitative Literacy", "COM120-Intro Interpersonal Communication", "ELC228-PLC Applications", "BPR115-Electric/Fluid Power Diagrams"]},

                    {"stu_id":"12415", "first_name":"Andrew", "last_name":"Jackson", "major":"UI/UX", "courses":["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "DME110-Intro to Digital Media", "DME115-Graphic Design Tools"]},

                    {"stu_id":"12302", "first_name":"Michelle", "last_name":"Robinson", "major":"UI/UX", "courses":["ENG111-Writing and Inquiry", "MAT143-Quantitative Literacy", "DME115-Graphic Design Tools", "WEB110-Internet/Web Fundamentals"]},

                    {"stu_id":"12252", "first_name":"Carol", "last_name":"Flores", "major":"Mech", "courses":["ENG111-Writing", "COM120-Intro Interpersonal Communication", "MAT143-Quantitative Literacy", "ELC228-PLC Applications"]},

                    {"stu_id":"12338", "first_name":"George", "last_name":"Brown", "major":"UI/UX", "courses":["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "DME110-Intro to Digital Media", "DME115-Graphic Design Tools"]},

                    {"stu_id":"12556", "first_name":"Ronald", "last_name":"Harris", "major":"Mech", "courses":["COM120-Intro Interpersonal Communication", "ENG114-Prof Research & Reporting", "BPR115-Electric/Fluid Power Diagrams", "HYD110-Hydraulics/Pneumatics I"]},

                    {"stu_id":"12645", "first_name":"Rebecca", "last_name":"Mitchell", "major":"Network", "courses":["ENG111-Writing and Inquiry", "MAT143-Quantitative Literacy", "NOS120-Linux/UNIX Single User", "NOS230-Windows Administration I"]},

                    {"stu_id":"12046", "first_name":"Nicholas", "last_name":"Garcia", "major":"Programming", "courses":["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "CSC121-Python Programming", "CSC151-Java Programming"]},

                    {"stu_id":"12082", "first_name":"Brandon", "last_name":"Adams", "major":"Programming", "courses":["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "CSC121-Python Programming", "CSC151-Java Programming"]},

                    {"stu_id":"12366", "first_name":"Debra", "last_name":"Martinez", "major":"UI/UX", "courses":["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "DME110-Intro to Digital Media", "DME115-Graphic Design Tools"]},

                    {"stu_id":"12011", "first_name":"Rachel", "last_name":"Rivera", "major":"Programming", "courses":["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "CSC121-Python Programming", "CSC151-Java Programming"]},

                    {"stu_id":"12116", "first_name":"Diane", "last_name":"Clark", "major":"Network", "courses":["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "CTS120-Hardware/Software Support", "NOS120-Linux/UNIX Single User"]},

                    {"stu_id":"12481", "first_name":"Jose", "last_name":"Lewis", "major":"UI/UX", "courses":["ENG111-Writing and Inquiry", "COM120-Intro Interpersonal Communication", "DME115-Graphic Design Tools", "CTS115-Information Systems Business Concepts"]},

                    {"stu_id":"12931", "first_name":"Victoria", "last_name":"Wright", "major":"Mech", "courses":["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "ELC112-DC/AC Electricity", "ELC117-Motors & Controls"]},

                    {"stu_id":"12283", "first_name":"Henry", "last_name":"Scott", "major":"Mech", "courses":["MAT143-Quantitative Literacy", "PSY150-General Psychology", "ELC228-PLC Applications", "ISC112-Industrial Safety"]},

                    {"stu_id":"12212", "first_name":"Peter", "last_name":"Carter", "major":"Network", "courses":["ACA122-College Transfer Success", "ENG111-Writing and Inquiry", "CTS120-Hardware/Software Support", "NOS120-Linux/UNIX Single User"]},

                    {"stu_id":"12018", "first_name":"Evelyn", "last_name":"Wilson", "major":"Mech", "courses":["PSY150-General Psychology", "COM120-Intro Interpersonal Communication", "ISC112-Industrial Safety", "BPR115-Electric/Fluid Power Diagrams"]},

                    {"stu_id":"12165", "first_name":"Austin", "last_name":"Thompson", "major":"Programming", "courses":["MAT143-Quantitative Literacy", "PSY150-General Psychology", "DBA110-Database Concepts", "DBA120-Database Programming I"]},

                    {"stu_id":"12548", "first_name":"Teresa", "last_name":"Martin", "major":"Mech", "courses":["ACA122-College Transfer Success", "PSY150-General Psychology", "ELC112-DC/AC Electricity", "ISC112-Industrial Safety"]},

                    {"stu_id":"12181", "first_name":"Randy", "last_name":"Lopez", "major":"Mech", "courses":["MAT143-Quantitative Literacy", "PSY150-General Psychology", "ELC228-PLC Applications", "ISC112-Industrial Safety"]}
                    ]


# menu for the progam
def menu():
    print()
    print(f"{'Menu':-<28}")
    print("1) Display Registry Content")
    print("2) Display Course Roster and Write to CSV")
    print("3) List of Students by Major and Write to CSV")
    print("4) Student Search by Id and Write to CSV")
    print("5) Exit")
    print(f"{'':-<28}\n")


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
    keep_going = True
    while (keep_going):
        # print the menu before choosing option and after choosing an option except exit
        menu()
        option = get_input()

        # calls functions depending on the option chosen
        if option == 1:
            m6fun.display_registry_content(student_registry)

        elif option == 2:
            # calls get_course_code for user input which calls a validation
            # function on the input
            course = m6fun.get_course(student_registry)
            # if the user quits rerun menu
            if course is None:
                continue
            # create the course roster
            course_roster = m6fun.create_course_roster(student_registry, course)
            # display/write the course roster
            m6fun.display_course_roster(course_roster)
            m6fun.write_course_roster_csv(course_roster, course)

        elif option == 3:
            # calls get_major for uesr input
            major = m6fun.get_major(student_registry)
            # if the user quits rerun menu
            if major is None:
                continue
            # create the major list
            major_list = m6fun.create_major_list(student_registry, major)
            # display/write the major list
            m6fun.display_list_by_major(major_list)
            m6fun.write_major_list_csv(major_list, major)

        elif option == 4:
            # get the search id
            student_id = m6fun.get_id(student_registry)
            # if the user quits, rerun menu
            if student_id is None:
                continue
            # isolate the student from the registry
            student = m6fun.create_student_dict(student_registry, student_id)
            # display/write the student
            m6fun.display_student_by_id(student)
            m6fun.create_csv_by_student_id(student, student_id)

        elif option == 5:
            print("Progam will now exit\n")
            keep_going = False


if __name__ == "__main__":
    main()

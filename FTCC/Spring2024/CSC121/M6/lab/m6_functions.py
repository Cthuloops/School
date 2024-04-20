import csv
import re

# global fieldnames
# g_fieldnames = ["stu_id", "first_name", "last_name", "major", "courses"]


# prints each student in the registry and each of their classes
def display_registry_content(student_registry):
    print(f"{'Student ID':<8}{'First Name':<13}{'Last Name':<13}{'Major':<13}{'Course'}")
    print(f"{'':-^87}")
    # accessing dicts in list of dicts
    for student in student_registry:
        # pulling courses per student into it's own list
        courses = student['courses']
        # listing each course for each student and their info
        for course in courses:
            print(f"{student['stu_id']:<8}{student['first_name']:<13}{student['last_name']:<13}{student['major']:<13}{course}")


# check to see if user input is a value in a dict in student_registry
def find_course_in_registry(student_registry, item_to_find):
    for student in student_registry:
        for values in student.values():
            for value in values:
                if value.startswith(item_to_find):
                    return value
    # returns None if the key isn't found
    return None


# get user input for course code
# returns the full course name from student_registry
def get_course(student_registry):
    not_valid = True
    while not_valid:
        # prompt user for input
        print("Please enter course code (ex MAT143) to search for", end=' ')
        course_code = input("or enter q/Q to return to menu: ")
        course = validate_course_code(student_registry, course_code)
        # return to main menu
        if course_code == 'q' or course_code == 'Q':
            not_valid = False
            return None
        elif course is not None:
            not_valid = False
            return course
        else:
            print()
            print("Course not found\n")


# validate course code
def validate_course_code(student_registry, course_code):
    validation = re.search("(^[A-Z]{3}[0-9]{3}$)", course_code)
    if validation is not None:
        course_in_registry = find_course_in_registry(student_registry, course_code)
        if course_in_registry is not None:
            return course_in_registry
    else:
        return None


# creates the course roster, returns a list of dicts
def create_course_roster(student_registry, course):
    course_roster = []
    for student in student_registry:
        if course in student["courses"]:
            course_roster.append(student)
    return course_roster


# pretty prints the course roster
def display_course_roster(course_roster):
    print()
    print(f"{'Student ID':<13}{'First Name':<13}{'Last Name':<13}{'Major':<13}")
    print(f"{'':-^52}")
    for student in course_roster:
        print(f"{student['stu_id']:<13}{student['first_name']:<13}{student['last_name']:<13}{student['major']:<13}")
    print()


# creates csv for the course roster
def write_course_roster_csv(course_roster, course):
    # list for header of csv
    fieldnames = ["stu_id", "first_name", "last_name", "major"]
    # create the name of the file
    filename = course + ".csv"
    # open the file
    print("Now creating CSV")
    try:
        with open(filename, 'w', newline='') as csv_file:
            # create the dictwriter
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(course_roster)
    except Exception as err:
        print()
        print("Something went wrong: " + str(err))


# checks the search items against the student registry
def check_if_in_registry(student_registry, item_to_find, key):
    for student in student_registry:
        if item_to_find in student[key]:
            return True
    return False


# prompt the user for the major they want to search
def get_major(student_registry):
    not_valid = True
    while not_valid:
        # get search term or quit
        search_term = input("Enter major to search for or enter q/Q to quit: ")
        # return to menu
        if search_term == 'q' or search_term == 'Q':
            not_valid = False
            return None
        # check to see if the major exists
        elif check_if_in_registry(student_registry, search_term, "major"):
            return search_term
        else:
            print()
            print("Major not found\n")


# create the list of student in the major searched for
def create_major_list(student_registry, major):
    # list to pack dicts
    major_list = []
    # search through student registry
    for student in student_registry:
        # if the student is in the major
        if major in student['major']:
            # add the dict to the list
            major_list.append(student)
    return major_list


# pretty print the list of students in the major
def display_list_by_major(major_list):
    print()
    print(f"{'Student ID':<13}{'First Name':<13}{'Last Name':<13}")
    print(f"{'':-^39}")
    for student in major_list:
        print(f"{student['stu_id']:<13}{student['first_name']:<13}{student['last_name']:<13}")
    print()


# create the csv for the major list
def write_major_list_csv(major_list, major):
    # list for header of csv
    fieldnames = ["stu_id", "first_name", "last_name"]
    # create the filename
    filename = major + ".csv"
    # open the file
    print("Now creating CSV")
    try:
        with open(filename, 'w', newline='') as csv_file:
            # create the writer
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerows(major_list)
    except Exception as err:
        print()
        print("Something went wrong: " + str(err))


# prompt the user for the user ID they want to find
def get_id(student_registry):
    not_valid = True
    while not_valid:
        # get search id or quit
        search_id = input("Enter ID to search for (ex 12345) or q/Q to quit: ")
        # return to main
        if search_id == 'q' or search_id == 'Q':
            not_valid = False
            return None
        # make sure the search_id is a number
        elif search_id.isdigit() and check_if_in_registry(student_registry, search_id, "stu_id"):
            return search_id
        else:
            print()
            print("ID not found")


# isolate the student from the registry
def create_student_dict(student_registry, student_id):
    for student in student_registry:
        if student_id in student['stu_id']:
            return student


# pretty print the student matching the id
def display_student_by_id(student):
    # print the header
    print()
    print(f"{'Student ID':<13}{'First Name':<13}{'Last Name':<13}{'Major':<13}")
    print(f"{'':-^52}")
    # print the student info
    print(f"{student['stu_id']:<13}{student['first_name']:<13}{student['last_name']:<13}{student['major']:<13}")
    print()


# create the student csv
def create_csv_by_student_id(student, student_id):
    # list for header of csv
    fieldnames = ["stu_id", "first_name", "last_name", "major"]
    # create the name of the file
    filename = student_id + ".csv"
    # open the file
    print("Now creating CSV")
    try:
        with open(filename, 'w', newline='') as csv_file:
            # create the dictwriter
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames, extrasaction='ignore')
            writer.writeheader()
            writer.writerow(student)
    except Exception as err:
        print()
        print("Something went wrong: " + str(err))

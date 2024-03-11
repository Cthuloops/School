# creating some global shorthands for formatting
stu_id = "Stu ID"
fname = "First Name"
lname = "Last Name"
maj = "Major"
cs = "Course"

# checks if the item to find is a value in a dict in student_registry
# defaults to false since the for loop terminates at the first occurence of the value
def check_if_in_registry(student_registry, item_to_find, key):
    for student in student_registry:
        if item_to_find in student[key]:
            return True
    return False


# prints each student in the registry and each of their classes
def display_registry_content(student_registry):
    print(f"{stu_id:<8}{fname:<13}{lname:<13}{maj:<13}{cs}")
    print("-------------------------------------------------------------")
    # accessing dicts in list of dicts
    for student in student_registry:
        # pulling courses per student into it's own list
        courses = student['courses']
        # listing each course for each student and their info
        for course in courses:
            print(f"{student['student_id']:<8}{student['first_name']:<13}{student['last_name']:<13}{student['major']:<13}{course}")

# asks user to enter a course name and then prints a list of students for the course
def display_course_roster(student_registry):
    course_to_display = input("Enter the course to display: ")
    print()
    # calls check_if_in_registry which returns a boolean
    course_in_registry = check_if_in_registry(student_registry, course_to_display, "courses")
   
    # if the course is found print header and students associated with the class
    if course_in_registry:
        print()
        print(f"{stu_id:<8}{fname:<13}{lname:<13}{maj:<13}")
        print("-------------------------------------------------------------")

        for student in student_registry:
            if course_to_display in student['courses']:
                print(f"{student['student_id']:<8}{student['first_name']:<13}{student['last_name']:<13}{student['major']:<13}")
    else:
        print("Class not found")

# asks user for major and prints a list of students with that major
def list_by_major(student_registry):
    major_to_display = input("Enter the major to display: ")
    print()
    major_in_registry = check_if_in_registry(student_registry, major_to_display, "major")
    
    # if the major to look for is valid, print header and student info related to the major
    if major_in_registry:
        print()
        print(f"{stu_id:<8}{fname:<13}{lname:<13}")
        print("------------------------------")

        for student in student_registry:
            if major_to_display in student['major']:
                print(f"{student['student_id']:<8}{student['first_name']:<13}{student['last_name']:<13}")
    else:
        print("Major not found")
                

def search_by_id(student_registry):
    id_to_display = input("Enter the ID to display: ")
    print()
    id_in_registry = check_if_in_registry(student_registry, id_to_display, "student_id")

    #if the id is valid, print info related to the student
    if id_in_registry:
        print()
        print(f"{stu_id:<8}{fname:<13}{lname:<13}{maj:<13}")
        print("-------------------------------------------------------------")
        
        for student in student_registry:
            if id_to_display in student['student_id']:
                print(f"{student['student_id']:<8}{student['first_name']:<13}{student['last_name']:<13}{student['major']:<13}")
    else:
        print("ID not found")

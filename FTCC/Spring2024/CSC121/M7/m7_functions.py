# functions for m7_project.py

import csv


# let's make this class I guess
class Student():
    """A class to reprsent a Student

    Attributes
    ----------
    stu_id : int
        student ID number
    first_name : str
        first name of the student
    last_name : str
        last name of the student
    major : str
        the students major
    courses : List[str]
        list of courses the student is enrolled in
    email : str
        email for the student

    Methods
    -------
    set_email():
        returns an email for the student
    get_stu_id():
        returns the student's id
    get_first_name():
        returns the student's first name
    get_last_name():
        returns the student's last name
    get_major():
        returns the student's major
    get_courses():
        returns the student's courses
    get_email():
        returns the student's email
    """

    def __init__(self, stu_id, first_name, last_name, major, courses):
        """Constructs all the necessary attributes for the Student object

        Parameters
        ----------
        stu_id : int
            student ID number
        first_name : str
            first name of the student
        last_name : str
            last name of the student
        major : str
            the students major
        courses : List[str]
            list of courses the student is enrolled in
        """

        self.__stu_id = stu_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__major = major
        self.__courses = courses
        self.__email = Student.set_email(self, stu_id, last_name)

    def __repr__(self, delim=', '):

        return "ID: " + str(self.__stu_id) + delim + "First name: " + self.__first_name + delim + "Last name: " + self.__last_name + delim + "Major: " + self.__major + delim + "Email: " + self.__email

    def set_email(self, stu_id, last_name, domain_ext="student.faytechcc.edu"):
        """Sets an email address for the Student

        If the argument 'domain_ext' is passed, then the domain and extenstion of the email is changed

        Parameters
        ----------
        domain_ext : str, optional
            Sets the "domain.extenstion" of the email (default is "student.faytechcc.edu")

        Returns
        -------
        email (str) : email generated for the student
        """
        email = str(stu_id[-2:]) + last_name.lower() + '@' + domain_ext
        return email

    def get_stu_id(self):
        """Used to access stu_id attribute

        Returns
        -------
        value referenced in attribute __stu_id
        """
        return self.__stu_id

    def get_first_name(self):
        """Used to access first_name attribute

        Returns
        -------
        value referenced in attribute __first_name
        """
        return self.__first_name

    def get_last_name(self):
        """Used to access last_name attribute

        Returns
        -------
        value referenced in attribute __last_name
        """
        return self.__last_name

    def get_major(self):
        """Used to access major attribute

        Returns
        -------
        value referenced in attribute __major
        """
        return self.__major

    def get_courses(self):
        """Used to access courses attribute

        Returns
        -------
        value referenced in attribute __courses
        """
        return self.__courses

    def get_email(self):
        """Used to access email attribute

        Returns
        -------
        value referenced in attribute __email
        """
        return self.__email


# create the student objects
def create_instances(student_registry):
    """Converts a dict to a Student instance, returns a list of Student objects"""

    # creating list for packing student instances
    student_list = []
    # for each student in the registry
    for student in student_registry:
        # create an instance of Student
        current_student = (Student(student["student_id"], student["first_name"], student["last_name"], student["major"], student["courses"]))
        student_list.append(current_student)

    return student_list


# write these objects to a csv file
def write_instances(student_list, filename="student_registry_content.csv"):
    """Writes the list created with create_instances to a csv file

    If the argument 'filename' is passed, the filename for the csv created is changed

    Parameters
    ----------
    student list : list[obj]
        list of Student objects
    filename : str, optional
       optional, sets the name for the file created (default is student_registry_content.csv)
    """

    csv_header = ["Stu ID", "First Name", "Last Name", "Major", "Email"]
    try:
        with open(filename, 'w', newline='') as csv_file:
            # create the csv writer
            writer = csv.writer(csv_file)
            # write the header
            writer.writerow(csv_header)
            # write the Student objects from student_list
            for student in student_list:
                # packing the info from the student class into a list, as tuples apparently
                values = str(student.get_stu_id()), student.get_first_name(), student.get_last_name(), student.get_major(), student.get_email()
                # write the student row to the csv
                writer.writerow(values)
    except Exception as err:
        print("Something went wrong: " + str(err))


def create_item_set(student_list, search):
    """Creates a set of items from the student list, returns a tuple (int, set)

    Parameters
    ----------
    student_list : list[obj]
        list of Student objects
    search : str
        'major' or 'courses', changes the values in the set

    Returns
    -------
    max_len : int
        length of the longest string
    item_set : set[str]
        set of the items searched for
    """
    # create the set
    item_set = set()
    # stuff for formatting
    max_len = 0
    # for each student
    for student in student_list:
        # if searching for major, add the major to the set
        if search == 'major':
            major = student.get_major()
            # getting lengths for formatting
            length = len(major)
            if length > max_len:
                max_len = length
            item_set.add(major)
        # if searching for courses
        elif search == 'courses':
            courses = student.get_courses()
            # for each course in the list
            for course in courses:
                # get length for formatting
                length = len(course)
                if length > max_len:
                    max_len = length
                # add the course to the set
                item_set.add(course)
    # sort the set because it looks nice
    item_set = sorted(item_set)
    # return a tuple, length for formatting and then the item set
    return max_len, item_set


def display_course_roster(student_list, course_to_display):
    """Prints the students enrolled in the chosen course

    Parameters
    ----------
    student_list : list[obj]
        list of student objects
    course : str
        course to display students for
    """
    # getting the length of course_to_display for formatting purposes
    format_len = len(course_to_display)
    # some formatting
    print()
    print(course_to_display)
    print(f"{'':-^{format_len}}")
    # for each student in student_list
    for student in student_list:
        # get the courses for that student
        courses = student.get_courses()
        # for each course in the student's courses
        for course in courses:
            # if the course matches the one being searched for
            if course_to_display == course:
                # print the student information
                print(student)


# remake this thing
def get_course_to_display(student_list, search):
    item_set = set()
    max_len = 0
    for student in student_list:
        if search == 'major':
            major = student.get_major()
            length = len(major)
            if length > max_len:
                max_len = length
            item_set.add(major)
        elif search == 'courses':
            courses = student.get_courses()
            for course in courses:
                length = len(course)
                if length > max_len:
                    max_len = length
                item_set.add(course)
    item_set = sorted(item_set)
    keep_going = True
    while keep_going:
        # print a menu of item selection options
        print()
        print(f"{'Choose a Course':^{max_len}}")
        print(f"{'':-^{max_len}}")
        for idx, item in enumerate(item_set):
            # labeling the courses so its easier to select one
            print(f"{str(idx + 1):>2}) {item}")
        print(f"{'':-^48}")
        # get the input
        option = input("Select an option or enter 'q' to return to main menu: ")
        # check if returing to menu, returns None
        if option.casefold() == 'q':
            keep_going = False
        else:
            try:
                # convert option to int, and subtract the one added in the
                # list for readability
                option = int(option) - 1
                # if the option is within the number of items
                if option in range(len(item_set)):
                    # can't index into a set, so iterate through
                    for idx, course in enumerate(item_set):
                        # if the option selected matches the current index
                        if idx == option:
                            # return the item as a string
                            return item
                else:
                    # if the option isn't within the length of the set, start over
                    continue
            # yeah, enter an int
            except ValueError:
                print("Please enter a valid integer\n")
            # idk what else could go wrong but let's handle it
            except Exception as err:
                print("something went wrong: " + str(err) + "\n")

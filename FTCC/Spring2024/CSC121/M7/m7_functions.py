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


# menu because i like it
def display_course_roster_menu(student_list):
    """Menu for display course roster"""

    print(f"{'Display Course Roster':-^29}")
    print("1) Display available courses")
    print("2) Search for course")
    print("3) Return to Main Menu")
    print(f"{'':-^29}")


# lets get this bread
def display_course_roster(student_list, course_to_search_for):
    """Prints Students that have a course matching the search"""

    course_to_search_for = "MAT143-Quantitative Literacy"

    for student in student_list:
        courses = student.get_courses()
        if course_to_search_for in courses:
            print(student)

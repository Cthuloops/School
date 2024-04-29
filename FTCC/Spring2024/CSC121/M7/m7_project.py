# this program runs functions on list of dicts, feat OOP
# 04/28/2024
# CSC121 M7Project OOP
# Harley Coughlin

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

    def __repr__(self, delim='\n'):

        return "ID: " + str(self.__stu_id) + delim + "First name: " + self.__first_name + delim + "Last name: " + self.__last_name + delim + "Major: " + self.__major + delim + "Email: " + self.__email

    def set_email(self, __stu_id, __last_name, domain_ext="student.faytechcc.edu"):
        """Sets an email address for the Student

        If the argument 'atdomext' is passed, then the 

        Parameters
        ----------
        domain_ext : str, optional
            Sets the "domain.extenstion" of the email (default is "student.faytechcc.edu")

        Returns
        -------
        email (str) : email generated for the student
        """
        email = self.__stu_id[-2:] + self.__last_name.lower() + '@' + domain_ext
        return email

    def get_stu_id(self):
        return self.__stu_id

    def get_first_name(self):
        return self.__first_name

    def get_last_name(self):
        return self.__last_name

    def get_major(self):
        return self.__major

    def get_courses(self):
        return self.__courses

    def get_email(self):
        return self.__email

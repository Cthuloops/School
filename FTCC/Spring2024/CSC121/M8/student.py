# class for the final project
# 05/03/2024
# Harley Coughlin

class Student:
    """A class to represent a Student

    Attributes
    ----------
    stu_id : int
        student ID number
    first_name : str
        student's first name
    last_name : str
        student's last name
    login : str
        student's login name
    email : str
        student's email address
    active : bool
        marks the student as active, defaults to True

    Methods
    -------
    set_login():
        returns a login name for the student
    set_email():
        returns an email address for the student
    set_active():
        changes a students active status (True -> False)||(False -> True)
    get_stu_id():
        returns the student's ID
    get_first_name():
        returns the student's first name
    get_last_name():
        returns the student's last name
    get_login():
        returns the student's login
    get_email():
        returns the student's email
    get_active():
        returns the student's active status (T/F)
    """

    def __init__(self, stu_id, first_name, last_name):
        """Constructs all the necessary attributes for the Student object

        Parameters
        ----------
        stu_id : int
            student ID number
        first_name : str
            student's first name
        last_name : str
            student's last name
        """
        self.__stu_id = stu_id
        self.__first_name = first_name
        self.__last_name = last_name
        self.__login = Student.set_login(self, self.__stu_id, self.__last_name)
        self.__email = Student.set_email(self, self.__login)
        self.__active = True

    def __repr__(self, delim=', '):
        return str(self.__stu_id) + delim + self.__first_name + delim + self.__last_name + delim + self.__login + delim + self.__email + delim + str(self.__active)

    def set_login(self, stu_id, last_name):
        """Sets a login for the student

        Returns
        -------
        login (str) : login generated for the student
        """
        stud_id = str(stu_id)
        return last_name[:5].lower() + stud_id[-3:]

    def set_email(self, login):
        """Sets an email for the students

        Returns
        -------
        email (str) : email generated for the student
        """
        return self.__login + "@student.faytechcc.edu"

    def set_active(self):
        """Changes the active status for a student

        Returns
        -------
        True (bool) : if the active status is False, returns True
        False (bool) : if the active status is True, returns False
        """
        self.__active = False

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

    def get_login(self):
        """Used to access login attribute

        Returns
        -------
        value referenced in attribute __login
        """
        return self.__login

    def get_email(self):
        """Used to access email attribute

        Returns
        -------
        value referenced in attribute __email
        """
        return self.__email

    def get_active(self):
        """Used to access active attribute

        Returns
        -------
        value referenced in attribute __active
        """
        return self.__active

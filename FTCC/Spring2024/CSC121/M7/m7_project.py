# this program runs functions on list of dicts, feat OOP
# 04/28/2024
# CSC121 M7Project OOP
# Harley Coughlin


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

    def __repr__(self, delim='\n'):

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
                writer.writerow(values)
    except Exception as err:
        print("Something went wrong: " + str(err))


if __name__ == "__main__":
    students = create_instances(student_registry)
    write_instances(students)

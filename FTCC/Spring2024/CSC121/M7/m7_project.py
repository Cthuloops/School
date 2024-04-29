# this program runs functions on list of dicts, feat OOP
# 04/28/2024
# CSC121 M7Project OOP
# Harley Coughlin

# let's make this class I guess
class Student():

    def __init__(self, stu_id, first_name, last_name, major, courses, email):
        self.stu_id = str(stu_id)
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.courses = courses
        self.email = Student.set_email(self, stu_id, last_name)

    def __repr__(self):
        delim = ','
        return self.stu_id + delim + self.first_name + delim + self.last_name + delim + self.major + delim + self.email

    def set_email(self, stu_id, last_name):
        atdomext = "@student.faytechcc.edu"
        return stu_id[-2:] + last_name + atdomext

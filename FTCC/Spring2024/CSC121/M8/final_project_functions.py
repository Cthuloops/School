# Functions for the final project
# 05/03/2024
# Harley Coughlin


import student
import csv


def read_content():
    with open("StudentInfo.csv", 'rt', newline='') as csv_file:
        # eating the header
        header = csv_file.readline()
        # loading StudentInfo into a list
        csv_reader = csv.reader(csv_file)
        # initializing list for student objects
        student_list = []
        # for each line in the csv
        # unpacking the line
        for last, first, id in csv_reader:
            # append the student object to the list
            student_list.append(student.Student(id, first, last))
        # return the list
        return student_list

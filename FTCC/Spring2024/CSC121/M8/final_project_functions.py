# Functions for the final project
# 05/03/2024
# Harley Coughlin


import student as student_class
import csv


# reads a csv file and converts the info into a list of Student objects
def read_content():
    try:
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
                student_list.append(student_class.Student(id, first, last))
            # return the list
            return student_list
    except FileNotFoundError:
        print("StudentInfo.csv not found in the current directory")
    except Exception as err:
        print("Something went wrong: " + str(err))


# just a helper function for formatting
def get_lengths(student_list):
    header = ['Last Name', 'First Name', 'Email']
    max_fname_len = 0
    max_lname_len = 0
    max_email_len = 0
    # get the lengths of the info from the student objects
    # get the formatting things
    for student in student_list:
        # get the max length of student first names
        fname_len = len(student.get_first_name())
        if fname_len > max_fname_len:
            max_fname_len = fname_len
        # get the max length of student last names
        lname_len = len(student.get_last_name())
        if lname_len > max_lname_len:
            max_lname_len = lname_len
        # get the max lenght of student emails
        email_len = len(student.get_email())
        if email_len > max_email_len:
            max_email_len = email_len
    # if the max name length is shorter than the length of the corresponding
    # header label, set max length to the length of the header instead
    max_fname_len = max_fname_len if max_fname_len > len(header[1]) else len(header[1])
    max_lname_len = max_lname_len if max_lname_len > len(header[0]) else len(header[0])
    return max_fname_len, max_lname_len, max_email_len


# creates a txt and csv file
def write_report(student_list):
    header_csv = ['ID #', 'Last Name', 'First Name', 'Login', 'Email', 'Active']
    # open the csv to write
    with open("student_accounts.csv", 'w', newline='') as csv_file:
        # create the csv writer
        writer = csv.writer(csv_file)
        # write the header
        writer.writerow(header_csv)
        for student in student_list:
            student_info = student.get_stu_id(), student.get_last_name(), student.get_first_name(), student.get_login(), student.get_email(), student.get_active()
            # write the Student info
            writer.writerow(student_info)

    header_txt = ['ID #', 'First Name', 'Last Name', 'Login', 'Active', 'Email']
    # open the text file to write
    with open("stu_accounts_txt.txt", 'w', newline='') as txt_file:
        # get the formatting details from the helper function
        fname_len, lname_len, email_len = get_lengths(student_list)
        # the magic numbers come from the set length of ID, login, and Active status
        title_len = 9 + fname_len + lname_len + 9 + 9 + email_len
        # print the Title, nicely formatted
        print(f"{'Student Login Information':^{title_len}}", file=txt_file)
        print(f"{'':-^{title_len}}", file=txt_file)
        # print the header, adding + 1 so theres a space between fields
        print(f"{header_txt[0]:<9}{header_txt[1]:<{fname_len + 1}}{header_txt[2]:<{lname_len + 1}}{header_txt[3]:<9}{header_txt[4]:<7}{header_txt[5]:<}", file=txt_file)
        # for student in the student list
        for student in student_list:
            # retrieve/print the student info
            student_info = student.get_stu_id(), student.get_last_name(), student.get_first_name(), student.get_login(), student.get_active(), student.get_email()
            print(f"{student_info[0]:<9}{student_info[1]:<{fname_len + 1}}{student_info[2]:<{lname_len + 1}}{student_info[3]:<9}{str(student_info[4]):<7}{student_info[5]:<}", file=txt_file)


def add_student_record(student_list):
    # while loop
    keep_going = True
    while keep_going:
        # prompt for ID from user
        id = input("Enter new Student ID or 'q' to return to Main Menu: ")
        # q to return to main
        if id.lower() == 'q':
            return None
        else:
            # try to convert id to int
            try:
                id = int(id)
                # for each student in the list
                for student in student_list:
                    # if the id exists already
                    if id == student.get_stu_id():
                        # tell the user and return to id input
                        print(f"{id} is already in use.\n")
                        continue
            # handle values other than 'q' and ints
            except ValueError:
                print("Please enter a valid integer\n")
                continue
            fname = input("Enter the Student's first name: ")
            lname = input("Enter the Student's last name: ")
            student_list.append(student_class.Student(id, fname, lname))
            return student_list

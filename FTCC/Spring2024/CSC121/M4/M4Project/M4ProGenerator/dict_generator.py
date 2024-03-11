# this is a helper program to M4Project because I wanted to spend 4 hours
# automating something that would have probably only taken like 20 minutes to type

import random

# this function grabs random names from a txt file and returns a list
def get_names(amount_of_students=20):
    # empty lists for choosing/storing random names
    line_numbers = []
    names_list = []

    # choosing random lines to pull from the names file
    # names file has 10000 entries
    for i in range(amount_of_students):
        line_numbers.append(random.randint(0,10000))
    
    # open the names file and pull the lines that correspond with the random
    # numbers chosen in line_numbers
    # I chose this method instead of reading all the lines into a list and using
    # random.choice() since I think theres the opportunity of reading all the names
    # into the list before reaching the end of the file
    with open("txtdir/firstlast.txt", "r") as names:
        for idx, line in enumerate(names):
            if idx in line_numbers:
                # strip the \n from the line
                names_list.append(line.rstrip())

    return names_list

# using random.choice to choose 2 classes from general.txt returns a list
def general_class_gen():
    # empty list to store class choices
    classes = []

    with open("txtdir/general.txt", "r") as general:
        # read file into lines list
        lines = general.readlines()
        # only need two classes from general
        while len(classes) < 2:
            # removes the chance of duplicate values but can choose two classes
            # from the same subject if they're in the list. I don't think that 
            # matters too much for this application
            random_choice = random.choice(lines)
            if random_choice not in classes:
                classes.append(random_choice.rstrip())

    return classes

# this function takes a major as a parameter and chooses classes related to that major
# returns a list
def major_class_gen(major):
    # empty list to store classes
    classes = []

    
    if major == "Programming":
        major_selected = "txtdir/prog.txt"
    elif major == "Network":
        major_selected = "txtdir/network.txt"
    elif major == "UI/UX":
        major_selected = "txtdir/uiux.txt"
    elif major == "Mech":
        major_selected = "txtdir/mech.txt"
    
    # nvim keeps telling me that major_selected is possibly unbound but I've
    # chosen to ignore it
    with open(major_selected, "r") as major_related:
        lines = major_related.readlines()

        while len(classes) < 2:
            random_choice = random.choice(lines)
            if random_choice not in classes:
                classes.append(random_choice.rstrip())
    return classes

def classes_list_gen(general, major):
    classes_list = []
    classes_list = (general + major)
    return classes_list
# generates random id numbers for the students
def student_id_gen(amount_of_students=20):
    # empty list to store ids
    id_num_list = []

    # choosing a number between 12000 and 13000 for the student id
    # 12000-13000 is an arbitrary range. could have chosen any numbers
    i = 0
    while i < amount_of_students:
        random_num = random.randint(12000, 13000)
        # just making sure there are no duplicates
        if random_num not in id_num_list:
            id_num_list.append(random_num)
            i += 1

    return id_num_list


# calls the other functions and builds a list of dicts to output to a txt file
def main():
    # calling our functions so we have lists of things to work with
    # default amount is 20, kwarg for both functions is amount_of_students
    names = get_names()
    id_numbers = student_id_gen()

    # some shorthands for the formatting step
    dict_id = "{\"student_id\":"
    fname = "\"first_name\":"
    lname = "\"last_name\":"
    maj = "\"major\":"
    majors = ["Programming", "Network", "UI/UX", "Mech"]
    courses = "\"courses\":"
    delim = ", "
    
    # empty list to hold the dict strings
    student_dicts_list = []

    # here we build some strings to add to a list to write to a file
    # formatted in such a way that they're valid dicts just have to remove the 
    # final ',' from the file
    for idx, name in enumerate(names):
        # choosing a major and generating classes per student
        major = random.choice(majors)
        classes_list = classes_list_gen(general_class_gen(), major_class_gen(major))
        # building the string to append to the list
        student_dict = ""
        # splitting the student name into first and last
        student_name = name.split()
        # formatting the string so that it creates a valid dict
        student_dict += dict_id + "\"" + str(id_numbers[idx]) + "\"" + delim + fname + "\"" + student_name[0] + "\""
        student_dict += delim + lname + "\"" + student_name[1] + "\"" + delim + maj + "\"" + major + "\""
        # converting the clases list to a string
        student_dict += delim + courses + str(classes_list) + "},"

        #adding the dict string to the list
        student_dicts_list.append(student_dict)
    
    # writing/overwriting the student dicts into a txt file
    with open("student_dicts.txt", "w") as student_dicts:
        for dict_str in student_dicts_list:
            student_dicts.write(dict_str + "\n")

if __name__ == "__main__":
    main()

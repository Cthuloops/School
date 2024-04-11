# This program parses a patient file and creates a txt & csv from the data
# 03/26/2024
# CSC121 M5Lab
# Harley Coughlin

import csv

# gets the header and patient info from patient_file.txt
def extract_data(filename):
    # open file in readtext mode
    with open(filename, "rt") as patient_file:
        # list for packing patient info dicts
        patient_list = []
        # dict for patient info
        patient_info = {}
        # getting the header
        header = patient_file.readline().rstrip().split(',')
        # reading the rest of the lines into a list
        lines = patient_file.readlines()
        # iterate over lines to extract the data
        for line in lines:
            # strip newline and separate commas
            patient_id, height, weight = line.rstrip().split(',')
            # try to cast height & weight to int
            try:
                height = int(height)
            except Exception:
                print("Patient {} height could not be cast to int".format(patient_id))
            try:
                weight = int(weight)
            except Exception:
                print("Patient {} weight could not be cast to int".format(patient_id))
            # adding key/val pairs to dict
            patient_info[header[0]] = patient_id
            patient_info[header[1]] = height
            patient_info[header[2]] = weight
            # packing the dict into the list
            patient_list.append(patient_info.copy())
        
        return patient_list

# adds bmi as a key/val pair in the patient dicts
def calc_bmi(patient_info):
    # iterate through list
    for patient in patient_info:
        # use height and weight to get bmi
        patient["bmi"] = (patient["weight"] / (patient["height"] ** 2)) * 703

# writes strings to a txt file with patient id and bmi
def write_txt_file(filename, patient_info):
    # open file to write to
    with open(filename, "w") as text_file:
        # unpack dict and write to text file
        for patient in patient_info:
            # build string to write to file
            bmi_string = "Patient-id: {}, BMI: {}\n".format(patient["patient-id"], patient["bmi"])
            text_file.write(bmi_string)

# writes a csv file with all the patient info
def write_csv(filename, patient_info):
    # list to store keys
    keys = []
    # extract list of keys
    for key in patient_info[0].keys():
        keys.append(key)

    with open(filename, "w") as patient_csv:
        # create the dictwriter object
        writer = csv.DictWriter(patient_csv, fieldnames=keys)
        # write the header values
        writer.writeheader()
        # write the info from the dicts in patient_info
        writer.writerows(patient_info)

def main():
    # extract the data from the initial file
    try:
        patient_info = extract_data("patient_file.txt")
    except Exception:
        print("Patient file is not found")

    # update patient info with bmi
    calc_bmi(patient_info)
   
    # I wish I knew more on how to use exceptions
    try:
        write_txt_file("patient_bmi.txt", patient_info)
        write_csv("patient_bmi.csv", patient_info)
    except Exception:
        print("Write operations failed")

    print("Progam completed")
        
if __name__ == "__main__":
    main()

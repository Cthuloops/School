# this is a menu driven program for interacting with files containing sales transactions
# 03/28/2024
# CSC121 M5 Pro
# Harley Coughlin

import csv

# the main menu
def main_menu():
    print()
    print(f"{'Menu':-^58}")
    print("1) Read from existing list of transactions               |")
    print("2) Add new transactions to file                          |")
    print("3) Display total sales for each product                  |")
    print("4) Display total units and total sales for each customer |")
    print("5) Exit                                                  |")
    print(f"{'':-^58}\n")

# read the csv
def get_sales_list(filename):
    # list for packing the csv data 
    sales_list = []
    # open the file for reading
    with open(filename, "rt") as csv_file:
        # create dictreader object
        reader = csv.DictReader(csv_file)
        for row in reader:
            # add the dicts to the sales list
            sales_list.append(row)
    return sales_list

# pretty print the sales list
def print_sales_list(sales_list):
    fieldnames = ["#", "date", "prodID", "custID", "units", "price"]
    # I'm kinda choosing the format arbitrarily, there's no real max value for these
    # fields so it's not possible to guess the perfect spacing
    print(f"{fieldnames[0]:<4}{fieldnames[1]:<11}{fieldnames[2]:<7}{fieldnames[3]:<7}{fieldnames[4]:<6}{fieldnames[5]:<6}")
    print(f"{'':-^40}")
    for sale in sales_list:
        # list for packing values
        value_list = []
        for value in sale.values():
            value_list.append(value)
        print(f"{value_list[0]:<4}{value_list[1]:<11}{value_list[2]:<7}{value_list[3]:<7}{value_list[4]:<6}{value_list[5]:<6}")

# add new transactions to the csv
def add_new_transactions(filename, sales_list):
    # fieldnames for the dictwriter
    fieldnames = ["#", "date", "prodID", "custID", "units", "price"]

    # open file to append
    with open(filename, "a") as csv_file:
        # sentinel for while loop
        keep_going = True
        # create dictwriter object
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # dict for user input
        transaction = {}

        while(keep_going):
            # creating the dict from user input
            # get the transaction info
            transaction["#"] = get_int(transaction_field="#")
            transaction["date"] = get_date()
            transaction["prodID"] = get_int(transaction_field="prodID")
            transaction["custID"] = get_int(transaction_field="custID")
            transaction["units"] = get_int(transaction_field="units")
            transaction["price"] = get_float()
            print()
            
            # write the finished transaction to the file
            writer.writerow(transaction)

            # ask the user if they want to enter more transactions
            choice = input("Enter n/N to quit or press enter to continue: ")
            if choice == 'n' or choice == 'N':
                keep_going = False

# get/validate int
def get_int(transaction_field):
    # sentinel val for while loop
    not_valid = True
    # while loop for input
    while not_valid:
        # make sure to get an int
        try:
            user_input = int(input("Please enter transaction " + transaction_field + ": "))
        except Exception:
            print()
            print("Not a valid integer\n")
            continue
        if user_input > 0:
            not_valid = False
        else:
            print()
            print("Please enter a int larger than 0\n")

    return user_input

# really just going to let the user do basically whatever here as long as the 
# format is correct
def get_date():
    not_valid = True
    while not_valid:
        # prompt user for date
        date = input("Please enter date (format MM/DD/YYYY): ")
        # validate the date
        if date != '':
            # throwing the whole thing in a try block so I don't have to handle
            # the multitude of ways it can break individually
            try:
                check_date = date.split("/")
                for i in range(len(check_date)):
                    check_date[i] = int(check_date[i])
                if check_date[0] > 12 or check_date[0] < 1:
                    print("Month not valid\n")
                    continue
                if check_date[1] > 31 or check_date[1] < 1:
                    print("Day not valid\n")
                    continue
                if check_date[2] > 9999 or check_date[2] < 0:
                    print("Year not valid\n")
                    continue
            except Exception:
                print("Date format incorrect\n")
                continue
        else:
            print()
            print("Date format incorrect\n")
            continue

        return date

# at least this one is super simple
def get_float():
    not_valid = True
    while not_valid:
        try:
            price = float(input("Please enter the price per unit: "))
        except Exception:
            print()
            print("Please enter a valid float\n")
            continue
        if price > 0:
            not_valid = False
        else:
            print()
            print("Please enter a value larger than 0\n")
    return price

# find the totals for the unique product ids in the sales list
def totals_per_product(sales_list):
    # identify unique product ids
    unique_products = set()
    for sale in sales_list:
        unique_products.add(sale["prodID"])

    # dict for the unique product ids
    products = {}
    # for each unique product
    for product in unique_products:
        # total for sales
        total = 0
        # search through the sales list
        for sale in sales_list:
            # if the sale is related to the product
            if sale["prodID"] == product:
                # add the units x price to the total for the product
                total += int(sale["units"]) * float(sale["price"])
        # add product/total to dict
        products[product] = total

    return products

# pretty print the results of total_sales_per_product
def print_totals_per_product(products):
    print("Product | Total")
    print(f"{'':-^16}")
    for product, total in products.items():
        print(f"{product:<9}${total:^7.2f}")

# get total units and total sales per customer
def totals_per_customer(sales_list):
    # going go steal my strat from totals_per_product
    # get the unique custIDs
    unique_customers = set()
    for sale in sales_list:
        unique_customers.add(sale["custID"])

    # list for the customer dicts
    customer_list = []
    # dict for the customers
    customer_dict = {}
    # for each customer
    for customer in unique_customers:
        # totals for units and sales
        total_units = 0
        total_price = 0
        # searching through the sales_list
        for sale in sales_list:
            # if the sale is related to the customer
            if sale["custID"] == customer:
                # add unit amount
                total_units += int(sale["units"])
                # add price of units
                total_price += int(sale["units"]) * float(sale["price"])
        # add the values to the dict
        customer_dict["custID"] = customer
        customer_dict["units"] = total_units
        customer_dict["price"] = total_price
        # pack int the list
        customer_list.append(customer_dict.copy())
        # clear it for the next customer
        customer_dict.clear()

    return customer_list

# print the customer totals to a txt file
def totals_per_customer_file(customer_list):
        with open("customer_totals.txt", 'w') as file:
            print(f"{'Customer ID':<13}{'Total Units Sold':<18}{'Total Sales':<13}", file=file)
            print(f"{'':-^42}", file=file)
            for customer in customer_list:
                print(f"{customer['custID']:0>4}{'':<9}{customer['units']:<18}${customer['price']:<13.2f}", file=file)
        print("customer_totals.txt created/updated")

def execute_menu_option(option, filename):
    # always update the sales list
    sales_list = get_sales_list(filename)

    if option == 1:
        print_sales_list(sales_list)
    elif option == 2:
        add_new_transactions(filename, sales_list)
    elif option == 3:
        print_totals_per_product(totals_per_product(sales_list))
    elif option == 4:
        totals_per_customer_file(totals_per_customer(sales_list))
                
def main():
    keep_going = True
    filename = "sales.csv"
    
    # just checking if the file exists
    try:
        f = open(filename)
    except FileNotFoundError:
        print("File not found, please add \"" + filename + "\" to current directory\n")
        keep_going = False
        print("Program now exiting")
    finally:
        f.close()

    # loop for the main menu
    while keep_going:
        main_menu()
        try:
            option = int(input("Select an option: "))
            print()
        except Exception:
            print()
            print("Please enter a valid menu option\n")
            continue

        # handling exit condition
        if option == 5:
            print()
            print("Now exiting the program\n")
            keep_going = False

        # execute options that aren't exit
        execute_menu_option(option, filename)

if __name__ == "__main__":
    main()

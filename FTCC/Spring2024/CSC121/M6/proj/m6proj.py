# This program reads from a csv and performs operations on the data
# 04/24/2024
# CSC121 M6Proj
# Harley Coughlin

import csv


# extracts the data from WorldSeriesWinners.csv
def extract_data():
    """Returns a list of dicts from WorldSeriesWinners.csv"""
    # using utf-8-sig because there was a BOM
    with open('WorldSeriesWinners.csv', mode='r', encoding='utf-8-sig', newline='') as csv_file:
        # list for packing dicts
        world_series_winners = []
        # create reader
        reader = csv.DictReader(csv_file)
        for line in reader:
            world_series_winners.append(line.strip())

        return world_series_winners


# really couldn't come up with a good name for this
def create_set(world_series_winners):
    """Formats the data from extract_data and returns a tuple (set, list)"""
    # creating the set for team names
    team_names = set()
    # list for packing dicts
    winner_list = []
    # for the data in the list
    for line in world_series_winners:
        # add the team name to the set
        team_names.add(line['Name'])

    # for the team in the set
    for team in team_names:
        # dict for the current team
        winner = {}
        # list for packing the years the current team won
        years_won = []
        # iterating through the list of world_series_winners
        for line in world_series_winners:
            # if the current team is the winning team for the year
            if team in line['Name']:
                # add the year to the list
                years_won.append(line['Year'])
        # add the key/value pairs to the dict
        winner['Name'] = team
        winner['Year'] = years_won
        # add the dict to the list
        winner_list.append(winner)
    # return the list
    return (team_names, winner_list)


# the main menu
def print_main_menu():
    """Just prints a menu"""
    print(f"{'Menu':-^54}")
    print("1) Search by Team (list number of times and years won)")
    print("2) Search by Year")
    print("3) Get file listing number of times each team won")
    print("4) Exit")
    print(f"{'':-^54}")


# get the menu option from the user, returns an int
def get_menu_option():
    """Get Int from user and returns it"""
    # sentinel for loop
    not_valid = True

    while not_valid:
        # prompt user for input
        try:
            option = int(input("Please select a menu option: "))
        # on exception reprompt for a valid int
        except Exception:
            print("Please enter a valid integer (1-4)\n")
            continue
        # if the int is one of the options available exit loop, return option
        if option in range(1, 5):
            not_valid = False
        else:
            print("Please select a valid menu option\n")

    return option


# airoenstoiaernstoieanrstoieanr
def get_team_name(team_names):
    """Prompts user to enter a team name to search for, returns a string"""
    team_name = input("Enter team to search for or enter q to quit: ")
    if team_name.lower() == 'q':
        return None


# search for the team, returns tuple
def search_by_team(team_name, world_series_winners):
    """Takes a team name and searches a list of dicts. Returns a tuple (int, list)"""
    times_won = 0

    for team in world_series_winners:
        if team_name in team['Name']:
            times_won = len(team['Year'])
            years_won = team['Year']

    return (times_won, years_won)


# pretty print the search_by_team results
def print_search_results(team_search_results):
    """Prints results of search_by_team with formatting"""
    print(team_search_results)


# main
def main():

    # data extraction from the csv file
    try:
        team_names, world_series_winners = create_set(extract_data())
    except Exception as err:
        print()
        print("Something went wrong: " + str(err) + "\n")

    # sentinel for the while loop
    keep_going = True

    # main loop
    while keep_going:
        print_main_menu()
        # get the option
        option = get_menu_option()
        if option == 1:
            team_name = input("Please enter team name to search for: ")
            print_search_results(search_by_team(team_name, world_series_winners))
        if option == 4:
            print("Now exiting")
            keep_going = False


if __name__ == "__main__":
    main()

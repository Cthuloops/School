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
        # fields = 'Year', 'Name'
        for line in reader:
            world_series_winners.append(line)

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
        team_names.add(line['Name'].strip())

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
    print()
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


# this is the menu for option 1, search by team
def team_search_menu(team_names):
    """Creates a menu and takes an input for option, returns a string or None"""
    # sentinel value
    not_done = True
    while not_done:
        print()
        print(f"{'Search by Team Menu':-<32}")
        print("1) List Team Names")
        print("2) Enter Team Name to search for")
        print("3) Return to Main Menu")
        print(f"{'':-^32}")
        option = input("(1/2/3) > ")
        try:
            option = int(option)
        except ValueError:
            print("Please enter a valid number")
            continue

        # print the team names if L is selected
        if option == 1:
            print()
            for team in team_names:
                print(team.title())
            continue
        # call get team name and return the input
        elif option == 2:
            team_name = get_team_name(team_names)
            # returns the team_name if not None and continues menu if None
            if team_name is None:
                continue
            return team_name
        # exit the function returning to menu
        elif option == 3:
            not_done = False
        else:
            print("Please enter a valid option")


# gets a team name and checks it against available teams
def get_team_name(team_names):
    """Gets input, checks against team list, returns a string or None"""
    not_done = True
    while not_done:
        print()
        team_name = input("Enter team to search for or enter q to return to search: ")
        # does this count as sanitizing input?
        team_name = team_name.casefold().strip()
        if team_name == 'q':
            return None
        elif not team_in_winners(team_name, team_names):
            print("Team not found")
        else:
            return team_name


# checks if the team_name is present in team_names
def team_in_winners(team_name, team_names):
    for team in team_names:
        if team_name == team:
            return True
    return False


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
def print_team_search_results(team_name, team_search_results):
    """Prints results of search_by_team with formatting"""
    # unpack team_search_results
    times_won, years_won = team_search_results
    # idk how long the logest name is so var for formatting
    length = max(len(team_name), 20)
    # formatting the results
    print()
    print(team_name.title())
    print(f"{'':-^{length}}")
    print(f"{'Times Won':<10}|{'Years Won':-<}")
    print(f"{'':-^{length}}")
    print(f"{times_won:<10}", end=' ')
    # loop for printing years formatted
    for idx, year in enumerate(years_won):
        # if not the last year won add ', ' to the end
        if idx < len(years_won) - 1:
            print(f"{year}", end=', ')
        # if last year, print
        else:
            print(f"{year}")


# get 4 digit year from user
def get_year():
    """Gets int from user, checks if four digits and between 1990-2022, returns int"""
    not_done = True
    # loop for getting user input
    while not_done:
        year = input("Enter four digit year (1990-2022) to search for or q to quit: ")
        if year == 'q':
            year = None
            not_done = False
        else:
            try:
                year = int(year)
            except ValueError:
                print("Input has to be int or 'q'\n")
                continue
            if year < 1990 or year > 2022:
                print("Year needs to be between 1990 and 2022\n")
                continue
            else:
                not_done = False
    return year


# search by the year, print team name that won that year
def search_by_year(year, world_series_winners):
    """Searches a list of dicts, returns string"""
    # search through the world_series_winners
    for team in world_series_winners:
        for years in team['Year']:
            # if the year matches
            if str(year) in years:
                # print the team name
                print()
                print(f"The team that won in {year} is:")
                print(team['Name'].title())


# create file with team names and how many times they won
def create_world_series_agg(team_names, world_series_winners):
    """Creates a formatted txt file of team names and times won"""
    # get the length of the longest team name for formatting
    # init the max length
    max_length = 0
    # go through the team names
    for team in team_names:
        # set length to current team name
        length = len(team)
        # if the current team name is longer than max
        if length > max_length:
            # update max
            max_length = length
    filename = "world_series_aggregated.txt"
    with open(filename, "wt") as file:
        # formatted print
        file.write(f"{'':-^{max_length + 15}}\n")
        file.write(f"|{'Team Name':<{max_length}} | {'Times Won':<} |\n")
        file.write(f"{'':-^{max_length + 15}}\n")
        # iterate through sorted team names
        for team in team_names:
            # iterate through list of dicts
            for winner in world_series_winners:
                # if the team matches the current dict
                if team == winner['Name']:
                    # format team name
                    team_name = winner['Name'].title().strip()
                    # get amount of wins
                    times_won = len(winner['Year'])
                    file.write(f"|{team_name:<{max_length}} | {times_won:<10}|\n")
                    file.write(f"{'':-^{max_length + 15}}\n")


# main
def main():
    """Extracts data from WorldSeriesWinners.csv and can perform operations on it"""

    # data extraction from the csv file
    try:
        team_names, world_series_winners = create_set(extract_data())
        # alphabetical order looks nicer
        team_names = sorted(team_names)
        # if file opens correctly,
        filenotfound = False
    except FileNotFoundError:
        print()
        print("WorldSeriesWinners.csv not found in current directory")
        filenotfound = True
    except Exception as err:
        print()
        print("Something went wrong: " + str(err) + "\n")

    # sentinel for the while loop
    if filenotfound:
        keep_going = False
    else:
        keep_going = True

    # main loop
    while keep_going:
        print_main_menu()
        # get the option
        option = get_menu_option()
        # search by team name
        if option == 1:
            # get the team name or return to main
            team_name = team_search_menu(team_names)
            # if no team name rerun main
            if team_name is None:
                continue
            else:
                # print the results of searching by the team name
                print_team_search_results(team_name, search_by_team(team_name, world_series_winners))
        # search by year
        elif option == 2:
            year = get_year()
            if year is None:
                continue
            search_by_year(year, world_series_winners)
        # create a txt file w/ the data from world_series_winners
        elif option == 3:
            print()
            print("Creating world_series_aggregated.txt")
            try:
                create_world_series_agg(team_names, world_series_winners)
            except Exception as err:
                print("Something went wrong: " + str(err) + "\n")
        # exit the program
        elif option == 4:
            print()
            print("Now exiting")
            keep_going = False


if __name__ == "__main__":
    main()

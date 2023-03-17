import os
import random
from datetime import datetime, timedelta


def that_is_the_way(path):
    """
    The function that_is_the_way takes a path as an argument and returns
     a list of files in that path that contain the substring 'deep'.
    :param path: path of directory to search in
    :return: list of matches
    """
    return [file for file in os.listdir(path) if 'deep' in file]


# print the search result
print(that_is_the_way(os.path.join('images')))


def dont_have_Vinaigrette(start_d, end_d):
    """
    The function checks if the start date is earlier than
    the end date, and raises a ValueError if it is not.
    It then converts the input strings to datetime objects,
    calculates the time range between the start and end dates,
    generates a random number of days between 0 and the total time range,
    and adds that random number of days to the start date to calculate a new random date.
    :param start_d: start date string representing dates in the format 'YYYY-MM-DD'
    :param end_d: end date string representing dates in the format 'YYYY-MM-DD'
    :return: random date converted back to a string in the 'YYYY-MM-DD' format
    """
    # Check if start date is earlier than end date
    if start_d > end_d:
        raise ValueError("Start date can't be later than end date")

    # Convert input strings to datetime objects
    start_date = datetime.strptime(start_d, '%Y-%m-%d')
    end_date = datetime.strptime(end_d, '%Y-%m-%d')

    # Calculate the time range between the start and end dates
    delta = end_date - start_date

    # Generate a random number of days between 0 and the total time range
    random_days = random.randrange(delta.days)

    # Calculate the random date by adding the random number of days to the start date
    rand_date = start_date + timedelta(days=random_days)

    # Print 'Monday' if the random date falls on a Monday
    if rand_date.weekday() == 0:
        print('Dont have Vinaigrette!')

    # Convert the random date back to a string and return it
    return rand_date.strftime('%Y-%m-%d')


# print the random date result
print(dont_have_Vinaigrette('1915-06-23', '1952-06-07'))

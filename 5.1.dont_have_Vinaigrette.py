import random
from datetime import datetime, timedelta


def dont_have_Vinaigrette(start_d, end_d):
    """
    The dont_have_Vinaigrette function takes in two date strings representing a start date and an end date,
    and returns a random date between those two dates.
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


if __name__ == '__main__':
    start_d = input('Enter a start date in the format YYYY-MM-DD: ')
    end_d = input('Enter a end date in the format YYYY-MM-DD: ')
    # print the random date result
    print(dont_have_Vinaigrette(start_d, end_d))

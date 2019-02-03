"""
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

"""

import time
start_time = time.time()


def is_leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


days_dictionary = {'0': 'Monday',
                   '1': 'Tuesday',
                   '2': 'Wednesday',
                   '3': 'Thursday',
                   '4': 'Friday',
                   '5': 'Saturday',
                   '6': 'Sunday'}

starting_date = 0 + 365 % 7  # 1 Jan 1900 is a Monday, and 1900 is not a leap year .. this is a Tuesday 1901


def annual_process(year, starting_day):
    """
    returns a count of months that begin on a Sunday and the starting date for the next year
    """
    day = starting_day
    count = 0
    if day % 7 == 6:  # January
        count = count + 1
    day = day + 31
    if day % 7 == 6:  # February
        count = count + 1
    if is_leap_year(year):  # Adjust for leap year
        day = day + 29
    else:
        day = day + 28
    if day % 7 == 6:  # March
        count = count + 1
    day = day + 31
    if day % 7 == 6:  # April
        count = count + 1
    day = day + 30
    if day % 7 == 6:  # May
        count = count + 1
    day = day + 31
    if day % 7 == 6:  # June
        count = count + 1
    day = day + 30
    if day % 7 == 6:  # July
        count = count + 1
    day = day + 31
    if day % 7 == 6:  # August
        count = count + 1
    day = day + 31
    if day % 7 == 6:  # September
        count = count + 1
    day = day + 30
    if day % 7 == 6:  # October
        count = count + 1
    day = day + 31
    if day % 7 == 6:  # November
        count = count + 1
    day = day + 30
    if day % 7 == 6:  # December
        count = count + 1
    day = day + 31
    return count, day


count = 0
for i in range(1901, 2001):
    year_count, next_day = annual_process(i, starting_date)
    count = count + year_count
    starting_date = next_day

print("Answer = %s" % count)

print("--- %s seconds ---" % (time.time() - start_time))

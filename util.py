from enum import IntEnum
import datetime

class Day(IntEnum):
    TODAY = datetime.datetime.now().weekday()
    MONDAY = 0
    TUESDAY = 1
    WEDNESDAY = 2
    THURSDAY = 3
    FRIDAY = 4
    SATURDAY = 5
    SUNDAY = 6

                
def convert_StrtoDate(str_date):
    # we check what the string input of the user is
    # and then we map each of those strings to the
    # enumerated variant
    if str_date == 'Monday':
        return Day.MONDAY
    elif str_date == 'Tuesday':
        return Day.TUESDAY
    elif str_date == 'Wednesday':
        return Day.WEDNESDAY
    elif str_date == 'Thursday':
        return Day.THURSDAY
    elif str_date == 'Friday':
        return Day.FRIDAY
    elif str_date == 'Saturday':
        return Day.SATURDAY
    else:
        return Day.SUNDAY


def format_datetime(dt):
    '''
    Returns date in the format `Friday, 1 March`
    '''
    return dt.strftime("%A, %-d %B")


def get_next_datetime(day, hour=0):
    '''
    Takes in a day and an hour and returns the soonest possible datetime that is on the day and after the hour
    '''
    dt = datetime.datetime.now()

    # If after hour on day, return current time (with a 1 minute buffer)
    if dt.weekday() == day and dt.hour >= hour:
        return datetime.datetime.now() + datetime.timedelta(minutes=1)

    # Otherwise, increment date to required day and hour
    dt += datetime.timedelta(days=(day-dt.weekday()) % 7)
    return datetime.datetime(dt.year, dt.month, dt.day, hour, 0, 0, 0)


def get_next_datetime_formatted(day, hour=0):
    next_dt = get_next_datetime(day, hour)
    return format_datetime(next_dt)

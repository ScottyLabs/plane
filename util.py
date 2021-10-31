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


def returnNewDate(default_date, new_date):
    #returns default day as an integer
    #Monday is 0 sunday is 6
    default_day = default_date.weekday()
    today = datetime.datetime.now()
    #if same day
    if default_day == new_date:
        return default_date
    elif new_date < default_day:
        difference = default_day - new_date
        send_date = default_date - datetime.timedelta(days = difference)
        #send date is in the past
        #we add 7 days to the send date
        if today > send_date:
            send_date = send_date + datetime.timedelta(days = 7)
            return send_date
        else:
        #send date is in the future
        #just return the send date
            return send_date
    else:
        #new_date > default_day
        difference = new_date - default_day
        return default_date + datetime.timedelta(days = difference)

                
def convert_StrtoDate(str_date):
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

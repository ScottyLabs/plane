from collections import namedtuple
from util import Day, get_next_datetime_formatted

Meeting = namedtuple('Meeting', 'name date time location')

m_gbm = Meeting(
    'General Body Meeting',
    get_next_datetime_formatted(Day.THURSDAY),
    '6pm ET',
    'POS 151',
)

m_watercooler = Meeting(
    'Watercooler Session',
    get_next_datetime_formatted(Day.SUNDAY),
    '9pm ET',
    'http://href.scottylabs.org/watercooler-zoom',
)

m_tech = Meeting(
    'Tech Meeting',
    get_next_datetime_formatted(Day.SATURDAY),
    '2pm ET',
    'http://href.scottylabs.org/tech-zoom',
)

m_planning = Meeting(
    'Planning Meeting',
    get_next_datetime_formatted(Day.SATURDAY),
    '12pm ET',
    'http://href.scottylabs.org/planning-zoom',
)
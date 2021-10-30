from collections import namedtuple, OrderedDict
from functools import partial

#import cli
from meetings import m_gbm, m_watercooler, m_tech, m_planning, m_design
from util import Day, get_next_datetime


DEFAULT_DELIVERY_HOUR = 23 
f = partial(get_next_datetime, hour=DEFAULT_DELIVERY_HOUR)


PlaneSchema = namedtuple('PlaneSchema', 'id template subject delivery_day meetings') # TODO: Rename deliver_day

weekly = PlaneSchema(
    'weekly',
    'weekly',
    "ScottyLabs Meetings This Week",
    f(Day.MONDAY), 
    {
        'gbm': m_gbm,
        'tech': m_tech,
        'design': m_design,
    },
)

longform = PlaneSchema(
    'longform',
    'longform',
    None,
    f(Day.TODAY),
    None,
)

gbm_reminder = PlaneSchema(
    'gbm-reminder',
    'reminder',
    "ScottyLabs GBM Reminder",
    f(Day.THURSDAY),
    {
        'reminder': m_gbm,
    },
)

schema = [ weekly, longform, gbm_reminder]

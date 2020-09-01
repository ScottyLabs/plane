from collections import namedtuple, OrderedDict
from functools import partial

from meetings import m_gbm, m_watercooler, m_hack
from util import Day, get_next_datetime


DEFAULT_DELIVERY_HOUR = 10 # AM
f = partial(get_next_datetime, hour=DEFAULT_DELIVERY_HOUR)


PlaneSchema = namedtuple('PlaneSchema', 'id template subject delivery_day meetings') # TODO: Rename deliver_day

weekly = PlaneSchema(
    'weekly',
    'weekly',
    "ScottyLabs Meetings This Week",
    f(Day.MONDAY), 
    {
        'gbm': m_gbm,
        'watercooler': m_watercooler,
        'hack': m_hack,
    },
)

longform = PlaneSchema(
    'longform',
    'longform',
    None,
    f(Day.TODAY),
    None,
)

schema = [ weekly, longform ]
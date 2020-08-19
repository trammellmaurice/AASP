import calendar
import random

# custom imports
from info import *
from watch_obj import *

"""
GET FREE PERIODS SPECIFIED
"""
def searchPeriod(period_number):
    mid_names = getFourth() # get the list of mids (just 4/C rn)
    free_periods = []
    list = {'M' : [],
            'T' : [],
            'W' : [],
            'R' : [],
            'F' : []}
    for mid in mid_names:
        free_periods = getFreePeriods(mid)
        # print(free_periods)
        for day in free_periods:
            # print(day)
            if period_number in free_periods[day]:
                list[day].append(mid + ': ' + getEmail(mid))
    return list

if 1 == 1:
    print(searchPeriod(4))
    # searchPeriod(4)

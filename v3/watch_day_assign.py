import random
import datetime

# custom imports
from info import *
from watch_obj import *

"""
LIST OF WATCHSTANDSERS AND DATE -> WATCH OBJECTS
"""

# take section and make events
# date = YYYY-MM-DD
def assignWatch(standers,date,ACWATCH = True):
    #create list of watch objects
    watchbill = []
    times = []
    if ACWATCH:
        times = getWatchTimes()
    else:
        times = getWatchTimes(True)

    #check for right NUMBERS
    l1 = len(standers)
    l2 = len(times)
    if l1 != l2:
        return None
    while standers:
        stander = standers.pop(0)
        time = times.pop(0)

        if standers and standers[0] == stander:
            time[1] = times.pop(0)[1]
            if standers and standers[1] == stander:
                time[1] = times.pop(0)[1]
                standers.pop(0)
            standers.pop(0)
        watchbill.append(Watch('CMOD',date,time[0],time[1],'-04:00:00',stander))
    return watchbill

if 1 == 0:
    watchbill = assignWatch(['A','B','C','D','E','F','G','H','I','J','K','L','M'],'2020-08-17')
    for watch in watchbill:
        watch.show()

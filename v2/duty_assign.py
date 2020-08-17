import calendar
import random
import datetime

# custom imports
from info import *
from duty_obj import *

# Returns a schedule list of duty objects with the duty section members as personnel
def assignDutyDays(year,month):
    schedule = []
    # get the duty section assignments
    duty_sections = assignSections()
    i = 1
    for date in calendar.Calendar().itermonthdates(year,month):
        if date.weekday() <= 4:
            section_number = i
            mids = duty_sections[i]
            if date.weekday() < 4:
                schedule.append(Duty('Duty Section ' + str(i),str(date),str(date),mids[2]+mids[3]))
            else:
                schedule.append(Duty('Duty Section ' + str(i),str(date),str(date+datetime.timedelta(days=2)),mids[2]+mids[3]))
            if i >= 9:
                i = 0
            i+=1
    return schedule

if 1 == 0:
    show(assignDutyDays(2020,5))

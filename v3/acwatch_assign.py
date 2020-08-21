import calendar
import random

# custom imports
from info import *
from watch_obj import *
"""
ASSIGN ACWATCH SPOTS
Fill schedule list with WATCH OBJECTS
"""
times = {
'M1' : getPeriodTime(1),
'M2' : getPeriodTime(2),
'M3' : getPeriodTime(3),
'M4' : getPeriodTime(4),
'M5' : getPeriodTime(5),
'M6' : getPeriodTime(6),
'T1' : getPeriodTime(1),
'T2' : getPeriodTime(2),
'T3' : getPeriodTime(3),
'T4' : getPeriodTime(4),
'T5' : getPeriodTime(5),
'T6' : getPeriodTime(6),
'W1' : getPeriodTime(1),
'W2' : getPeriodTime(2),
'W3' : getPeriodTime(3),
'W4' : getPeriodTime(4),
'W5' : getPeriodTime(5),
'W6' : getPeriodTime(6),
'R1' : getPeriodTime(1),
'R2' : getPeriodTime(2),
'R3' : getPeriodTime(3),
'R4' : getPeriodTime(4),
'R5' : getPeriodTime(5),
'R6' : getPeriodTime(6),
'F1' : getPeriodTime(1),
'F2' : getPeriodTime(2),
'F3' : getPeriodTime(3),
'F4' : getPeriodTime(4),
'F5' : getPeriodTime(5),
'F6' : getPeriodTime(6),
}

# create a schedule of 6 watches for X days
def initializeWeek(days = ['M','T','W','R','F']): # default 5 day week
    schedule = []
    for index in range(0,len(days)):
        for i in range (0,6): # add 6 watches per day
            schedule.append((days[index],i + 1))
    return schedule # list full of day, time block pairs


# TODO: Combine methods into 1
def assignAC(schedule, monday_date, shuffle = False):
    dates = getWeekDates(monday_date)
    # add dates info to reference dictionary
    keys = list(times.keys())
    for i in range(0,len(times)):
        times[keys[i]].append(dates[i//6])
    # print(times)
    data = {}
    mids_list = getFourth()
    if shuffle:
        # mids_list.reverse()
        random.shuffle(mids_list)
    for mid in mids_list:
        data[mid] = getFreePeriods(mid) #update a data dictionary

    for index in range(0,len(schedule)):
        day = schedule[index][0]
        period = schedule[index][1]

        for mid in list(data.keys()):
            if period in data[mid][day]:
                schedule[index] = Watch('CMOD',times[day+str(period)][2],times[day+str(period)][0],times[day+str(period)][1], '-04:00:00', mid) # add the mid to the schedule
                # print(times[day+str(period)][2])
                data.pop(mid)
                break
    return schedule

def validate(schedule):
        types = []
        for obj in schedule:
            types.append(type(obj))
        if set([type(Watch())]) != set(types):
            raise Exception('ERROR: Please re-run')

"""
TIME & DATE STUFF
"""
def getWeekDates(start_date): #GET A LIST OF DATES THAT WEEK ***MUST BE A MONDAY***
    base_date = start_date.split('-')
    start = None
    list = []
    # print(int(base_date[1]))
    # get month iterator for that month
    counter = 0;
    for date in calendar.Calendar().itermonthdates(int(base_date[0]), int(base_date[1])):
        if str(date) == start_date and date.weekday() != 0: # make sure they input a monday
            raise Exception('Input the Monday Date')
        elif str(date) == start_date:
            start = date
        if start and date >=start:
            if counter < 5:
                list.append(str(date))
                counter+=1
            else:
                return list

# def getDayOfWeek(date_number):
#     if date_number == 0:
#         return 'Monday'
#     elif date_number == 1:
#         return 'Tuesday'
#     elif date_number == 2:
#         return 'Wednesday'
#     elif date_number == 3:
#         return 'Thursday'
#     elif date_number == 4:
#         return 'Friday'
#     elif date_number == 5:
#         return 'Saturday'
#     elif date_number == 6:
#         return 'Sunday'

def show(schedule):
    for duty in schedule:
        duty.show()


if 1 == 0:
    schedule = assignAC(initializeWeek(['M']), '2020-08-17', True)
    validate(schedule)

    show(schedule)

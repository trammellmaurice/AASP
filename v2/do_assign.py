import calendar
import random

# custom imports
from info import *
from duty_obj import *
from watch_obj import *

"""
Assign 1/C to CDO duty, taking into account date conflicts
[INPUTS] List of names
[OUTPUTS] LIST of Duty objects
"""

# Get list of CDOs from info list
first = getFirst()
second = getSecond()

# List of conflicts
first_conflicts = {
     '2020-07-27' : ['Anthony','Arlett'],
     '2020-07-31'  :  ['Jennings'],
     '2020-09-05' :  ['Edwards']
}

second_conflicts = {

}

# add a conflict to the list (for use in the terminal interface later)
def addConflict(date, name):
    if name in first:
        # print('first')
        if date in first_conflicts.keys():
            first_conflicts[date].append(name)
        else:
            first_conflicts[date] = [name]
        return first_conflicts
    if name in second:
        # print('second')
        if date in second_conflicts.keys():
            second_conflicts[date].append(name)
        else:
            second_conflicts[date] = [name]
        return second_conflicts

# Let's create days and iterate through it to mark each UNASSIGNED
# TODO: Get the accurate days
# TODO: Weekend long duty
def initialize(start,end): # input a pair (first, last)
    schedule = [] # need to fill this with Duty objects
    for i in range(start,end):
        for date in calendar.Calendar().itermonthdates(2020, i):
            schedule.append(str(date))
    return schedule

def assignDO(grade, schedule, shuffle = False):
    """
    Take in a list of midshipmen and pop off the next one
    OPTIONALLY
    - randomize them?
    """
    list = []
    conflicts = []
    position = None
    if grade == 1:
        list = first
        conflicts = first_conflicts
        position = 'CDO'
    elif grade == 2:
        list = second
        conflicts = second_conflicts
        position = 'ACDO'
    else:
        raise Exception("grade must be 1 or 2")
    if shuffle:
        random.shuffle(list)
    # first check next unassigned date
    for index in range(0,len(schedule)):
        if type(schedule[index]) != type(Duty()):
            # print(schedule[index])
            if str(schedule[index]) in conflicts:
                # print(conflicts[str(schedule[index])])
                while list[0] in conflicts[str(schedule[index])]: # TODO: make this a while loop for every possible conflict
                    if list[1] in conflicts[str(schedule[index])]:
                        list.insert(2,list.pop(1))
                    else:
                        list.insert(1,list.pop(0))
                        # fill it with duty objects
                # schedule[index] = list[0]
                # TODO: check for weekends and make them multi day watch objects
                schedule[index] = Duty(position, schedule[index], schedule[index], list[0], list[len(list)-1])
                list.append(list.pop(0))
            else:
                # schedule[index] = list[0]
                schedule[index] = Duty(position, schedule[index], schedule[index], list[0], list[len(list)-1])
                list.append(list.pop(0))
    return schedule



if 1 == 0:
    # print(first)
    # print(second)
    # print(third)
    # print(addConflict('2020-04-29', 'Treseler'))
    show(assignDO(2,initialize(6,7)))
    # print(assign(2,initialize(8,9)))

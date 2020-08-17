import random
import datetime

# custom imports
from info import *
from duty_obj import *

"""
DUTY SECTION NUMBERS AND DATE -> DUTY_OBJECTS
"""

# take section and make events
# date = YYYY-MM-DD
def assignDutyDay(section,date):
    #create a duty object
    duty_day = Duty('Duty Section ' + str(section),date,date,getDutySectionNames(section))
    # duty_day.show()
    return duty_day

if 1 == 0:
    assignDutyDay(1,'2020-08-17')

from __future__ import print_function
import datetime
# custom imports
from calendar_auth import auth
from info import *
from do_assign import *
from acwatch_assign import *
from duty_assign import *

"""
INPUT CONSTANTS
"""
testing = {
'summary' : 'AUTO_ADJ TEST EVENT: ',
'description' : "PLEASE IGNORE **THIS IS A TEST OF THE AUTOMATED ADJUTANT PROGRAM __WATCH_ASSIGNMENT__ CAPABILITY** PLEASE IGNORE",
}

operational = {
'description' : 'This event was created by the Autonomous Adjutant Sergeant Program: if there are any issues with this event (time, date, assignment, description, etc.) please contact your Company Adjutant',
}

"""
METHODS
"""

# FOR DUTIES NOT WATCHES
def makeDuty(info):
    duty = {
        'summary' : info.name() + ' ' + info.position(),
        'description' : operational['description'] + ' Relieving: ' + info.previous(),
        'start' : {
            'date' : info.start_date(),
        },
        'end' : {
            'date' : info.end_date(),
        },
        'attendees' : [
            {'email' : getEmail(info.name())},
        ],
    }
    return duty

def makeDutyDay(info):
    attendees = []
    for name in info.name():
        attendees.append({'email' : getEmail(name)})
    dutyDay = {
        'summary' : info.position(),
        'description' : operational['description'],
        'start' : {
            'date' : info.start_date(),
        },
        'end' : {
            'date' : info.end_date(),
        },
        # 'attendees' : attendees, # No attendees for duty days, it'll kill the API limit
    }
    return dutyDay

def makeWatch(info):
    watch = {
        'summary' : testing['summary'] + info.name() + ' ACWATCH',
        'description' : testing['description'],
        'start' : {
            'dateTime' : info.start_dateTime(),
            'timeZone' : 'America/New_York',
        },
        'end' : {
            'dateTime' : info.end_dateTime(),
            'timeZone' : 'America/New_York',
        },
        'attendees' : [
            {'email' : getEmail(info.name())},
        ],
    }
    return watch

"""
API INTERFACE METHOD
"""
def push(event):
    service = auth() # authenticate and get the service object
    # Call the Calendar API
    event = service.events().insert(calendarId='theplanetmarsz@gmail.com', body=event, sendNotifications = True).execute()
    print ('Event created: %s' % (event.get('htmlLink')))


if 1 == 0:
    acdoData = assignDO(2,initialize(6,7))
    # show(acdoData)
    for duty in acdoData:
        print(makeDuty(duty))
        # push(makeDuty(duty))
if 1 == 0:
    cdoData = assignDO(1,initialize(6,7))
    # show(cdoData)
    for duty in cdoData:
        print(makeDuty(duty))
        # push(makeDuty(duty))

if 1 == 0:
    dutyData = assignDutyDays(2020,6)
    # show(acdoData)
    for duty in dutyData:
        print(makeDutyDay(duty))
        # push(makeDuty(duty))

if 1 == 0:
    acWatch = assignAC(initializeWeek(),'2020-06-08',True)
    validate(acWatch)
    for watch in acWatch:
        print(makeWatch(watch))
        # push(makeWatch(watch))

# sample event as template
"""event = {
    'summary' : 'Test Input',
    'description' : 'Test description',
    'start' : {
        'dateTime' : '2020-05-15T11:00:00-04:00:00',
        'timeZone' : 'America/New_York',
    },
    'end' : {
        'dateTime' : '2020-05-15T11:00:00-04:00:00',
        'timeZone' : 'America/New_York',
    },
    'attendees' : [
        {'email' : 'm216762@usna.edu'},
    ],
}"""

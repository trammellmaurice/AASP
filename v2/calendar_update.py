from __future__ import print_function
import datetime
# custom imports
from calendar_auth import auth
from info import *
from do_assign import *
from acwatch_assign import *

"""
INPUT CONSTANTS
"""
testing = {
'summary' : 'AUTO_ADJ TEST EVENT: ',
'description' : "PLEASE IGNORE **THIS IS A TEST OF THE AUTOMATED ADJUTANT PROGRAM __WATCH_ASSIGNMENT__ CAPABILITY** PLEASE IGNORE",
}

operational = {
'summaryC' : 'CDO Watch: ',
'summaryA' : 'ACDO Watch: ',
'description' : 'This event was created by the Autonomous Adjutant Sergeant Program: if there are any issues with this event (time, date, assignment, description, etc.) please contact your Company Adjutant',
}

"""
METHODS
"""

# FOR DUTIES NOT WATCHES
def makeDuty(info):
    duty = {
        'summary' : testing['summary'] + info.name() + ' ACDO',
        'description' : testing['description'] + ' Relieving: ' + info.previous(),
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

if 1 == 1:
    acWatch = assignAC(initializeWeek(),'2020-06-08',True)
    validate(acWatch)
    for watch in acWatch:
        # print(makeWatch(watch))
        push(makeWatch(watch))

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

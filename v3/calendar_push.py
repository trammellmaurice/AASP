from __future__ import print_function
import datetime
import time
# custom imports
from calendar_auth import auth
from info import *
# from do_assign import *
# from acwatch_assign import *
from duty_section_assign import *
from watch_day_assign import *

"""
INPUT CONSTANTS
"""
testing = {
'summary' : 'AUTO_ADJ TEST EVENT: ',
'description' : "PLEASE IGNORE **THIS IS A TEST OF THE AUTOMATED ADJUTANT PROGRAM __WATCH_ASSIGNMENT__ CAPABILITY** PLEASE IGNORE",
}

operational = {
'description' : """***UOD, SHOW UP 5 MINUTES EARLY***
This event was created by the Automated Adjutant Program: if there are any issues with this event (time, date, assignment, description, etc.) please contact your Company Adjutant m216762@usna.edu""",
}

"""
METHODS
"""

# FOR DUTIES NOT WATCHES
def makeDuty(info):
    duty = {
        'summary' : info.name() + ' ' + info.position(),
        'description' : ' Relieving: ' + info.previous() +"\n"+ operational['description'],
        'start' : {
            'date' : info.start_date(),
        },
        'end' : {
            'date' : info.end_date(),
        },
        'attendees' : [
            {'email' : getEmail(info.name())},
        ],
        "reminders": {
           "useDefault": False,
           "overrides": [
               {
               "method": "email",
               "minutes": "1440"
               },
               {
               "method": "popup",
               "minutes": "30"
               }
           ]
       }
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
        'summary' : info.name() + ' ' + info.position(),
        'description' : operational['description'],
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
         "reminders": {
            "useDefault": False,
            "overrides": [
                {
                "method": "email",
                "minutes": "1440"
                },
                {
                "method": "popup",
                "minutes": "30"
                }
            ]
        }
    }
    return watch

"""
API INTERFACE METHOD
"""
def push(event):
    service = auth() # authenticate and get the service object
    # Call the Calendar API
    event = service.events().insert(calendarId='watchthirtycompany@gmail.com', body=event, sendNotifications = True).execute()
    print ('Event created: %s' % (event.get('htmlLink')))


if 1 == 0:
    # acdoData = assignDO(2,initialize(6,7))
    # show(acdoData)
    for duty in acdoData:
        print(makeDuty(duty))
        # push(makeDuty(duty))
if 1 == 1:
    cdo = Duty('CDO', '2020-07-27', '2020-08-18', 'Trammell', 'Chavez')
    # cdoData = assignDO(1,initialize(6,7))
    # show(cdoData)
    # print(makeDuty(cdo))
    push(makeDuty(cdo))

if 1 == 0:
    dutyData = assignDutyDay(4,'2020-08-18')
    # show(acdoData)
    print(makeDutyDay(dutyData))
    # push(makeDuty(duty))

if 1 == 0:
    order = []
    schedule = assignWatch(order,'2020-08-22')
    for watch in schedule:
        # print(makeWatch(watch))
        push(makeWatch(watch))
        # time.sleep(3)

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

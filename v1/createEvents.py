from __future__ import print_function
import datetime
from calendar_auth import auth
from info import getEmail

#FOR THIS TEST
from cdo_acdo_schedule import getCDO
from cdo_acdo_schedule import getACDO

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

testing = {
'summary' : 'TEST INPUT',
'description' : """THIS IS A TEST OF THE AUTONOMOUS ADJUTANT SERGEANT PROGRAM __CDO_ASSIGNMENT__ CAPABILITY
THIS IS A TEST OF THE AUTONOMOUS ADJUTANT SERGEANT PROGRAM __CDO_ASSIGNMENT__ CAPABILITY
THIS IS A TEST OF THE AUTONOMOUS ADJUTANT SERGEANT PROGRAM __CDO_ASSIGNMENT__ CAPABILITY
THIS IS A TEST OF THE AUTONOMOUS ADJUTANT SERGEANT PROGRAM __CDO_ASSIGNMENT__ CAPABILITY
THIS IS A TEST OF THE AUTONOMOUS ADJUTANT SERGEANT PROGRAM __CDO_ASSIGNMENT__ CAPABILITY
THIS IS A TEST OF THE AUTONOMOUS ADJUTANT SERGEANT PROGRAM __CDO_ASSIGNMENT__ CAPABILITY
THIS IS A TEST OF THE AUTONOMOUS ADJUTANT SERGEANT PROGRAM __CDO_ASSIGNMENT__ CAPABILITY""",
}
operational = {
'summaryC' : 'CDO Watch: ',
'summaryA' : 'ACDO Watch: ',
'description' : 'This event was created by the Autonomous Adjutant Sergeant Program: if there are any issues with this event (time, date, assignment, description, etc.) please contact your Company Adjutant',
}

"""
CDO SCHEDULE METHOD
[Input] Watch schedule: Key value pairs name and date
[Output] One event formatted for Google Calendar API
"""
def makeCDO(info):
    # blank event object
    event = {
        'summary' : testing['summary'] + info[1],
        'description' : testing['description'],
        'start' : {
            'date' : info[0],
        },
        'end' : {
            'date' : info[0],
        },
        'attendees' : [
            {'email' : getEmail(info[1])},
        ],
    }
    return event

"""
ACWATCH SCHEDULE METHOD
[Input] Watch schedule: Key value pairs name and day
[Mechanics] - Connect day to date -
[Output] One event at a time formatted for Google Calendar API
"""

def addEvent(event):
    service = auth() # authenticate and get the service object
    # Call the Calendar API
    event = service.events().insert(calendarId='primary', body=event, sendNotifications = True).execute()
    print ('Event created: %s' % (event.get('htmlLink')))

if 1 == 1:
    data = getCDO()
    # print(data)
    for watch in data:
        # print(watch)
        addEvent(makeCDO(watch))

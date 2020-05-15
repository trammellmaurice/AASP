from __future__ import print_function
import datetime
from calendar_auth import auth

service = auth()

# Call the Calendar API
event = {
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
}
event = service.events().insert(calendarId='primary', body=event, sendNotifications = True).execute()
print ('Event created: %s' % (event.get('htmlLink')))

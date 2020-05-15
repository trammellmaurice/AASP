# (Semi)Autonomous Adjutant Sergeant Program #

## AUTOMATE THE 30TH COMPANY WATCH PROCESS ##
----------------------------------------------
* ### Academic Watch Schedule Program ###
  __ac-watch.py__
  * INPUT : Dictionary {'Name' : 'Free Periods'}
  * OUTPUT : Schedule of names assigned to watches
----------------------------------------------------
* ### Company / Assistant Company Duty Officer Schedule Program ###
  __cdo_acdo_schedule.py__
  * INPUTS : List of Midshipmen ['A','B'], Dictionary of Conflicts {'2020-04-28' : ['A','B']}
  * OUTPUT : Schedule of names assigned to dates (CDO / ACDO separate)
----------------------------------------------------
* ### Pull from Calendar Program / Setup ###
  __quickstart.py__
  * INPUTS : None (Connection Established)
  * OUTPUT : 10 Events from Calendar
----------------------------------------------------
* ### Add Events to Schedule Program ###
  __createEvents.py__
  * INPUTS : CDO / ACDO Schedule (calls cdo-acdo-schedule.py getData())
  * OUTPUT : Events added to calendar / Emails sent to invitees
----------------------------------------------------------------
* ### Supporting Infrastructure ###

  __info.py__
  * INPUT : Midshipmen Name
  * OUTPUT : Midshipmen email or alpha

  __calendar_auth.py__
  * Authentication for google calendar API
  
  __credentials.json__
  * Credentials for Google Calendar API

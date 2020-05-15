# Semi-Autonomous Adjutant Sergeant Program #

## AUTOMATE THE 30TH COMPANY WATCH PROCESS ##
----------------------------------------------
* ### Academic Watch Schedule Program ###
  __ac-watch.py__
  * INPUT : Dictionary {'Name' : 'Free Periods'}
  * OUTPUT : Schedule of names assigned to watches
----------------------------------------------------
* ### Company Duty Officer / Assistant Schedule Program ###
  __cdo-acdo-schedule.py__
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
  * INPUTS : Hard-coded 'event' object (Will Fix)
  * OUTPUT : Events added to calendar / Emails sent to invitees

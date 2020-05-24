# (Semi)Autonomous Adjutant Sergeant Program Version 2 #

## AUTOMATE THE 30TH COMPANY WATCH PROCESS ##
----------------------------------------------
* ### Watch Object ###
  __watch_obj.py__
  * Object for lower watches
  * INPUT position, date,start_time,end_time ,timeZone, name
  ----------------------------------------------
* ### Duty Object ###
  __duty_obj.py__
  * Object for higher watches (CDO, ACDO, duty days)
  * INPUT position, date,start_date,end_date,name,previous
----------------------------------------------
* ### Academic Watch Schedule Program ###
  __acwatch_assign.py__
  * INITIALIZE a schedule week (designate the days (M,T,W,R,F))
  * ASSIGN : Input a schedule, the date of the Monday, and OPTIONAL shuffle
  * OUTPUT : A list of Watch objects
----------------------------------------------------
* ### Company / Assistant Company Duty Officer Schedule Program ###
  __do_assign.py__
  * Assign 1/C and 2/C CDO or ACDO Duty objects
  * Takes into account date conflicts
  * OUTPUT : A list of duty Objects
----------------------------------------------------
* ### Pull from Calendar Program / Setup ###
  __quickstart.py__
  * INPUTS : None (Connection Established)
  * OUTPUT : 10 Events from Calendar
----------------------------------------------------
* ### Add Events to Schedule Program ###
  __calendar_update.py__
  * Make Duty and Watch Calendar events for input
  * OUTPUT : Use GCal API to add to GCalendar
----------------------------------------------------------------
* ### Supporting Infrastructure ###

  __info.py__
  * Holds information for the company
  * METHODS : getEmail(), getFirst(), getSecond(), getThird(), getFreePeriods(), getPeriodTime(), assignSections(), getWeekDates()
  * Used for every other program

  __calendar_auth.py__
  * Authentication for google calendar API

  __credentials.json__
  * Credentials for Google Calendar API

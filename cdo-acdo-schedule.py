import calendar
import random

""" Assign people to duty days and return a schedule
EXAMPLE:
2020-04-27  :  Anthony
2020-04-28  :  Ahmadazani"""

#blank schedule
schedule = {}

# List of Midshipmen
cdos = ['Ahmadazani',
'Anthony','Arlett','Book','Chavez',
'Clymer','Cobb','Cortez','Craig','Craine',
'Dalke','Domler','Edwards','Fulton','Gagnon',
'Hogan','Jennings','Joo','Kane','Keller',
'Kilic','Lake','Leins','Mcginnis','Mcinerney',
'Midgette','Parsons','Polmatier','Rooney','Sand',
'Satre','Tumbas']


cdo_conflicts = {
# date : name
# list of when people cant stand CDO
 '2020-04-28' : ['Anthony','Arlett'],
 '2020-05-14'  :  ['Jennings'],
 '2021-01-03' :  ['Edwards']
}





class Company_Duty:
    def __init__(self,midshipmen,conflicts):
        self.mids_list = midshipmen
        self.conflicts = conflicts
        self.schedule = {}
        # Make a python calendar - iterate through it - assign CDOs to each date
        self.cal = calendar.Calendar()

    # Let's create one month and iterate through it to mark each UNASSIGNED
    # TODO: Get the accurate days
    def addDays(self):
        for i in range(8,13):
            for day in self.cal.itermonthdates(2020, i):
                self.schedule[str(day)] = "unassigned"



    # Let's assign a mid to a date
    def run(self, shuffle = False):
        """ Take in a list of midshipmen and pop off the next one
        OPTIONALLY
        - randomize them? """
        if shuffle:
            random.shuffle(self.mids_list)
        # first check next unassigned date
        for watch in self.schedule:
            if self.schedule[watch] == 'unassigned':
                if watch in self.conflicts:
                    while self.mids_list[0] in self.conflicts[watch]:
                        if self.mids_list[1] in self.conflicts[watch]:
                            self.mids_list.insert(2,self.mids_list.pop(1))
                        else:
                            self.mids_list.insert(1,self.mids_list.pop(0))
                    else:
                        self.schedule[watch] = self.mids_list[0]
                        self.mids_list.append(self.mids_list.pop(0))
                else:
                    self.schedule[watch] = self.mids_list[0]
                    self.mids_list.append(self.mids_list.pop(0))

    # Print in viewable format
    def printForm(self):
        for key, value in self.schedule.items():
            print(key, ' : ', value)

sched = Company_Duty(cdos,cdo_conflicts)
sched.addDays()
sched.run()
# sched.printForm()
date = list(sched.schedule.keys())[0]
print( [date,sched.schedule[date]] )

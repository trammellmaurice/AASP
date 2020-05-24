import calendar
import random

"""
NAME -> ALPHA
"""
TEST = False # SENDS EMAILS TO ME INSTEAD OF ACTUAL PEOPLE
first = {}
second = {}
third = {}
if TEST:
    first = {
    # 1/C
    'Ahmadazani' : 216762,
    'Anthony' : 216762,
    'Arlett' : 216762,
    'Bang' : 216762,
    'Book' : 216762,
    'Chavez' : 216762,
    'Clymer' : 216762,
    'Cobb' : 216762,
    'Cortez' : 216762,
    'Craig' : 216762,
    'Craine' : 216762,
    'Dalke' : 216762,
    'Domler' : 216762,
    'Edwards' : 216762,
    'Fulton' : 216762,
    'Gagnon' : 216762,
    'Hogan' : 216762,
    'Jennings' : 216762,
    'Joo' : 216762,
    'Kane' : 216762,
    'Keller' : 216762,
    'Kilic' : 216762,
    'Lake' : 216762,
    'Leins' : 216762,
    'Mcginnis' : 216762,
    'Mcinerney' : 216762,
    'Midgette' : 216762,
    'Parsons' : 216762,
    'Polmatier' : 216762,
    'Rooney' : 216762,
    'Sand' : 216762,
    'Satre' : 216762,
    'Steerman' : 216762,
    'Trammell' : 216762,
    'Tumbas' : 216762
    }
    # 2/C
    second = {
    'Almas' : 216762,
    'Bain' : 216762,
    'Barta' : 216762,
    'Buchanan' : 216762,
    'Buckley' : 216762,
    'Certesio' : 216762,
    'Collins' : 216762,
    'Corcoran' : 216762,
    'Csuka' : 216762,
    'Duncan' : 216762,
    'Fagot' : 216762,
    'Fiore' : 216762,
    'Hunter' : 216762,
    'Kim' : 216762,
    'Mcdonough' : 216762,
    'Mckeon' : 216762,
    'Mckilligan' : 216762,
    'Medina' : 216762,
    'Mercer' : 216762,
    'Nielson' : 216762,
    'Norman' : 216762,
    'Nufer' : 216762,
    'Peterson' : 216762,
    'Purvis' : 216762,
    'Richardson' : 216762,
    'Sosinsky' : 216762,
    'Shen' : 216762,
    'Stenberg' : 216762,
    'Thomas' : 216762,
    'Treseler' : 216762,
    'Vilinskis' : 216762,
    'Vu' : 216762,
    'Waaler' : 216762,
    'Wade' : 216762,
    'Ward' : 216762,
    'C.Williams' : 216762,
    'J.Williams' : 216762,
    'Witt' : 216762
    }
    # 3/C
    third = {
    'Armstrong' : 216762,
    'Borman' : 216762,
    'Brown' : 216762,
    'Cash' : 216762,
    'Chang' : 216762,
    'Chung' : 216762,
    'Cohn' : 216762,
    'Desantiago' : 216762,
    'Emanus' : 216762,
    'Fuller' : 216762,
    'Gravois' : 216762,
    'Greenberg' : 216762,
    'Hendrickson' : 216762,
    'Kwong' : 216762,
    'Hinola' : 216762,
    'Laplante' : 216762,
    'Lindsay' : 216762,
    'Macaluso' : 216762,
    'Martineau' : 216762,
    'Mathews' : 216762,
    'Meshad' : 216762,
    'Mendez' : 216762,
    'Miller' : 216762,
    'Morris' : 216762,
    'Newton' : 216762,
    'Pattison' : 216762,
    'Ratnayake' : 216762,
    'Rodriguez' : 216762,
    'Rolwes' : 216762,
    'Ruggiero' : 216762,
    'Schlein' : 216762,
    'Scholl' : 216762,
    'Shah' : 216762,
    'Smith' : 216762,
    'Urbana' : 216762,
    'Walz' : 216762,
    'Weimer' : 216762,
    'Wheelock' : 216762,
    }
else:
    first = {
    # 1/C
    'Ahmadazani' : 210054,
    'Anthony' : 210126,
    'Arlett' : 210174,
    'Bang' : 210288,
    'Book' : 210552,
    'Chavez' : 211002,
    'Clymer' : 211098,
    'Cobb' : 211104,
    'Cortez' : 211218,
    'Craig' : 211266,
    'Craine' : 211272,
    'Dalke' : 211338,
    'Domler' : 211548,
    'Edwards' : 211668,
    'Fulton' : 212022,
    'Gagnon' : 212046,
    'Hogan' : 212844,
    'Jennings' : 213108,
    'Joo' : 213270,
    'Kane' : 213318,
    'Keller' : 213372,
    'Kilic' : 213426,
    'Lake' : 213708,
    'Leins' : 213882,
    'Mcginnis' : 214392,
    'Mcinerney' : 214404,
    'Midgette' : 214530,
    'Parsons' : 215196,
    'Polmatier' : 215394,
    'Rooney' : 215742,
    'Sand' : 215874,
    'Satre' : 215910,
    'Steerman' : 216414,
    'Trammell' : 216762,
    'Tumbas' : 216822
    }
    # 2/C
    second = {
    'Almas' : 220102,
    'Bain' : 220348,
    'Barta' : 220444,
    'Buchanan' : 220888,
    'Buckley' : 220894,
    'Certesio' : 221128,
    'Collins' : 221290,
    'Corcoran' : 221350,
    'Csuka' : 221440,
    'Duncan' : 221836,
    'Fagot' : 221968,
    'Fiore' : 222076,
    'Hunter' : 223126,
    'Kim' : 223498,
    'Mcdonough' : 224314,
    'Mckeon' : 224356,
    'Mckilligan' : 224362,
    'Medina' : 224434,
    'Mercer' : 224494,
    'Nielson' : 224830,
    'Norman' : 224860,
    'Nufer' : 224878,
    'Peterson' : 225154,
    'Purvis' : 225310,
    'Richardson' : 225460,
    'Shen' : 225928,
    'Sosinsky' : 226150,
    'Stenberg' : 226252,
    'Thomas' : 226474,
    'Treseler' : 226606,
    'Vilinskis' : 226798,
    'Vu' : 226852,
    'Waaler' : 226858,
    'Wade' : 226864,
    'Ward' : 226924,
    'C.Williams' : 227074,
    'J.Williams' : 227092,
    'Witt' : 227134
    }
    # 3/C
    third = {
    'Armstrong' : 230216,
    'Borman' : 230600,
    'Brown' : 230720,
    'Cash' : 230954,
    'Chang' : 231014,
    'Chung' : 231116,
    'Cohn' : 231176,
    'Desantiago' : 231446,
    'Emanus' : 231758,
    'Fuller' : 232058,
    'Gravois' : 232298,
    'Greenberg' : 232328,
    'Hendrickson' : 232580,
    'Hinola' : 232652,
    'Kwong' : 233396,
    'Laplante' : 233438,
    'Lindsay' : 233570,
    'Macaluso' : 233702,
    'Martineau' : 233852,
    'Mathews' : 233894,
    'Mendez' : 234122,
    'Meshad' : 234152,
    'Miller' : 234194,
    'Morris' : 234344,
    'Newton' : 234518,
    'Pattison' : 234770,
    'Ratnayake' : 235154,
    'Rodriguez' : 235346,
    'Rolwes' : 235370,
    'Ruggiero' : 235460,
    'Schlein' : 235664,
    'Scholl' : 235688,
    'Shah' : 235784,
    'Smith' : 235952,
    'Urbana' : 236414,
    'Walz' : 236648,
    'Weimer' : 236732,
    'Wheelock' : 236816,
    }

def getEmail(mid):
    # go through all classes
    if(mid in first):
        grade = first
    if(mid in second):
        grade = second
    if(mid in third):
        grade = third
    alpha = grade[mid]
    email = 'm' + str(alpha) + '@usna.edu'
    return email

def getFirst():
    return list(first.keys())

def getSecond():
    return list(second.keys())

def getThird():
    return list(third.keys())

"""
NAME -> FREE PERIODS
"""
# TODO : NOT ACCURAT INFO YET
free_periods = {
'Wheelock' : 'M 47 T 3567 W 7 R 3457 F 7 S 1234567',
'Weimer' : 'M 67 T 67 W 67 R 267 F 567 S 1234567',
'Walz' : 'M 47 T 7 W 2467 R 7 F 2467 S 1234567',
'Urbana' : 'M 47 T 157 W 7 R 457 F 347 S 1234567',
'Smith' : ' M 47 T 7 W 17 R 7 F 1347 S 1234567',
'Shah' : 'M 17 T 127 W 17 R 47 F 1567 S 1234567',
'Scholl' : 'M 17 T 1467 W 17 R 1267 F 147 S 1234567',
'Schlein' : 'M 17 T 17 W 157 R 1347 F 157 S 1234567',
'Ruggiero' : 'M 2457 T 17 W 57 R 27 F 57 S 1234567',
'Rolwes' : 'M 57 T 57 W 157 R 57 F 157 S 1234567',
'Rodriguez' : 'M 357 T 1567 W 347 R 57 F 7 S 1234567',
'Ratnayake' : 'M 157 T 567 W 17 R 67 F 17 S 1234567',
'Pattison' : 'M 57 T 17 W 567 R 12347 F 7 S 1234567',
'Newton' : 'M 57 T 27 W 7 R 2347 F 357 S 1234567',
'Morris' : 'M 17 T 1267 W 17 R 1267 F 17 S 1234567',
'Miller' : 'M 7 T 57 W 7 R 7 F 47 S 1234567',
'Meshad' : 'M 7 T 17 W 7 R 127 F 7 S 1234567',
'Mendez' : 'M 37 T 12457 W 47 R 567 F 47 S 1234567',
'Mathews' : 'M 17 T 7 W 57 R 7 F 57 S 1234567',
'Martineau' : 'M 57 T 3457 W 57 R 12457 F 7 S 1234567',
'Macaluso' : 'M 347 T 1257 W 247 R 567 F 7 S 1234567',
'Lindsay' : 'M 37 T 12467 W 67 R 127 F 37 S 1234567',
'Laplante' : 'M 3467 T 27 W 47 R 127 F 67 S 1234567',
'Kwong' : 'M 57 T 127 W 57 R 1257 F 257 S 1234567',
'Hinola' : 'M 57 T 257 W 23567 R 57 F 7 S 1234567',
'Hendrickson' : 'M 127 T 567 W 127 R 67 F 47 S 1234567',
'Greenberg' : 'M 57 T 12357 W 157 R 3457 F 7 S 1234567',
'Gravois' : 'M 27 T 1347 W 7 R 124567 F 27 S 1234567',
'Fuller' : 'M 147 T 67 W 7 R 567 F 1347 S 1234567',
'Emanus' : 'M 27 T 127 W 27 R 267 F 247 S 1234567',
'Desantiago' : 'M 27 T 167 W 67 R 12347 F 67 S 1234567',
'Cohn' : 'M 3567 T 7 W 3457 R 17 F 7 S 1234567',
'Chung' : 'M 37 T 247 W 367 R 12347 F 37 S 1234567',
'Chang' : 'M 237 T 67 W 237 R 127 F 237 S 1234567',
'Cash' : 'M 257 T 17 W 57 R 1257 F 257 S 1234567',
'Brown' : 'M 7 T 457 W 7 R 57 F 7 S 1234567',
'Borman' : 'M 147 T 57 W 7 R 567 F 1247 S 1234567',
'Armstrong' : 'M 157 T 17 W 17 R 127 F 17 S 1234567'
}

def _formatFreePeriods(name):
    # return referencable dictionary
    info = free_periods[name].split()
    info = {'M': [int(d) for d in str(info[1])], 'T': [int(d) for d in str(info[3])], 'W': [int(d) for d in str(info[5])], 'R': [int(d) for d in str(info[7])], 'F': [int(d) for d in str(info[9])]}
    return info

# format the dictionary
for mid in free_periods:
    free_periods[mid] = _formatFreePeriods(mid)

def getFreePeriods(name):
    return free_periods[name]

def getPeriodTime(period):
    periods = {
    1 : ['07:55:00','08:45:00'],
    2 : ['08:55:00','09:45:00'],
    3 : ['09:55:00','10:45:00'],
    4 : ['10:55:00','11:45:00'],
    5 : ['13:30:00','14:20:00'],
    6 : ['14:30:00','15:20:00']
    }
    return periods[period]

"""
DUTY SECTION STUFF
"""
duty_sections = {
    1: {2: [], 3: []},
    2: {2: [], 3: []},
    3: {2: [], 3: []},
    4: {2: [], 3: []},
    5: {2: [], 3: []},
    6: {2: [], 3: []},
    7: {2: [], 3: []},
    8: {2: [], 3: []},
    9: {2: [], 3: []}
}

def assignSections():
    # get class lists
    seconds = getSecond()
    num_sec = len(seconds)//9
    thirds = getThird()
    num_third = len(thirds)//9
    random.shuffle(seconds)
    random.shuffle(thirds)
    # TODO : 4/C
    for section in duty_sections:
        for i in range(0,num_sec):
            duty_sections[section][2].append(seconds.pop())
        for i in range(0,num_third):
            duty_sections[section][3].append(thirds.pop())
    for section in duty_sections:
        while len(seconds) > 0:
            duty_sections[section][2].append(seconds.pop())
            break
        while len(thirds) > 0:
            duty_sections[section][3].append(thirds.pop())
            break
    return duty_sections

def showSections(duty_schedule):
    # print with format
    for section in duty_schedule:
        print('Section ' + str(section) + '| Second Class: ' + str(duty_schedule[section][2]) + ' Youngsters: ' + str(duty_schedule[section][3]))
        print('_________|________________________________________________________________________________________________________________________')

"""
TIME & DATE STUFF
"""
def getWeekDates(start_date): #GET A LIST OF DATES THAT WEEK ***MUST BE A MONDAY***
    base_date = start_date.split('-')
    start = None
    list = []
    # print(int(base_date[1]))
    # get month iterator for that month
    counter = 0;
    for date in calendar.Calendar().itermonthdates(int(base_date[0]), int(base_date[1])):
        if str(date) == start_date and date.weekday() != 0: # make sure they input a monday
            raise Exception('Input the Monday Date')
        elif str(date) == start_date:
            start = date
        if start and date >=start:
            if counter < 5:
                list.append(str(date))
                counter+=1
            else:
                return list
"""
FORMAT STUFF
"""
def show(schedule):
    for duty in schedule:
        duty.show()
if 1 == 0:
    # print(getEmail('Macaluso'))
    # print(getFirst())
    # print(getSecond())
    # print(getThird())
    # print(getFreePeriods('Macaluso'))
    print(getWeekDates('2020-05-18'))

if 1 == 0:
    showSections(assignSections())

import random

"""
NAME -> ALPHA
"""
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
#'Wade' : 226864,
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
'D. Miller' : 234194,
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
fourth = {
'Adkinson' : 240024,
'Alexander' :240066,
'Anderson' :240102,
'Arline' :240162,
'Becker':240324,
'Bland':240438,
'Bly':240468,
'Boamah':240474,
'Brown':240696,
'Cerniglia':240972,
'Cole':241110,
# 'Cromwell': 241230,
'Esqueda' :241668,
'Feng':241752,
'Gerard':242100,
'Gonzalezreed':242190,
'Green':242256,
'Gruendling':242322,
'Grumme':242328,
# 'Guetig':242346,
'Ho':242742,
'Kampling' :243186,
'Kimmel' :243330,
'Kitsch':243372,
'Mcgovern':244152,
'M. Miller':244356,
'Moore':244434,
'Ngo':244620,
'Proctor':245214,
'Savage':245664,
'Stevens':246192,
'Sundvall':246258,
'Tang':246324,
'Tong':246444,
'Umbarger':246564,
'Vath':246618,
'Wojtylak':247074,
'Wood':247086,
'Yelensky':247158,
'Zimmer':247230
}

#########################################################################

def getEmail(mid):
    # go through all classes
    if(mid in first):
        grade = first
    if(mid in second):
        grade = second
    if(mid in third):
        grade = third
    if(mid in fourth):
        grade = fourth
    alpha = grade[mid]
    email = 'm' + str(alpha) + '@usna.edu'
    return email

##########################################################################

def getFirst():
    return list(first.keys())

def getSecond():
    return list(second.keys())

def getThird():
    return list(third.keys())

def getFourth():
    return list(fourth.keys())

############################################################################

"""
NAME -> FREE PERIODS
"""

fourth_frees = {
'Adkinson' : "M 127 T 3457 W 127 R 57 F 7 S 1234567",
'Alexander' :"M 57 T 1257 W 57 R 12357 F 7 S 1234567",
'Anderson' :"M 57 T 57 W 157 R 1247 F 157 S 1234567",
'Arline' :"M 7 TMcgovern 27 W 7 R 27 F 7 S 1234567",
'Becker': "M 7 T 7 W 57 R 12567 F 57 S 1234567",
'Bland':"M 167 T 7 W 467 R 37 F 467 S 1234567",
'Bly':"M 17 T 2567 W 17 R 267 F 147 S 1234567",
'Boamah':"M 7 T 17 W 57 R 3567 F 57 S 1234567",
'Brown':"M 137 T 567 W 17 R 67 F 147 S 1234567",
'Cerniglia':"M 17 T 57 W 7 R 7 F 7 S 1234567",
'Cole':"M 57 T 2567 W 567 R 3567 F 7 S 1234567",
# 'Cromwell': "M 27 T 7 W 7 R 37 F 7 S 1234567",
'Esqueda' :"M 467 T 1247 W 7 R 1247 F 7 S 1234567",
'Feng':"M 147 T 157 W 13467 R 127 F 167 S 1234567",
'Gerard':"M 147 T 157 W 17 R 127 F 157 S 1234567",
'Gonzalezreed':"M 7 T 17 W 57 R 1247 F 57 S 1234567",
'Green':"M 367 T 157 W 37 R 17 F 367 S 1234567",
'Gruendling':"M 567 T 137 W 267 R 7 F 267 S 1234567",
'Grumme':"M 47 T 7 W 57 R 12357 F 457 S 1234567",
# 'Guetig':"M 17 T 14567 W 167 R 127 F 17 S 1234567",
'Ho':"M 157 T 567 W 57 R 457 F 57 S 1234567",
'Kampling' :"M 67 T 47 W 67 R 17 F 3467 S 1234567",
'Kimmel' :"M 347 T 127 W 3457 R 27 F 7 S 1234567",
'Kitsch':"M 47 T 7 W 7 R 567 F 12347 S 1234567",
'Mcgovern':"M 47 T 27 W 2457 R 27 F 247 S 1234567",
'M. Miller':"M 1567 T 47 W 17 R 7 F 1567 S 1234567",
'Moore':"M 57 T 57 W 567 R 1257 F 567 S 1234567",
'Ngo':"M 137 T 17 W 167 R 127 F 137 S 1234567",
'Proctor':"M 167 T 567 W 167 R 7 F 167 S 1234567",
'Savage':"M 17 T 347 W 57 R 3567 F 127 S 1234567",
'Stevens':"M 1257 T 7 W 457 R 7 F 1257 S 1234567",
'Sundvall':"M 157 T 4567 W 1457 R 57 F 157 S 1234567",
'Tang':"M 347 T 1267 W 7 R 127 F 347 S 1234567",
'Tong':"M 467 T 17 W 4567 R 1567 F 467 S 1234567",
'Umbarger':"M 7 T 357 W 17 R 157 F 7 S 1234567",
'Vath':"M 347 T 7 W 257 R 57 F 2347 S 1234567",
'Wojtylak':"M 57 T 7 W 1357 R 1237 F 357 S 1234567",
'Wood':"M 27 T 47 W 1567 R 12347 F 27 S 1234567",
'Yelensky':" M 347 T 12567 W 237 R 67 F 7 S 1234567",
'Zimmer':"M 37 T 17 W 257 R 157 F 2347 S 1234567"
}

############################################################################

def _formatFreePeriods(name):
    # return referencable dictionary
    info = fourth_frees[name].split()
    info = {'M': [int(d) for d in str(info[1])], 'T': [int(d) for d in str(info[3])], 'W': [int(d) for d in str(info[5])], 'R': [int(d) for d in str(info[7])], 'F': [int(d) for d in str(info[9])]}
    return info

# format the dictionary
for mid in fourth_frees:
    fourth_frees[mid] = _formatFreePeriods(mid)

############################################################################

def getFreePeriods(name):
    return fourth_frees[name]

def getPeriodTime(period):
    periods = {
    1 : ['07:45:00','08:50:00'],
    2 : ['08:50:00','09:50:00'],
    3 : ['09:50:00','10:50:00'],
    4 : ['10:50:00','11:55:00'],
    5 : ['13:20:00','14:25:00'],
    6 : ['14:25:00','15:30:00']
    }
    return periods[period]

############################################################################

"""
DUTY SECTIONS
"""
duty_sections = {
    1: {2: ['Vu','Mercer','C.Williams','Purvis'], 3: ['Chung','Ruggiero','Schlein','DeSantiago'], 4: ['Gonzalezreed','Kampling','Kitsch','Wood','Grumme']},
    2: {2: ['Duncan','Kim','Almas', 'Fiore'], 3: ['Weimer', 'Chang', 'Macaluso', 'Gravois'], 4: ['Tang','Vath','Cromwell','Alexander','Gerard']},
    3: {2: ['Ward','Norman','Corcoran', 'J. Williams'], 3: ['Borman','Rowles','Rodriguez','Lindsay'], 4: ['Umbarger', 'Green','Adkinson','Boamah','Anderson']},
    4: {2: ['Csuka','Nufer','Mckeon'], 3: ['Mendez','Scholl','Wheelock','Newton'], 4: ['Mcgovern','Moore', 'Ngo','Feng','Cole']},
    5: {2: ['Vilinskis','Buckley','Shen','Treseler'], 3: ['Brown','Hendrickson','Hinola','Laplante'], 4: ['Yelensky','Proctor','Savage','Esqueda']},
    6: {2: ['Certesio','Thomas','Buchanan','Richardson'], 3: ['Meshad','Fuller', 'Cohn','Emanus'], 4: ['Bly','Arline','Gruendling','Sundvall']},
    7: {2: ['Waaler','Bain','Stenberg'], 3: ['Armstrong','Walz','Pattison','Cash','D. Miller'], 4: ['Bland','Wojtylak','Tong','Becker']},
    8: {2: ['Sosinsky','Peterson','Witt'], 3: ['Shah','Smith','Ratnayake','Martineau','Mathews'], 4: ['M. Miller','Guetig','Ho','Stevens']},
    9: {2: ['Neilson','Collins','Barta','Medina'], 3: ['Morris','Greenberg','Kwong','Urbana'], 4: ['Zimmer','Cerniglia','Brown','Kimmel']}
}

def getDutySectionNames(section):
    names = []
    for name in duty_sections[section][2]:
        names.append(name)
    # for name in duty_sections[section][3]:
    #     names.append(name)
    for name in duty_sections[section][4]:
        names.append(name)
    return names

"""
WATCH SCHEDULES
"""

watches = [
['06:30:00','07:00:00'],
['07:00:00','07:45:00'],
['11:55:00','12:55:00'],
['12:55:00','13:20:00'],
['15:30:00','16:00:00'],
['16:00:00','17:00:00'],
['17:00:00','18:00:00'],
['18:00:00','19:00:00'],
['19:00:00','20:00:00'],
['20:00:00','21:00:00'],
['21:00:00','22:00:00'],
['22:00:00','23:00:00'],
]
alt_watches = [
['06:30:00','07:00:00'],
['07:00:00','08:00:00'],
['08:00:00','09:00:00'],
['09:00:00','10:00:00'],
['10:00:00','11:00:00'],
['11:00:00','12:00:00'],
['12:00:00','13:00:00'],
['13:00:00','14:00:00'],
['14:00:00','15:00:00'],
['15:00:00','16:00:00'],
['16:00:00','17:00:00'],
['17:00:00','18:00:00'],
['18:00:00','19:00:00'],
['19:00:00','20:00:00'],
['20:00:00','21:00:00'],
['21:00:00','22:00:00'],
['22:00:00','23:00:00'],
]

#####################################################
def getWatchTimes(alt = False):
    if alt:
        return alt_watches
    else:
        return watches

"""
TESTS
"""

if 1 == 0:
    # print(getEmail('Buckley'))
    # print(getFirst())
    # print(getSecond())
    # print(getThird())
    # print(getFourth())
    # print(getDutySectionNames(4))
    print(getFreePeriods('Anderson'))

if 1 == 0:
    print(getWatchTimes())

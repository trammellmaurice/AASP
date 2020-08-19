"""
NAME -> FREE PERIODS
"""

list_frees = {
'Adkinson' : "M 127 T 3457 W 127 R 57 F 7 S 1234567",
'Alexander' :"M 57 T 1257 W 57 R 12357 F 7 S 1234567",
'Anderson' :"M 57 T 57 W 157 R 1247 F 157 S 1234567",
'Arline' :"M 7 TMcgovern 27 W 7 R 27 F 7 S 1234567",
'Becker': "M 7 T 7 W 57 R 12567 F 57 S 1234567",
'Bland': "M 167 T 7 W 467 R 37 F 467 S 1234567",
'Bly': "M 17 T 2567 W 17 R 267 F 147 S 1234567",
'Boamah':"M 7 T 17 W 57 R 3567 F 57 S 1234567",
'Brown': "M 137 T 567 W 17 R 67 F 147 S 1234567",
'Cerniglia':"M 17 T 57 W 7 R 7 F 7 S 1234567",
'Cole': "M 57 T 2567 W 567 R 3567 F 7 S 1234567",
# 'Cromwell': "M 27 T 7 W 7 R 37 F 7 S 1234567",
'Esqueda' : "M 467 T 1247 W 7 R 1247 F 7 S 1234567",
'Feng': "M 147 T 157 W 13467 R 127 F 167 S 1234567",
'Gerard': "M 147 T 157 W 17 R 127 F 157 S 1234567",
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
    info = list_frees[name].split()
    info = {'M': [int(d) for d in str(info[1])], 'T': [int(d) for d in str(info[3])], 'W': [int(d) for d in str(info[5])], 'R': [int(d) for d in str(info[7])], 'F': [int(d) for d in str(info[9])]}
    return info

# format the dictionary
for mid in list_frees:
    list_frees[mid] = _formatFreePeriods(mid)

############################################################################

def getFreePeriods(name):
    return list_frees[name]

"""
GET FREE PERIODS SPECIFIED
"""
def searchPeriod(period_number):
    free_periods = []
    list = {'M' : [],
            'T' : [],
            'W' : [],
            'R' : [],
            'F' : []}
    for mid in list_frees:
        free_periods = getFreePeriods(mid)
        # print(free_periods)
        for day in free_periods:
            # print(day)
            if period_number in free_periods[day]:
                list[day].append(mid)
    return list

def formatLong(dictionary):
    for key in dictionary:
        print('____' +  key + '____')
        for value in dictionary[key]:
            print(value)

if 1 == 1:
    # print(getFreePeriods('Anderson'))
    formatLong(searchPeriod(4))
    # searchPeriod(4)

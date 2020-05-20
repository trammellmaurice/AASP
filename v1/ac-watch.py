NUM_WATCHES = 30

# Midshipmen Name: Free Period String
sample_data = {
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

# Days: [Watches to be filled or names]
# 'M' : [[1],[A],[3],[B],[5],[6]]
schedule = {
'M' : [[1],[2],[3],[4],[5],[6]],
'T' : [[1],[2],[3],[4],[5],[6]],
'W' : [[1],[2],[3],[4],[5],[6]],
'R' : [[1],[2],[3],[4],[5],[6]],
'F' : [[1],[2],[3],[4],[5],[6]],
}

class Scheduler:
    def __init__(self, data, schedule):
        self.data = data
        self.schedule = schedule
        temporary = {}
        self.mids = {}
        for mid in self.data:
            temporary[mid] = self.data[mid].split()
        for mid in temporary:
            self.mids[mid] = {'M': [int(d) for d in str(temporary[mid][1])], 'T': [int(d) for d in str(temporary[mid][3])], 'W': [int(d) for d in str(temporary[mid][5])], 'R': [int(d) for d in str(temporary[mid][7])], 'F': [int(d) for d in str(temporary[mid][9])]}

    def run(self):
        for x in range(0,NUM_WATCHES):
            self.setWatch()

    def showUnassigned(self):
        # get the next unassigned period from the schedule
        for day in self.schedule:
            for period in self.schedule[day]:
                if type(period[0]) == type(1):
                    print('unassigned',day,period[0])

    def getNextUnassigned(self):
        # get the next unassigned period from the schedule
        for day in self.schedule:
            for period in self.schedule[day]:
                if type(period[0]) == type(1):
                    return [day,period[0]]

    def assignMid(self):
        # given a day and period, get a mid with that period free
        temp = self.getNextUnassigned()
        period = temp[1]
        day = temp[0]
        for mid in self.mids:
            if period in self.mids[mid][day]:
                # remove the mid from the mids pool and add them to the end
                # remove that free period from that mid
                self.mids[mid][day].remove(period)
                value = self.mids.pop(mid)
                self.mids.update({mid:value})
                return [mid,temp]

    def setWatch(self):
        # put a name in the schedule
        temp = self.assignMid()
        for spot in self.schedule[temp[1][0]]:
            if type(spot[0]) == type(1): # if its a number still
                # self.showUnassigned()
                spot[0] = [temp[0],spot[0]]
                return self.schedule

    def printSchedule(self):
        # print the schedule of assigned Watches
        for key, value in self.schedule.items():
            print(key, ' : ', value)

if 1 == 1:
    s = Scheduler(sample_data, schedule)
    s.run()
    s.printSchedule()

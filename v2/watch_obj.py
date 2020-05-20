"""
WATCH OBJECT
This class is to be the data type for uniformity between programs.
This data type represents a specific Watch for lower watches
"""

class Watch:
    def __init__(self, position = None, date = None, start_time = None, end_time = None, timeZone = None, name = None):
        if name:
            self._position = position
            self._start_dateTime = date + 'T' + start_time + timeZone
            self._end_dateTime = date + 'T' + end_time + timeZone
            self._name = name

    def position(self):
        return self._position

    def start_dateTime(self):
        return self._start_dateTime

    def end_dateTime(self):
        return self._end_dateTime

    def name(self):
        return self._name

    def show(self):
        print([self.position(), self.start_dateTime(), self.end_dateTime(), self.name()])

if 1 == 0:
    cmod = Watch('CMOD', '2020-07-27', '08:00:00', '09:00:00', '-04:00:00', 'Trammell')
    cmod.show()

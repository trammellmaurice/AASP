"""
DUTY OBJECT
This class is to be the data type for uniformity between programs.
This data type represents a Duty Day for higher watches (CDO, ACDO, etc)
"""

class Duty:
    def __init__(self, position = None, start_date = None, end_date = None, name = None, previous = None):
        self._position = position
        self._start_date = start_date
        self._end_date = end_date
        self._name = name
        self._previous = previous

    def position(self):
        return self._position

    def start_date(self):
        return self._start_date

    def end_date(self):
        return self._end_date

    def name(self):
        return self._name

    def previous(self):
        return self._previous

    def show(self):
        print([self.position(), self.start_date(), self.end_date(), self.name(), self.previous()])
if 1 == 0:
    cdo = Duty('CDO', '2020-07-27', '2020-07-27', 'Trammell', 'Chavez')
    cdo.show()

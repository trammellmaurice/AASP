"""
WATCH SCHEDULES
"""

watches = [
0.5,
0.75,
1.17,
1,
1,
1.08,
1,
0.42,
1.08,
1.08,
0.5,
1,
1,
1,
1,
1,
1,
1]


alt_watches = [
0.5,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
1,
]

#####################################################
def getWatchHours(alt = False):
    if not alt:
        return alt_watches
    else:
        return watches

"""
TEST
"""
if 1 == 0:
    print(getWatchHours())

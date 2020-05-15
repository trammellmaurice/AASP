#FIXME: FIX ALPHAS
# Need a file to store information so it can be retrieved to make Events
mids_test = {
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
'Tumbas' : 216762,
}

def getEmail(mid, mids = mids_test):
    alpha = mids[mid]
    email = 'm' + str(alpha) + '@usna.edu'
    return email

if 1 == 0:
    print(getEmail('Trammell'))

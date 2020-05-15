# Need a file to store information so it can be retrieved to make Events
mids = {
'Ahmadazani' : 21,
'Anthony' : 21,
'Arlett' : 21,
'Bang' : 21,
'Book' : 21,
'Chavez' : 21,
'Clymer' : 21,
'Cobb' : 21,
'Cortez' : 21,
'Craig' : 21,
'Craine' : 21,
'Dalke' : 21,
'Domler' : 21,
'Edwards' : 21,
'Fulton' : 21,
'Gagnon' : 21,
'Hogan' : 21,
'Jennings' : 21,
'Joo' : 21,
'Kane' : 21,
'Keller' : 21,
'Kilic' : 21,
'Lake' : 21,
'Leins' : 21,
'Mcginnis' : 21,
'Mcinerney' : 21,
'Midgette' : 21,
'Parsons' : 21,
'Polmatier' : 21,
'Rooney' : 21,
'Sand' : 21,
'Satre' : 21,
'Steerman' : 21,
'Trammell' : 216762,
'Tumbas' : 21,
}

def getEmail(mid, mids = mids):
    alpha = mids[mid]
    email = 'm' + str(alpha) + '@usna.edu'
    return email

if 1 == 0:
    print(getEmail('Trammell'))

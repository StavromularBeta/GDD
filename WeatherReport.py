from tinydb import TinyDB, Query
db = TinyDB('db.json')
crddb = TinyDB('crddb.json')

Entry = Query()
JBentries = db.search(Entry.name == "JamesBay")
Sentries = db.search(Entry.name == "Sangster")

directions = {"Na": [348.75,360],
              "Nb": [0,11.25],
              "NNE": [11.25,33.75],
              "NE": [33.75,56.25],
              "ENE": [56.25,78.75],
              "E": [78.75,101.25],
              "ESE": [101.25,123.75],
              "SE": [123.75,146.25],
              "SSE": [146.25,168.75],
              "S": [168.75,191.25],
              "SSW": [191.25,213.75],
              "SW": [213.75,236.25],
              "WSW": [236.25,258.75],
              "W": [258.75,281.25],
              "WNW": [281.25,303.75],
              "NW": [303.76,326.25],
              "NNW": [326.25,348.75]}

MostRecentJB = JBentries[-1]
MostRecentSentries = Sentries[-1]

print '\n'
print 'Weather Report:'
print 'Time: ' + MostRecentJB['Time']
print '\n'
print "Jennie's House: T(C) = " + MostRecentSentries['T']
print "Wind (km/hr) = " + MostRecentSentries['W']
print "Hourly Rain (mm/hr) = " + MostRecentSentries['hRain']
print '\n'
print "Home: T(C) = " + MostRecentJB['T']
print "Wind (km/hr) = " + MostRecentJB['W']
print "Hourly Rain (mm/hr) = " + MostRecentJB['hRain']
print '\n'

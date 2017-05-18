#!/usr/local/bin/python
from tinydb import TinyDB, Query
db = TinyDB('db.json')
crddb = TinyDB('crddb.json')
import datetime

Entry = Query()
coordinate_entries = crddb.all()
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

for item in coordinate_entries:
    print "\n"
    print item['name']
    print crddb.search(Entry.name == item['name'])[0]['Coord']
    print "-----------------------------------------------------"
    for item in db.search(Entry.name == item['name']):
        for key, value in directions.items():
            if item['Wdir'] == '----':
                direction = ''
            elif value[0] <= float(item['Wdir']) <= value[1]:
                direction = key
        print item['Time'] + " | T = " + item['T'] + " Celsius"
        print "                          | Wind = " + item['W'] + " km\hr " + direction
        print "-------------------------------------------------"


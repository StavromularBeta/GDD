from tinydb import TinyDB, Query
db = TinyDB('db.json')
crddb = TinyDB('crddb.json')
import datetime

Entry = Query()
coordinate_entries = crddb.all()
for item in coordinate_entries:
    print "\n"
    print item['name']
    print crddb.search(Entry.name == item['name'])[0]['Coord']
    for item in db.search(Entry.name == item['name']):
        print item['Time'] + " | T = " + item['T'] + " Celsius"

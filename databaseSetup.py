from tinydb import TinyDB, Query
db = TinyDB('db.json')
import datetime

print db.all()[0]['name=StJosephs id=215'][0]
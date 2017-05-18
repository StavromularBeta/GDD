from tinydb import TinyDB, Query
import datetime
from lxml import html
import requests
db = TinyDB('db.json')
crddb = TinyDB('crddb.json')

namelist = []
idlist = []

for item in db.all():
    namelist.append(item['name'])
    idlist.append(item['id'])

addresslist = []

for item in namelist:
    address = 'http://www.victoriaweather.ca/station.php?name=' + item
    addresslist.append(address)

for item in addresslist:
    index = addresslist.index(item)
    page = requests.get(item)
    tree = html.fromstring(page.content)
    crds = tree.xpath("//span[@class='small']/text()")[-1]
    crddb.insert({"name": namelist[index], "id": idlist[index], "Coord": str(crds)})


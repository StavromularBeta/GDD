#!/usr/bin/env python

from lxml import html
import requests
from tinydb import TinyDB
import Webscraper_functions as ff


db = TinyDB('db.json')

page = requests.get('http://www.victoriaweather.ca/all_current_data.php')
tree = html.fromstring(page.content)
trs = tree.xpath("//table[@class='extreme']/tr/td/text()")[:-4]
labels = tree.xpath("//a/@href")[5:-5]

trs = ff.n_remover(trs)
slices = ff.slices_maker(trs)
labels = ff.label_splitter(labels)
station_list = ff.labels_processor(labels)
slices = ff.time_adder(slices)
stationsdict = ff.dictionary_maker(station_list, slices)

for item in stationsdict:
    db.insert(item)

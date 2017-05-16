#!/usr/bin/env python

from lxml import html
import requests
from tinydb import TinyDB, Query
import datetime

db = TinyDB('db.json')

page = requests.get('http://www.victoriaweather.ca/all_current_data.php')
tree = html.fromstring(page.content)
trs = tree.xpath("//table[@class='extreme']/tr/td/text()")[:-4]
labels = tree.xpath("//a/@href")[5:-5]


def n_remover(raw_data):
    for entry in raw_data:
        if entry == "\n":
            del raw_data[raw_data.index(entry)]
    return raw_data

trs = n_remover(trs)


def slices_maker(raw_data):
    slices_list = []
    raw_data_length = len(raw_data)
    x = 0
    y = 9
    while y < raw_data_length+1:
        trs_slice = raw_data[x:y]
        x += 9
        y += 9
        slices_list.append(trs_slice)
    return slices_list

slices = slices_maker(trs)


def label_splitter(raw_labels):
    for item in raw_labels:
        items = item.split("?")
        raw_labels[raw_labels.index(item)] = items[1]
    return raw_labels

labels = label_splitter(labels)


def labels_processor(raw_labels):
    station_list = []
    newy = 1
    labels_length = len(raw_labels)
    while newy < labels_length:
        if raw_labels[newy][:4] == "name":
            stringstring = raw_labels[newy] + " " + raw_labels[newy-1]
            newy += 2
            station_list.append(stringstring)
        else:
            del raw_labels[newy]
            labels_length = len(raw_labels)
    return station_list

station_list = labels_processor(labels)


def time_adder(raw_slices):
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%a, %d %b %Y %H:%M:%S")
    for entry in raw_slices:
        entry.append(current_date)
    return raw_slices

slices = time_adder(slices)


def dictionary_maker(raw_stationlist, raw_slices):
    newx = 0
    stationsdict = {}

    while newx < len(raw_slices):
        stationsdict[raw_stationlist[newx]] = raw_slices[newx]
        newx +=1
    return stationsdict

stationsdict = dictionary_maker(station_list,slices)
db.insert(stationsdict)

for item in stationsdict:
    print item
    print stationsdict[item]

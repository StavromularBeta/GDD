#!/usr/bin/env python

from lxml import html
import requests


page = requests.get('http://www.victoriaweather.ca/all_current_data.php')
tree = html.fromstring(page.content)
trs = tree.xpath("//table[@class='extreme']/tr/td/text()")[:-4]
labels = tree.xpath("//a/@href")[5:-5]

for item in trs:
    if item == "\n":
        del trs[trs.index(item)]

trs_length = len(trs)

x = 0
y = 9
slices = []

while y < trs_length+1:
    trs_slice = trs[x:y]
    x += 9
    y += 9
    slices.append(trs_slice)

for item in labels:
    items = item.split("?")
    labels[labels.index(item)] = items[1]

newy = 1
labels_length = len(labels)
station_list = []

while newy < labels_length:
    if labels[newy][:4] == "name":
        stringstring = labels[newy] + " " + labels[newy-1]
        newy += 2
        station_list.append(stringstring)
    else:
        del labels[newy]
        labels_length = len(labels)

newx = 0
stationsdict = {}

while newx < len(slices):
    stationsdict[station_list[newx]] = slices[newx]
    newx +=1

for item in stationsdict:
    print item
    print stationsdict[item]

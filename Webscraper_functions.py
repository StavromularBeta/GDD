import datetime


def n_remover(raw_data):
    for entry in raw_data:
        if entry == "\n":
            del raw_data[raw_data.index(entry)]
    return raw_data


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


def label_splitter(raw_labels):
    for item in raw_labels:
        items = item.split("?")
        raw_labels[raw_labels.index(item)] = items[1]
    return raw_labels


def labels_processor(raw_labels):
    station_list = []
    newy = 1
    labels_length = len(raw_labels)
    while newy < labels_length:
        if raw_labels[newy][:4] == "name":
            stringstring = [raw_labels[newy][5:], raw_labels[newy-1][3:]]
            newy += 2
            station_list.append(stringstring)
        else:
            del raw_labels[newy]
            labels_length = len(raw_labels)
    return station_list


def time_adder(raw_slices):
    current_date = datetime.datetime.now()
    current_date = current_date.strftime("%a, %d %b %Y %H:%M:%S")
    for entry in raw_slices:
        entry.append(current_date)
    return raw_slices


def dictionary_maker(raw_stationlist, raw_slices):
    newx = 0
    dictlist = []

    while newx < len(raw_slices):
        stationsdict = {}
        stationsdict['name'] = raw_stationlist[newx][0]
        stationsdict['id'] = raw_stationlist[newx][1]
        stationsdict['T'] = raw_slices[newx][0]
        stationsdict['H'] = raw_slices[newx][1]
        stationsdict['p'] = raw_slices[newx][2]
        stationsdict['Ins'] = raw_slices[newx][3]
        stationsdict['UV'] = raw_slices[newx][4]
        stationsdict['Rain'] = raw_slices[newx][5]
        stationsdict['hRain'] = raw_slices[newx][6]
        stationsdict['W'] = raw_slices[newx][7]
        stationsdict['Wdir'] = raw_slices[newx][8]
        stationsdict['Time'] = raw_slices[newx][9]
        newx +=1
        dictlist.append(stationsdict)
    return dictlist

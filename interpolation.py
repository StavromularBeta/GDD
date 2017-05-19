from scipy.interpolate import griddata
from tinydb import TinyDB, Query
import numpy as np
import matplotlib.pyplot as plt

coordinate_entries = TinyDB('crddb.json')
namelist = []
coordinates = coordinate_entries.all()

for item in coordinates:
    namelist.append(item['name'])

temperature_entries = TinyDB('onedb.json')
entry = Query()
counter = 0
t_points = []
t_values = []

for name in namelist:
    one_temp_entry = temperature_entries.get(entry.name == name)
    if one_temp_entry['T'] == "----":
        pass
    elif one_temp_entry['T'] == "---":
        pass
    else:
        t_points.append(one_temp_entry['name'])
        t_values.append(float(one_temp_entry['T']))

t_coords = []
lats = []
longs = []

for item in t_points:
    coordinates = coordinate_entries.get(entry.name == item)
    coords = coordinates['Coord']
    long = float(coords[11:18])
    lat = float(coords[30:36])
    coords = [lat, long]
    lats.append(lat)
    longs.append(long)
    t_coords.append(coords)

coordarray = np.array(t_coords)
valuearray = np.array(t_values)
lat, long = np.mgrid[233:237:2000j, 50.5:48:2000j]

z = griddata(coordarray, valuearray, (long, lat), method='linear')
plt.imshow(z.T, extent=(233,237,48,50.5), origin="upper")
plt.colorbar()
plt.scatter(coordarray[:,1], coordarray[:,0], s=0.1, alpha = 0.5)
plt.savefig('interpolation.png', dpi=1000)
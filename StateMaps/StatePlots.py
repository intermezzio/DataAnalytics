'''import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex, Normalize
from matplotlib.patches import Polygon # https://stackoverflow.com/questions/39742305/how-to-use-basemap-python-to-plot-us-with-50-states
# https://gis.stackexchange.com/questions/198530/plotting-us-cities-on-a-map-with-matplotlib-and-basemap
from matplotlib.collections import PatchCollection
from matplotlib.colorbar import ColorbarBase
import os.path

m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49, projection='lcc',lat_1=33,lat_2=45,lon_0=-95)

shp_info = m.readshapefile('st99_d00','states',drawbounds=True)

data = { # dictionary of data
    "New Jersey": 65,
    "New York": 52,
    "state": "value"
}

#colors = dict()

#colorMap = plt.cm.YlOrRd




'''
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
shp_info = m.readshapefile('st99_d00','states',drawbounds=True)
popdensity = {
'New Jersey': 438.00,
'Rhode Island': 387.35,
'Massachusetts': 312.68,
'Connecticut': 271.40,
'Maryland': 209.23,
'New York': 155.18,
'Delaware': 154.87,
'Florida': 114.43,
'Ohio': 107.05,
'Pennsylvania': 105.80,
'Illinois': 86.27,
'California': 83.85,
'Hawaii': 72.83,
'Virginia': 69.03,
'Michigan': 67.55,
'Indiana': 65.46,
'North Carolina': 63.80,
'Georgia': 54.59,
'Tennessee': 53.29,
'New Hampshire': 53.20,
'South Carolina': 51.45,
'Louisiana': 39.61,
'Kentucky': 39.28,
'Wisconsin': 38.13,
'Washington': 34.20,
'Alabama': 33.84,
'Missouri': 31.36,
'Texas': 30.75,
'West Virginia': 29.00,
'Vermont': 25.41,
'Minnesota': 23.86,
'Mississippi': 23.42,
'Iowa': 20.22,
'Arkansas': 19.82,
'Oklahoma': 19.40,
'Arizona': 17.43,
'Colorado': 16.01,
'Maine': 15.95,
'Oregon': 13.76,
'Kansas': 12.69,
'Utah': 10.50,
'Nebraska': 8.60,
'Nevada': 7.03,
'Idaho': 6.04,
'New Mexico': 5.79,
'South Dakota': 3.84,
'North Dakota': 3.59,
'Montana': 2.39,
'Wyoming': 1.96,
'Alaska': 0.42}
colors={}
statenames=[]
cmap = plt.cm.hot
vmin = 0; vmax = 450
'''
for shapedict in m.states_info:
statename = shapedict['NAME']
if statename not in ['District of Columbia','Puerto Rico']:
pop = popdensity[statename]
colors[statename] = cmap(1.-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
statenames.append(statename)
ax = plt.gca()
for nshape,seg in enumerate(m.states):
if statenames[nshape] not in ['District of Columbia','Puerto Rico']:
color = rgb2hex(colors[statenames[nshape]]) 
poly = Polygon(seg,facecolor=color,edgecolor=color)
ax.add_patch(poly)
plt.title('Filling State Polygons by Population Density')
plt.show() '''
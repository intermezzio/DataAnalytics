import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
m = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
projection='lcc',lat_1=33,lat_2=45,lon_0=-95)
shp_info = m.readshapefile('StateMaps/st99_d00','states',drawbounds=True)

stateList = ['Mississippi', 'Oklahoma', 'Delaware', 'Minnesota', 'Illinois', 'Arkansas', 'New Mexico', 'Indiana', 'Louisiana', 'Texas', 'Wisconsin', 'Kansas', 'Connecticut', 'California', 'West Virginia', 'Georgia', 'North Dakota', 'Pennsylvania', 'Alaska', 'Missouri', 'South Dakota', 'Colorado', 'New Jersey', 'Washington', 'New York', 'Nevada', 'Maryland', 'Idaho', 'Wyoming', 'Arizona', 'Iowa', 'Michigan', 'Utah', 'Virginia', 'Oregon', 'Montana', 'New Hampshire', 'Massachusetts', 'South Carolina', 'Vermont', 'Florida', 'Hawaii', 'Kentucky', 'Rhode Island', 'Nebraska', 'Ohio', 'Alabama', 'North Carolina', 'Tennessee', 'Maine']

dataset = {
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
'Alaska': 0.42} # replace with real data

colors={}
statenames=[]
cmap = plt.cm.YlOrRd
vmin = 0; vmax = 100 # set range.
for shapedict in m.states_info:
    statename = shapedict['NAME']
    if statename not in ('District of Columbia','Puerto Rico', 'Alaska', 'Hawaii'):
        pop = dataset[statename]
        # calling colormap with value between 0 and 1 returns
        # rgba value.  Invert color range (hot colors are high
        # population), take sqrt root to spread out colors more.
        colors[statename] = cmap(1.-np.sqrt((pop-vmin)/(vmax-vmin)))[:3]
    statenames.append(statename)
# cycle through state names, color each one.
ax = plt.gca() # get current axes instance
for nshape,seg in enumerate(m.states):
    # skip DC and Puerto Rico.
    if statenames[nshape] not in ('District of Columbia','Puerto Rico', 'Alaska', 'Hawaii'):
        color = rgb2hex(colors[statenames[nshape]]) 
        poly = Polygon(seg,facecolor=color,edgecolor=color)
        ax.add_patch(poly)
plt.title('Percentage of Bilingual People By State')

# legend https://stackoverflow.com/questions/2451264/creating-a-colormap-legend-in-matplotlib
plt.show()
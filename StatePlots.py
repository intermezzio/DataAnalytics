import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap as Basemap
from matplotlib.colors import rgb2hex
from matplotlib.patches import Polygon
import math

base = Basemap(llcrnrlon=-119,llcrnrlat=22,urcrnrlon=-64,urcrnrlat=49,
projection='lcc',lat_1=33,lat_2=45,lon_0=-95) # create background for plot
shp_info = base.readshapefile('StateMaps/st99_d00','states',drawbounds=True)
# map file with shapes for the states

colors = dict()
stNames = list() # names of states
cmap=plt.cm.nipy_spectral # color scheme

def stateGraph(data, minimum = 0, maximum = 100, title = "Hello World"):
    '''
    Make a state graph with your data!
    @param data: dictionary of data
    @param minimum: smallest value (on the scale) of the data
    @param maximum: largest value (on the scale) of the data
    @param title: plot title
    @return: void; pyplot is shown
         
    '''
    colorset = lambda x: 1.-(1.-np.sqrt((x-minimum)/(maximum-minimum)))
    # controls scale of the data
    global colors
    global stNames
    for shape in base.states_info:
        s = shape['NAME'] # name of each state
        if s not in ('District of Columbia','Puerto Rico', 'Alaska', 'Hawaii'): # remove unused states
            thisState = data[s]
            colors[s] = cmap(colorset(thisState))[:3] # set color for data
        stNames.append(s)

    ax = plt.gca() # axis
    for i, seg in enumerate(base.states):
        if stNames[i] not in ('District of Columbia','Puerto Rico', 'Alaska', 'Hawaii'):
            c = rgb2hex(colors[stNames[i]]) # choose color
            p = Polygon(seg,facecolor=c,edgecolor=c) # add state to diagram
            ax.add_patch(p)
    plt.title(title) # add title
    
    # legend https://stackoverflow.com/questions/2451264/creating-a-colormap-legend-in-matplotlib
    plt.imshow([[minimum,maximum]], origin="lower", cmap="nipy_spectral", interpolation='nearest')
    # add legend
    plt.colorbar() # show colorbar
    plt.show() # show plot
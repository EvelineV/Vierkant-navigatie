from mpl_toolkits.basemap import Basemap

import matplotlib.pyplot as plt
import matplotlib.cm

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize
import numpy as np
import pandas as pd

#!pip install geonamescache
from geonamescache import GeonamesCache

fig, ax = plt.subplots(figsize=(20,20))
westlimit=-10.81
southlimit=35.98
eastlimit=26.46
northlimit=60.92
m = Basemap(resolution='i', # c, l, i, h, f or None
            projection='merc',
            lat_0=54.5, lon_0=-4.36,
            llcrnrlon=westlimit, llcrnrlat=southlimit, urcrnrlon=eastlimit, urcrnrlat=northlimit)

watercolor='#46bcec'
landcolor='#f2f2f2'
m.drawmapboundary(fill_color=watercolor)
m.fillcontinents(color=landcolor,lake_color=watercolor)
m.drawcoastlines()
m.drawcountries(linewidth=0.25)
meridians = np.arange(0.,30.,15.)
m.drawmeridians(meridians,labels=[True, True, True])
plt.show()
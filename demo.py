import matplotlib.pyplot as plt
import matplotlib.cm

import geopandas
from mpl_toolkits.basemap import Basemap

from matplotlib.patches import Polygon
from matplotlib.collections import PatchCollection
from matplotlib.colors import Normalize

fig, ax = plt.subplots(figsize=(10,20))

m = Basemap(resolution='c', # c, l, i, h, f or None
            projection='merc',
            lat_0=-4.27 , lon_0=56.49,
            llcrnrlon=-7.95, llcrnrlat= 54.55, urcrnrlon=-0.41, urcrnrlat=60.78)

# m.drawmapboundary(fill_color='#46bcec')
# m.fillcontinents(color='#f2f2f2',lake_color='#46bcec')
# m.drawcoastlines()

# def plot_area(pos):
#     count = new_areas.loc[new_areas.pos == pos]['count']
#     x, y = m(pos[1], pos[0])
#     size = (count/1000) ** 2 + 3
#     m.plot(x, y, 'o', markersize=size, color='#444444', alpha=0.8)
#
# new_areas.pos.apply(plot_area)

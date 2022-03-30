# SOURCE: https://datashader.org/getting_started/Introduction.html

import datashader as ds
import pandas as pd
import colorcet as cc
from datashader.utils import export_image
from bokeh.plotting import figure, show


plot_width  = int(990)
plot_height = int(plot_width//1.2)


df = pd.read_csv("nyc_taxi.csv", usecols=["dropoff_x", "dropoff_y"])
print(df.head(), df.shape)


cvs = ds.Canvas()

agg = cvs.points(df, "dropoff_x", "dropoff_y")
img = ds.tf.set_background(ds.tf.shade(agg, cmap=cc.fire), "black")

# SAVE IMAGE
export_image(img, "out", background="black", export_path="./")


import holoviews as hv
from holoviews.element.tiles import EsriImagery
from holoviews.operation.datashader import datashade

hv.extension("bokeh")

# map_tiles  = EsriImagery().opts(alpha=0.5, width=900, height=480, bgcolor='black')
# map_tiles  = hv.element.tiles.EsriImagery().opts(width=600, height=550)

points     = hv.Points(df, ['dropoff_x', 'dropoff_y']) #.opts(fontscale=2, width=500, height=400, title='Title')
taxi_trips = datashade(points, x_sampling=1, y_sampling=1, cmap=cc.fire, width=100, height=100)

hv.save(taxi_trips, 'DS.html')
# show(taxi_trips)

# https://datashader.org/getting_started/Pipeline.html

import pandas as pd
import numpy as np
from collections import OrderedDict as odict

import datashader as ds
import datashader.transfer_functions as tf

import hvplot

import holoviews as hv
from holoviews.operation.datashader import datashade

hv.extension("bokeh")

# GENERATE DATA
num = 10000
np.random.seed(1)

dists = {
    cat: pd.DataFrame(
        odict(
            [
                ("x", np.random.normal(x, s, num)),
                ("y", np.random.normal(y, s, num)),
                ("val", val),
                ("cat", cat),
            ]
        )
    )
    for x, y, s, val, cat in [
        (2, 2, 0.03, 10, "d1"),
        (2, -2, 0.10, 20, "d2"),
        (-2, -2, 0.50, 30, "d3"),
        (-2, 2, 1.00, 40, "d4"),
        (0, 0, 3.00, 50, "d5"),
    ]
}

df = pd.concat(dists, ignore_index=True)
df["cat"] = df["cat"].astype("category")

print(df)


# PLOT-1

# out=datashade(hv.Points(df))
# print(type(out))
# hv.save(out, "DS-1.html")
# hvplot.show(out)

# Here, if you are running a live Python process,
# you can enable the “wheel zoom” tool on the right,
# zoom in anywhere in the distribution, and datashader
#  will render a new image that shows the full
#  distribution at that new location. If you are
#  viewing this on a static web site, zooming will
#   simply make the existing set of pixels larger,
#   because this dynamic updating requires Python.


# PLOT-2

canvas = ds.Canvas(
    plot_width=300,
    plot_height=300,
    x_range=(-8, 8),
    y_range=(-8, 8),
    x_axis_type="linear",
    y_axis_type="linear",
)

out=canvas.points(df, 'x', 'y', agg=ds.count())

print(out,type(out))

out=tf.Images(tf.shade(   canvas.points(df,'x','y', ds.count()),     name="count()"),
          tf.shade(   canvas.points(df,'x','y', ds.any()),       name="any()"),
          tf.shade(   canvas.points(df,'x','y', ds.mean('y')),   name="mean('y')"),
          tf.shade(50-canvas.points(df,'x','y', ds.mean('val')), name="50- mean('val')"))

print(out,type(out))

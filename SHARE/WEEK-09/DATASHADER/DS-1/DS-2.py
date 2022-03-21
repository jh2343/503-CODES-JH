#https://nbviewer.org/github/danbochman/Open-Source-Spotlight/blob/master/Datashader/Datashader.ipynb

from bokeh.models import BoxZoomTool
from bokeh.plotting import figure, output_notebook, show
import pandas as pd


output_notebook()

df = pd.read_csv('nyc_taxi.csv',usecols= \
                       ['pickup_x', 'pickup_y', 'dropoff_x','dropoff_y', 'passenger_count','tpep_pickup_datetime'])
df.tail()

# Define general parameters for the Bokeh plot
NYC = x_range, y_range = ((-8242000,-8210000), (4965000,4990000))

plot_width  = int(990)
plot_height = int(plot_width//1.2)

options = dict(line_color=None, fill_color='blue', size=5)


# Reusable function to create simple Bokeh plots

def base_plot(tools='pan,wheel_zoom,reset', plot_width=plot_width, plot_height=plot_height, **plot_kwargs):
    p = figure(tools=tools, plot_width=plot_width, plot_height=plot_height,
        x_range=x_range, y_range=y_range, outline_line_color=None,
        min_border=0, min_border_left=0, min_border_right=0,
        min_border_top=0, min_border_bottom=0, **plot_kwargs)
    
    p.axis.visible = False
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    
    p.add_tools(BoxZoomTool(match_aspect=True))
    
    return p


# from bokeh.tile_providers import STAMEN_TERRAIN

samples = df.sample(n=1000)
p = base_plot()
# p.add_tile(STAMEN_TERRAIN)
p.circle(x=samples['dropoff_x'], y=samples['dropoff_y'], **options)
show(p)
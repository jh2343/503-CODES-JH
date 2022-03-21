# IMPORT
import pandas as pd
import numpy as np
import holoviews as hv

# LOAD THE BOKEH PLOTTING EXTENSION,
hv.extension("bokeh")

# LOAD SOME BOKEH TOOLS
from bokeh.plotting import figure, show

# USE SEABORN TO GET SOME DATA
import seaborn as sns

df = sns.load_dataset("tips")
print(df)


# CREATE AN HV ELEMENT OBJECT CALLED SCATTER
# INDEPENDENT OF PLOTTING LIBRARY (BOKEH OR MPL)
scatter = hv.Scatter(df, "total_bill", "tip")
print("OBJECT:", scatter, type(scatter))

# AUTOMATICALLY RENDER USING BOKEH AND SAVE TO HTML
hv.save(scatter, "HV-1.html")

# SHOW (WILL ALSO SAVE FILE)
#show(hv.render(scatter))

# COMPOSITE OBJECT (SUBPLOT):
	# using the + operator, to create a new, compositional object
	# called a Layout built from our scatter
	# all the plotting is happening behind the scenes.
	# The layout is not a plot, it’s a new object that exists
	# independently of any given plotting system:

# UPDATA SCATTER OBJECT OPTIONS
scatter = scatter.opts(color="red")
histogram = hv.Histogram(
			np.histogram(df["total_bill"], bins=24), 
			kdims=["total_bill"]) #Axis label

layout = scatter + histogram
print("OBJECT:", layout, type(layout))

hv.save(layout, "HV-2.html")


# to save as HTML with no widget:
# hv.save(scatter.last, 'HV-1.html')

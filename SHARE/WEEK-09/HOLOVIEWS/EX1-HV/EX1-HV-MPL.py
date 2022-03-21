# IMPORT
import pandas as pd
import numpy as np
import holoviews as hv
import matplotlib.pyplot as plt


# LOAD THE BOKEH PLOTTING EXTENSION,
hv.extension("matplotlib")

# USE SEABORN TO GET SOME DATA
import seaborn as sns

df = sns.load_dataset("tips")
print(df)


# CREATE AN HV ELEMENT OBJECT CALLED SCATTER
# INDEPENDENT OF PLOTTING LIBRARY (BOKEH OR MPL)
scatter = hv.Scatter(df, "total_bill", "tip")
print("OBJECT:", scatter, type(scatter))

# AUTOMATICALLY RENDER USING BOKEH AND SAVE TO HTML
hv.save(scatter, "HV-3.png")


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

hv.save(layout, "HV-4.png")



# CONVERT TO MPL OBJECT WITH RENDER
# fig, ax = plt.subplots()
# fig = hv.render(scatter)
# # fig=fig1
# # ax=fig1.axes
# # print('Figure: ', fig1)
# # print('Axes:   ', fig1.axes)
# # plt.figure(fig)
# plt.show()

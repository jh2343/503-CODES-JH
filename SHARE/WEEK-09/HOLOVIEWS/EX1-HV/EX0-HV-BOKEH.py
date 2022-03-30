# IMPORT
import pandas as pd
import numpy as np
import holoviews as hv

# LOAD THE BOKEH PLOTTING EXTENSION,
hv.extension("bokeh")

# LOAD SOME BOKEH TOOLS
from bokeh.plotting import figure, show


# ------------------
# VARIOUS PLOTS
# ------------------

# GENERATE DATA
N = 10000
u=1.0
std1=1.25*u
x1 = np.random.normal(loc= u,scale=std1, size=N)
y1 = np.random.normal(loc= u,scale=std1, size=N)

x2 = np.random.normal(loc= u,scale=0.7*std1, size=N)
y2 = np.random.normal(loc=-u,scale=0.7*std1, size=N)

x3 = np.random.normal(loc=-u,scale=0.4*std1, size=N)
y3 = np.random.normal(loc= u,scale=0.4*std1, size=N)

x4 = np.random.normal(loc=-u,scale=0.1*std1, size=N)
y4 = np.random.normal(loc=-u,scale=0.1*std1, size=N)

# FORM DICTIONARY
D = {
    "x1": x1,
    "y1": y1,
    "x2": x2,
    "y2": y2,
    "x3": x3,
    "y3": y3,
    "x4": x4,
    "y4": y4,
    "x5": sorted(x1),
    "sin": np.sin(sorted(x1))
}

# SCATTER-1
hv1 = hv.Scatter(D, "x1", "y1")
# print(hv1, type(hv1))
hv.save(hv1, "SCATTER-1.html")  # RENDER+SAVE
# hv.save(hv1, "HV.html")  # RENDER+SAVE


# CUSTOMIZE
# https://holoviews.org/user_guide/Customizing_Plots.html
hv1 = hv.Scatter(D, "x1", "y1")
hv1 = hv1.opts(
			  color="blue",
			  alpha=0.1,
			  size=3,
			  title="Scatter",
			  bgcolor='white',
			  width=500, 
			  height=500,
			  fontsize=14,
			  xticks = 6, 
			  yticks = 12
			  )

hv.save(hv1, "SCATTER-2.html")  # RENDER+SAVE
# hv.save(hv1, "HV.html")  # RENDER+SAVE

# COMBINE
hv1 = hv.Scatter(D, "x1", "y1").opts(color="red")
hv2 = hv.Scatter(D, "x2", "y2").opts(color="red")
hv3 = hv.Scatter(D, "x3", "y3").opts(color="red")
hv4 = hv.Scatter(D, "x4", "y4").opts(color="red")
out = hv1 * hv2 * hv3 * hv4
# out = hv1 + hv2 + hv3 + hv4
hv.save(out, "SCATTER-3.html")  # RENDER+SAVE

# exit()
# COMBINE
hv1 = hv.Scatter(D, "x1", "y1") #.opts(color="blue")
hv2 = hv.Scatter(D, "x2", "y2") #.opts(color="red")
hv3 = hv.Scatter(D, "x3", "y3") #.opts(color="green")
hv4 = hv.Scatter(D, "x4", "y4") #.opts(color="black")
# out = hv1 * hv2 * hv3 * hv4
out = hv1 + hv2 + hv3 + hv4
hv.save(out, "SCATTER-4.html")  # RENDER+SAVE



# EXAMPLE
hv1 = hv.Scatter(D, "x1", "y1").opts(color="blue")
hv2 = hv.Scatter(D, "x2", "y2").opts(color="blue")
hv3 = hv.Scatter(D, "x3", "y3").opts(color="blue")
hv4 = hv.Scatter(D, "x4", "y4").opts(color="blue")
out = hv1 * hv2 * hv3 * hv4
hv.save(out, "SCATTER-5.html")  # RENDER+SAVE

hv1 = hv.Scatter(D, "x1", "y1").opts(color="blue",size=0.1,alpha=0.1)
hv2 = hv.Scatter(D, "x2", "y2").opts(color="blue",size=0.1,alpha=0.1)
hv3 = hv.Scatter(D, "x3", "y3").opts(color="blue",size=0.1,alpha=0.1)
hv4 = hv.Scatter(D, "x4", "y4").opts(color="blue",size=0.1,alpha=0.1)
out = hv1 * hv2 * hv3 * hv4
hv.save(out, "SCATTER-6.html")  # RENDER+SAVE

#MULTIPLOT-SCATTER
hv1 = hv.Scatter({'x':x1,'y':y1}, "x", "y")
hv1 = hv1.opts(color="red")
hv2 = hv.Scatter({'x':x2,'y':y2}, "x", "y")
hv_object=hv1+hv2
hv.save(hv_object, "SCATTER-7.html")

# VIOLIN
hv_object = hv.Violin(x1)
print(hv_object, type(hv_object))
hv.save(hv_object, "Violin.html")

# LINEPLOT-1
hv1 = hv.Curve(D, "x5", "sin")
hv.save(hv1, "Curve-1.html")  # RENDER+SAVE

# LINEPLOT-2
hv1=(hv.Curve([1, 2, 3], label='A') * hv.Curve([3, 2, 1], label='B')).opts(fontscale=2, width=500, height=400, title='Title')
hv.save(hv1, "Curve-2.html")  # RENDER+SAVE

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
# show(hv.render(scatter))

# COMPOSITE OBJECT (SUBPLOT):
# using the + operator, to create a new, compositional object
# called a Layout built from our scatter
# all the plotting is happening behind the scenes.
# The layout is not a plot, it’s a new object that exists
# independently of any given plotting system:

# UPDATA SCATTER OBJECT OPTIONS
scatter = scatter.opts(color="red")
histogram = hv.Histogram(
    np.histogram(df["total_bill"], bins=24), kdims=["total_bill"]
)  # Axis label

layout = scatter + histogram
print("OBJECT:", layout, type(layout))

hv.save(layout, "HV-2.html")


# to save as HTML with no widget:
# hv.save(scatter.last, 'HV-1.html')

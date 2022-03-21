import datashader as ds, pandas as pd, colorcet
# df  = pd.read_csv('census.csv')
# import pandas as pd
import matplotlib.pyplot as plt
from datashader.utils import export_image

#READ FULL DATASET
#pip install --user tables
# df = pd.read_hdf('./census.hdf'); #print(df.shape)

df = pd.read_csv('./census-smaller.csv'); #print(df.shape)


print(df.keys())
# #MAKE SMALL SUBSET
# df1=df.sample(int(0.1*df.shape[0]))
# df1.to_csv('census-smaller.csv',index=False)


#PLOT FULL
cvs = ds.Canvas(plot_width=850, plot_height=500)
agg = cvs.points(df, 'meterswest', 'metersnorth')
img = ds.tf.shade(agg, cmap=colorcet.fire, how='log')

export_image(img, "out", background="black", export_path="./")

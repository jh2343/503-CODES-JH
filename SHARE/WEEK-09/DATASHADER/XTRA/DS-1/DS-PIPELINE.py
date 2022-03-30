


import numpy as np
import pandas as pd
import matplotlib.pylab as plt

import datashader as ds
import datashader.transfer_functions as tf


N = 10000
df = pd.DataFrame(np.random.random((N, 3)), columns = ['x','y', 'z'])

f, ax = plt.subplots(2, 2)
ax_r = ax.ravel()

cvs = ds.Canvas(plot_width=100, plot_height=100)
agg = cvs.points(df, 'x', 'y', ds.mean('z'))
ax_r[0].add_artist(agg)

ax_r[1].hist(df['x'])
ax_r[2].hist(df['y'])
ax_r[3].plot(df['z'])

plt.tight_layout()
plt.show()



# import pandas as pd
# import numpy as np
# from collections import OrderedDict as odict

# num=10000
# np.random.seed(1)

# dists = {cat: pd.DataFrame(odict([('x',np.random.normal(x,s,num)), 
#                                   ('y',np.random.normal(y,s,num)), 
#                                   ('val',val), 
#                                   ('cat',cat)]))      
#          for x,  y,  s,  val, cat in 
#          [(  2,  2, 0.03, 10, "d1"), 
#           (  2, -2, 0.10, 20, "d2"), 
#           ( -2, -2, 0.50, 30, "d3"), 
#           ( -2,  2, 1.00, 40, "d4"), 
#           (  0,  0, 3.00, 50, "d5")] }

# df = pd.concat(dists,ignore_index=True)
# df["cat"]=df["cat"].astype("category")

# print(df.tail())


# import datashader as ds
# import datashader.transfer_functions as tf

# tf.shade(ds.Canvas().points(df,'x','y'))
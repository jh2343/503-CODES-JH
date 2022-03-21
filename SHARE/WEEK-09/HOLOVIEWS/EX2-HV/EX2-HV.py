#SOURCE: https://holoviews.org/getting_started/Introduction.html

import pandas as pd
import numpy as np
import holoviews as hv
from holoviews import opts

# load the bokeh plotting extension, 
# allowing us to generate visualizations with Bokeh
hv.extension('bokeh')

station_info = pd.read_csv('../holoviews-examples/assets/station_info.csv')
station_info.head()


#SCATTER PLOT
scatter = hv.Scatter(station_info, 'services', 'ridership')

#SAVE
hv.save(scatter, "HV-0.html")


#COMPOSITE OBJECT
scatter = scatter.opts(color="red")
layout = scatter + hv.Histogram(np.histogram(station_info['opened'], bins=24), kdims=['opened'])
hv.save(scatter, "HV-1.html")



#ARRAY DATA
taxi_dropoffs = {hour:arr for hour, arr in np.load('../holoviews-examples/assets/hourly_taxi_data.npz').items()}
print('Hours: {hours}'.format(hours=', '.join(taxi_dropoffs.keys())))
print('Taxi data contains {num} arrays (one per hour).\nDescription of the first array:\n'.format(num=len(taxi_dropoffs)))
np.info(taxi_dropoffs['0'])


bounds = (-74.05, 40.70, -73.90, 40.80)
image = hv.Image(taxi_dropoffs['0'], ['lon','lat'], bounds=bounds)


points = hv.Points(station_info, ['lon','lat']).opts(color="red")
out=image+image * points
hv.save(out, "HV-3.html")



dictionary = {int(hour):hv.Image(arr, ['lon','lat'], bounds=bounds) 
              for hour, arr in taxi_dropoffs.items()}
out=hv.HoloMap(dictionary, kdims='Hour')

hv.save(out, "HV-3.html")



holomap = hv.HoloMap(dictionary, kdims='Hour')
out=holomap.select(Hour={3,6,9}).layout()
hv.save(out, "HV.html")



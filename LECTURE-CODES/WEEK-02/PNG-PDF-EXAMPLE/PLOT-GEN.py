#-------------------------------------------
# SAVING A PLOT TO PNG AND PDF FORMATS
#-------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d #,spline 
import scipy.signal
import warnings
from matplotlib.ticker import FormatStrFormatter

warnings.filterwarnings("ignore") #supress all warnings

#GENERATE DATA
N=1002	#number of data points 
x=np.linspace(-45,45.0, N); 
#ye=np.sin(x) #exact
ye=x*x*np.sin(x) #exact
y=ye+np.random.normal(0, 100, N)	#add noise

#DEFINE
f = plt.figure()
f, ax = plt.subplots()

#AXES
FS=18	#FONT SIZE
plt.xlabel('Time (ps)', fontsize=FS)
plt.ylabel('Amplitude (cm)', fontsize=FS)
plt.xticks([-40,-20,0,20,40],fontsize=FS)
plt.yticks([-2000,-1000,0,1000,2000],fontsize=FS)

#PLOT
plt.plot(x, y,'.', markersize=16,color='black',markerfacecolor='white',label="Data") # ,color='black', markersize=8)
plt.plot(x,ye,'r-',linewidth=3,label="Generating function") 
ax.legend()

#PLOT RANGES
plt.xlim(min(x),0)

#CONTROL AXIS TICK FORMAT
ax.yaxis.set_major_formatter(FormatStrFormatter('%4.1f'))
ax.xaxis.set_major_formatter(FormatStrFormatter('%.0f'))

#SAVE IMAGES
f.savefig('plot-1.png', bbox_inches='tight')
f.savefig("plot-1.pdf", bbox_inches='tight')
f.savefig("plot-1.svg", bbox_inches='tight')

plt.show()


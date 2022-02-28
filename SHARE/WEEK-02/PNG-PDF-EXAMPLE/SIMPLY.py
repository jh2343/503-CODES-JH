#-------------------------------------------
# SAVING A PLOT TO PNG AND PDF FORMATS
#-------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

#GENERATE DATA
N=4	#number of data points 
x=np.linspace(0,5.0, N);
print(x) 
#ye=np.sin(x) #exact
ye=x #exact
y=x	#add noise

#DEFINE
f, ax = plt.subplots()

#PLOT
plt.plot(x, y,'.') 

#SAVE IMAGES
f.savefig('simply-1.png', bbox_inches='tight')
f.savefig("simply-1.pdf", bbox_inches='tight')
f.savefig("simply-1.svg", bbox_inches='tight')

plt.show()


##-------------------------------------------
## 2 VARIABLE NORMAL DISTIBUTION
##-------------------------------------------

import matplotlib.pyplot as plt
import numpy as np


#normal distribution param
ux=0.0; uy=0.0; uz=0.0
sx=1.0; sy=1.0; sz=1.0				#STD-DEV
rho=0.5; 							#[0,1) RHO=PEARSON CORRELATION
u1=np.array([[ux],[uy],[uz]]) 		#MEAN VECTOR u=[ux,uy,uz] 
s=np.array([
 [sx**2.0,rho*sx*sy,rho*sx*sz]
,[rho*sy*sx,sy**2.0,rho*sy*sz]
,[rho*sz*sx,rho*sz*sy,sz**2.0]])	#COVARIANCE METRIC
u2=np.array([[10],[10],[0]]) 		#MEAN VECTOR u=[ux,uy,uz] 

#GENERATE POINTS SAMPLED FROM DISTRIBUTION
x1, y1, z1= np.random.multivariate_normal(u1.reshape(3), s, 1000).T
x2, y2, z2= np.random.multivariate_normal(u2.reshape(3), 3*s, 1000).T

#SCATTER PLOT
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, y1, z1,
           linewidths=1, alpha=.7,
           edgecolor='k',
           s = 200,
           )
ax.scatter(x2, y2, z2,
           linewidths=1, alpha=.7,
           edgecolor='k',
           s = 200,
           )
plt.show()
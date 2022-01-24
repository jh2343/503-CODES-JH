

##-------------------------------------------
## 2 VARIABLE NORMAL DISTIBUTION
##-------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

#USER INPUTS
FUNC=2
FS=18	#FONT SIZE
CMAP='hsv' #'RdYlBu'

#normal distribution param
ux=0.0; uy=0.0
sx=1.0; sy=1.0 								#STD-DEV
rho=0.5; 									#[0,1) RHO=PEARSON CORRELATION
u=np.array([[ux],[uy]]) 					#MEAN VECTOR u=[ux,uy] 
s=np.array([[sx**2.0,rho*sy*sx],[rho*sy*sx,sy**2.0]])	#COVARIANCE METRIC

#GENERATE POINTS SAMPLED FROM DISTRIBUTION
xp, yp = np.random.multivariate_normal(u.reshape(2), s, 1000).T

# DEFINE FUNCTION 
def N(x, y):
	out=1.0/(2*3.1415*sx*sy*(1-rho**2.0)**0.5)
	out=out*np.exp(-(((x-ux)/sx)**2.0-2*rho*((x-ux)/sx)*((y-uy)/sy)+((y-uy)/sy)**2.0)/(2*(1-rho**2)))
	return out

#MESH-1 (SMALLER)
L=3*max(sx,sy)
xmin=-L; xmax=L; ymin=-L; ymax=L
x,y = np.meshgrid(np.linspace(xmin,xmax,20),np.linspace(ymin,ymax,20))

#MESH-2 (DENSER)
X, Y = np.meshgrid(np.linspace(xmin, xmax, 40), np.linspace(ymin, ymax, 40))

#SURFACE PLOT 
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.set_xlabel('x', fontsize=FS); ax.set_ylabel('y', fontsize=FS); ax.set_zlabel('p(x,y)', fontsize=FS)
surf=ax.plot_surface(X, Y, N(X, Y), cmap=CMAP) 
ax.scatter(xp, yp, 1.1*np.max(N(X, Y)) , '.')
plt.show(); 

#SCATTER PLOT
plt.plot(xp, yp,'.')

#CONTOUR PLOT 
# plt.axis('equal')
plt.contour(X, Y, N(X, Y), 20, cmap=CMAP); 
plt.show(); 


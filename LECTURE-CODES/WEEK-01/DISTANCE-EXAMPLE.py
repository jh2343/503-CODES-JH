##-------------------------------------------
## 2 VARIABLE NORMAL DISTIBUTION
##-------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


#GENERATE DATA
#normal distribution param
N=20
sx=1.0; sy=1.0; sz=1.0				#STD-DEV
rho=0.0; 							#[0,1) RHO=PEARSON CORRELATION
s=np.array([
 [sx**2.0,rho*sx*sy,rho*sx*sz]
,[rho*sy*sx,sy**2.0,rho*sy*sz]
,[rho*sz*sx,rho*sz*sy,sz**2.0]])	#COVARIANCE METRIC

#GENERATE POINTS SAMPLED FROM DIFFERENT 3D NORMAL DISTRIBUTION
X1 = np.random.multivariate_normal([0,0,0],  s, N) 
X2 = np.random.multivariate_normal([25,0,0], s, N) 
X3 = np.random.multivariate_normal([50,0,0], s, N) 
X4 = np.random.multivariate_normal([75,0,0], s, N) 

#COMBINE
X=np.concatenate((X1,X2,X3,X4),axis=0)
# print(X.shape,X1.shape,X2.shape)

#RANDOMIZE ROWS (REMOVE ORDER)
np.random.shuffle(X)

#INITIALIZE MATRIX 
DIJ=np.zeros(X.shape[0]*X.shape[0]).reshape(X.shape[0],X.shape[0])

#COMPUTE DISTANCES
for i in range(0,X.shape[0]):
    for j in range(0,X.shape[0]):
        dij=0
        for dim in range(X.shape[1]):
            #print(i,j,dim)
            dij=dij+(X[i,dim]-X[j,dim])**2.0
        dij=dij**0.5
        DIJ[i,j]= dij
        #print(i,j,dij)

#NORMALIZE
DIJ=DIJ/np.max(DIJ)

#SORT EACH ROW INDEPENTLY (LOSE ORDER)
DIJ.sort(axis=1)
DIJ.sort(axis=0)

#PLOT 
ax = sns.heatmap(DIJ, linewidth=0.1)
plt.show(); exit()

#SCATTER PLOT
fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(X1[:,0], X1[:,1], X1[:,2],
           linewidths=1, alpha=.7,
           edgecolor='k',
           s = 200,
           )
ax.scatter(X2[:,0], X2[:,1], X2[:,2],
           linewidths=1, alpha=.7,
           edgecolor='k',
           s = 200,
           )
ax.scatter(X3[:,0], X3[:,1], X3[:,2],
           linewidths=1, alpha=.7,
           edgecolor='k',
           s = 200,
           )
ax.scatter(X4[:,0], X4[:,1], X3[:,2],
           linewidths=1, alpha=.7,
           edgecolor='k',
           s = 200,
           )

plt.show()

# plt.imshow(DIJ, cmap='hot')
# plt.show()



# #SORT EACH ROW (LOSE ORDER)
# a = np.array([[3,2,1], [3,1,2]])
# print(a)
# a.sort(axis=1)
# print(a)
# exit()
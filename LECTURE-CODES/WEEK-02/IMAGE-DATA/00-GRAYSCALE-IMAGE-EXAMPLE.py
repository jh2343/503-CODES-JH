# #------------------------
# #LOW RES GRAYSCALE IMAGE 
# #------------------------

import numpy as np
import matplotlib.pyplot as plt

#DEFINE IMAGE (HAND WRITTEN DIGIT 5)
x=[[0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0   ,0],
 [  0   ,0   ,0   ,1   ,5   ,14  ,28  ,38  ,18  ,0],
 [  0   ,0   ,25  ,140 ,190 ,207 ,162 ,124 ,38  ,0],
 [  0   ,0   ,13  ,108 ,204 ,58  ,40  ,1   ,0   ,0],
 [  0   ,0   ,0   ,5   ,136 ,72  ,8   ,0   ,0   ,0],
 [  0   ,0   ,0   ,0   ,16  ,142 ,143 ,11  ,0   ,0],
 [  0   ,0   ,0   ,0   ,18  ,101 ,219 ,39  ,0   ,0],
 [  0   ,0   ,19  ,86  ,196 ,188 ,80  ,4   ,0   ,0],
 [  0   ,52  ,176 ,183 ,95 , 11  ,0   ,0   ,0   ,0],
 [  0   ,2   ,7   ,3   ,0   ,0   ,0   ,0   ,0   ,0]]
x=np.array(x)

#QUICK INFO ON IMAGE
def get_info(image):
    print("------------------------")
    print("IMAGE INFO")
    print("------------------------")
    print("TYPE:",type(image))
    print("SHAPE:",image.shape)
    print("NUMBER OF PIXELS:",image.shape[0]*image.shape[1])
    print("NUMBER OF ENTRIES:",image.size)
    # print("N CHANNELS",image.shape[2])
    print("MIN:", image.min())
    print("MAX:", image.max())
    print("TYPE:",image.dtype)
    print("pixel-1 :", image[0,0])
    # print("image[0:3].shape:", image[0:3].shape)

get_info(x)

#BASIC SLICING AND PLOTS
print(x[0,0],x[0,9],x[9,0])
print(x[:,4])
print(x[4,:])

#SHOW IMAGES
plt.imshow(x, cmap=plt.cm.gray); plt.show()
plt.imshow([x[4,:]], cmap=plt.cm.gray); plt.show()
plt.imshow(np.array([x[:,4]]).reshape(10,1), cmap=plt.cm.gray); plt.show()

#SURFACE PLOT
def surface_plot(image):
    # create the x and y coordinate arrays (here we just use pixel indices)
    xx, yy = np.mgrid[0:image.shape[0], 0:image.shape[1]]
    fig = plt.figure()
    ax = fig.gca(projection='3d') #viridis
    ax.plot_surface(xx, yy, image[:,:] ,rstride=1, cstride=1, cmap=plt.cm.gray,linewidth=0)
    plt.show()

surface_plot(x)

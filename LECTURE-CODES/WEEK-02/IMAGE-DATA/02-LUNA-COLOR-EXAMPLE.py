
import numpy as np
import matplotlib.pyplot as plt
#conda install scikit-image

#LOAD IMAGE
x=plt.imread('luna-2.jpeg')

# #SHOW ORIGINAL IMAGE
plt.imshow(x); plt.show()

#ROTATE BY SWITCHING X AND Y DIMENSIONS
x=np.transpose(x,axes=[1,0,2])
plt.imshow(x); plt.show()



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
# print(x[0,0],x[0,9],x[9,0])
# print(x[:,4])
# print(x[4,:])

#CROP
plt.imshow(x[0:int(0.45*x.shape[0]),:]); plt.show()
plt.imshow(x[:,0:int(0.45*x.shape[0])]); plt.show()
# exit()


#SURFACE PLOT
def surface_plot(image):
    # create the x and y coordinate arrays (here we just use pixel indices)
    xx, yy = np.mgrid[0:image.shape[0], 0:image.shape[1]]
    fig = plt.figure()
    ax = fig.gca(projection='3d') #viridis
    ax.plot_surface(xx, yy, image[:,:] ,rstride=1, cstride=1, cmap=plt.cm.gray,linewidth=0)
    plt.show()


#REDUCE RESOLUTION-1
from skimage.transform import rescale, resize, downscale_local_mean
factor=50
x = resize(x, (x.shape[0] // factor, x.shape[1] // factor), anti_aliasing=True)
get_info(x)
plt.imshow(x); plt.show()
# exit()
# #SURFACE PLOT
from skimage.color import rgb2gray 
tmp=rgb2gray(x)
surface_plot(tmp)


#APPLY FILTER
def filter(x):
    # filter_ED=[[-1,-1,-1],[-1,8,-1],[-1,-1,-1]]
    # filter_ED=[[0,-1,0],[-1,4,-1],[0,-1,0]]
    # filter_ED=np.array([[1,2,1],[2,4,2],[1,2,1]])/16.0
    filter_ED=[[0,-1,0],[-1,5,-1],[0,-1,0]]

    tmp=np.copy(x)
    for channel in range(0,x.shape[2]):
        for i in range(1,x.shape[0]-1):
          for j in range(1,x.shape[1]-1):
            sub=x[:,:,channel]
            sub_matrix=sub[i-1:i+2,j-1:j+2] 
            tmp[i,j,channel]=np.sum(filter_ED*sub_matrix)

    # tmp=tmp.astype(int)
    return tmp

x=filter(x)
get_info(x)
plt.imshow(x); plt.show()



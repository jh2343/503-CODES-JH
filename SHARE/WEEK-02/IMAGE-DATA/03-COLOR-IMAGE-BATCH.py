import numpy as np
import matplotlib.pyplot as plt

#----------------------------------
#SINGLE IMAGE
#----------------------------------

print('---------SINGLE IMAGE------------')

nx=50  #number of pixels in x
ny=25  #number of pixels in y
channels=3

#GENERATE IMAGE
#HEIGHT,WIDTH
x =(np.random.uniform(0,255,nx*ny*channels).reshape(ny,nx,channels)).astype(int)
plt.imshow(x, cmap=plt.cm.gray); plt.show()


#QUICK INFO ON IMAGE
def get_info(image):
    print("------------------------")
    print("IMAGE INFO")
    print("------------------------")
    print("TYPE:",type(image))
    print("SHAPE:",image.shape)
    print("NUMBER OF PIXELS:",image.shape[0]*image.shape[1])
    print("NUMBER OF MATRIX ENTRIES:",image.size)
    # print("N CHANNELS",image.shape[2])
    print("MIN:", image.min())
    print("MAX:", image.max())
    print("TYPE:",image.dtype)
    print("pixel-1 :", image[0,0])
    # print("image[0:3].shape:", image[0:3].shape)
get_info(x)

#BASIC SLICING
# print(x[:,2])
# print(x[2,:])

#SHOW SUB-REGION IMAGE
plt.imshow(x[2:10,:], cmap=plt.cm.gray); plt.show()
plt.imshow(x[:,2:10], cmap=plt.cm.gray); plt.show()

#----------------------------------
# BATCH OF N GRAYSCALE NOISE SAMPLES
#----------------------------------

print('---------BATCH OF IMAGES------------')

Nsample=40

#GENERATE DATA MATRIX: SAMPLE,HEIGHT,WIDTH
X =(np.random.uniform(0,255,Nsample*nx*ny*channels).reshape(Nsample,ny,nx,channels)).astype(int)
print(X.shape)

#PLOT STATIC
for i in range(0,X.shape[0]):
    plt.imshow(X[i], cmap=plt.cm.gray); 
    plt.show(block=False)
    plt.pause(0.1)


# plt.close()

#CODE MODIFIED FROM:
# chollet-deep-learning-in-python

import numpy as np
from pandas import DataFrame
import time

#------------------------
#EXPLORE IMAGE
#------------------------
ipause=False 
#QUICK INFO ON NP ARRAY
def get_info(X,MESSAGE='SUMMARY'):
	print("\n------------------------")
	print(MESSAGE)
	print("------------------------")
	print("TYPE:",type(X))

	if(str(type(x))=="<class 'numpy.ndarray'>"):

		print("SHAPE:",X.shape)
		print("MIN:",X.min())
		print("MAX:",X.max())
		#NOTE: ADD SLICEING
		print("DTYPE:",X.dtype)
		print("NDIM:",X.ndim)
		print("IS CONTIGUOUS:",X.data.contiguous)
		#PRETTY PRINT 
		if(X.ndim==1 or X.ndim==2 ): 
			print("MATRIX:")
			print(DataFrame(X).to_string(index=False, header=False))
			# print("EDGES ARE INDICES: i=row,j=col") 
			# print(DataFrame(X)) 	
		if(ipause):  time.sleep(3)
	else:
		print("ERROR: INPUT IS NOT A NUMPY ARRAY")

#SCALAR (0D TENSOR)
x = np.array(10); get_info(x)

#VECTOR AS 1D ARRARY
x = np.array([12, 3, 6, 14]); get_info(x)

#VECTOR AS 2D ARRAY 
x = np.array([12, 3, 6, 14]);  x=x.reshape(len(x),1); get_info(x) #COLUMN VECTOR
x = np.array([12, 3., 6, 14]); x=x.reshape(1,len(x)); get_info(x) #ROW VECTOR

#MATRIX (RANK-2 TENSOR)
x = np.array([[5, 78, 2, 34, 0],
              [6, 79, 3, 35, 1],
              [7, 80, 4, 36, 2]]); get_info(x)

#RANK-3 TENSOR
x = np.array([[[5., 78, 2, 34, 0],
			   [6, 79, 3, 35, 1],
			   [7, 80, 4, 36, 2]],
			  [[5, 78, 2, 34, 0],
			   [6, 79, 3, 35, 1],
			   [7, 80, 4, 36, 2]],
			  [[5, 78, 2, 34, 0],
			   [6, 79, 3, 35, 1],
			   [7, 80, 4, 36, 2]]]) ; get_info(x,"3D TENSOR")

# #TRANSPOSE
x = np.array([[11, 12, 13],
            [21, 22, 23]]); 
get_info(x, "BEFORE TRANSPOSE")
get_info(np.transpose(x), "AFTER  TRANSPOSE")

#SLICING
x = np.array([[11, 12, 13, 14],
              [21, 22, 23, 24],
              [31, 32, 33, 34],
              [41, 42, 43, 44], 
              [51, 52, 53, 54]]); 

#NOTICE HOW ITS INCLUSIVE ON THE LEFT
#AND EXCLUSIVE ON THE RIGHT
get_info(x, "BEFORE SLICING")
get_info(x[:,1], 	"SLICE-1: x[:,1]")
get_info(x[2,:], 	"SLICE-2: x[2,:]")
get_info(x[1:3], 	"SLICE-3: x[1:3]")
get_info(x[:,-3:-1],"SLICE-4: x[:,-3:-1]")
get_info(x[:,0:2], 	"SLICE-5: x[:,0:2]")

#BROADCAST
get_info(x, "BEFORE BROADCAST")
get_info(x+1000, "ADD 1000 TO ALL")
get_info(x+x[0,:], "ADD FIRST ROW TO EACH ROW")

#RESHAPING 
get_info(x.reshape(x.shape[0]*x.shape[1],1), "x.reshape(x.shape[0]*x.shape[1],1)")
get_info(x.reshape(1,x.shape[0]*x.shape[1]), "x.reshape(1,x.shape[0]*x.shape[1])")
get_info(x.reshape(int(x.shape[0]*x.shape[1]/2),2), "x.reshape(int(x.shape[0]*x.shape[1]/2),2)")

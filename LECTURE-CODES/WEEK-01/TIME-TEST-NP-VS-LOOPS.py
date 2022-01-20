

#CODE MODIFIED FROM:
# chollet-deep-learning-in-python

import numpy as np
import time


# #COMPARE TIMES FOR NUMPY (VECTORIZED) VS LOOPS
def naive_add(x, y):
    assert len(x.shape) == 2
    assert x.shape == y.shape
    x = x.copy()
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            x[i, j] += y[i, j]
    return x


# #MAKE BIGGISH ARRAYS
x = np.random.random((100, 1000))
y = np.random.random((100, 1000))

# #NOTICE THAT THEY ARE CONTIGOUS IN MEMOERY
print("IS CONTIGUOUS:",x.data.contiguous)
print("IS CONTIGUOUS:",y.data.contiguous)


#ADD THEM 1000 TIMES WITH NUMPY (VECTORIZED)
num_add=1000
t0 = time.time()
for _ in range(num_add):
    z = x + y
time_numpy=time.time() - t0
print("NUMPY took: {0:.4f} s".format(time_numpy))

time.sleep(5)

#ADD THEM 1000 TIMES WITH LOOPS
t0 = time.time()
for _ in range(num_add):
    z = naive_add(x, y)
time_loop=time.time() - t0
print("LOOPS took: {0:.4f} s".format(time_loop))
print("Numpy is ",time_loop/time_numpy," X FASTER")



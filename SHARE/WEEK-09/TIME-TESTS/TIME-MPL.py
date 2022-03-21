import matplotlib.pyplot as plt
import numpy as np
import time

N_i=[]; T_i=[]
for i in range(1,26):

	N=2**i
	# Data for plotting
	t = np.linspace(0.0, 2*np.pi, N)
	s = np.sin(2 * np.pi * t)

	#START TIME
	to = time.process_time()

	fig, ax = plt.subplots()
	ax.plot(t, s,'-o')

	ax.set(xlabel='time (s)', ylabel='sin(x)')
	ax.grid()
	fig.savefig("test.png")
	# plt.show()

	#REPORT TIME NEEDED TO PLOT
	tf=time.process_time() - to
	print(i,N,np.round(tf,2))
	N_i.append(N); T_i.append(tf)

	#ONLY SHOW NEXT PLOT
	plt.close("all") #this is the line to be added

#PLOT N VS TIME
fig, ax = plt.subplots()
ax.plot(N_i, T_i,'-o')
ax.set(xlabel='Number of points', ylabel='Time (s)')
ax.grid()
plt.show()

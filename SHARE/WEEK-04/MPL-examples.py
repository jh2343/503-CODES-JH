

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#RUN ONE
# examples=['logscale']

#RUN ALL
examples=[
'basic-1',
'basic-2',
'subplots-1',
'customization-1',
'logscale',
'sparklines-1',
'sparklines-2',
'small-multiples','3D-plot-1',
'logscale','bar-1','annimation-1','annimation-2']


##SIMPLE STATIC 1D PLOT 
if('basic-1' in examples):
	plt.plot([1, 2, 3, 4],[1, 2, 3, 4],'o')

	#SET FIGURE LABELS 
	FS=18	 
	plt.xlabel('x', fontsize=FS)
	plt.ylabel('y', fontsize=FS)
	plt.show()
	#exit()

##SIMPLE STATIC 1D PLOT 
if('basic-2' in examples):
	#GENERATE DATA
	x = np.linspace(0, 10,200)
	y  = np.sin(x)
	y1 = y + np.random.normal(0, 0.5, len(x)) #ADD NOISE

	#DEFINE FIX+AX OBJECTS 
	fig, ax = plt.subplots()
	ax.plot(x,y1,'o')
	ax.plot(x,y,'-')
	ax.set_title('Basic plot')
	ax.set_xlabel('x', fontsize=14)
	ax.set_ylabel('y', fontsize=14)
	plt.show()

##SIMPLE SUB-PLOT
if('subplots-1' in examples):
	#SOURCE: https://towardsdatascience.com/what-are-the-plt-
	#and-ax-in-matplotlib-exactly-d2cf4bf164a9
	n_rows = 2
	n_cols = 2
	#FIGURE --> CANVAS   AXES --> CELLS
	fig, axes = plt.subplots(n_rows, n_cols)
	for row_num in range(n_rows):
		for col_num in range(n_cols):
			#AXES (CELL) ATTRIBUTES
			ax_ij = axes[row_num][col_num]
			ax_ij.plot(np.random.rand(20))
			ax_ij.set_title(f'Plot ({row_num}, {col_num})')
			ax_ij.set_xlabel('x', fontsize=14)
			ax_ij.set_ylabel('y', fontsize=14)
			# ax_ij.legend(fontsize=12)

	#FIGURE ATTRIBUTES
	fig.suptitle('Main title')
	fig.tight_layout()
	plt.show()

#CUSTOMIZATION
if('customization-1' in examples):

	#GENERATE DATA
	N=500	#number of data points 
	x=np.linspace(-45,45.0, N); 
	ye=x*x*np.sin(x) #exact
	y=ye+np.random.normal(0, 200, N)	#add noise

	#USER PARAM
	FS=17


	#DEFINE FIG+AX OBJECTS 
	f, ax = plt.subplots()
	#https://www.canva.com/colors/color-wheel/
	ax.plot(x,y,'o',color='#FF0012', markersize=16, label='Data')
	ax.plot(x,ye, color='#0012FF'  ,linewidth=6, label='Ground truth')
	ax.plot(x,ye,color='#12FF00'   , linewidth=1, linestyle='dashed')

	#SET LEGEND
	ax.legend(fontsize=FS)

	#SET FIGURE SIZE
	f.set_size_inches(10, 10)

	#FIGURE TITLE
	f.suptitle('Decaying oscillations', fontsize=24)

	#AXIS LABELS
	ax.set_xlabel('Time (ps)', fontsize=FS)
	ax.set_ylabel('Amplitude (cm)', fontsize=FS)

	# #X-Y PLOT RANGE
	ax.set_xlim([-40,0])
	ax.set_ylim([-1750,1750])

	#AXIS TIC VALUES
	ax.set_xticks([-40,-30,-20,-10,0],fontsize=20)
	ax.set_yticks([-2000,-1000,0,1000,2000],fontsize=20)

	#CONTROL AXIS TICK FORMAT
	ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%4.2f'))
	ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

	#AXIS TIC FONT SIZE
	ax.tick_params(axis='both', which='major', labelsize=FS)
	ax.tick_params(axis='both', which='minor', labelsize=FS)

	#SAVE IMAGES
	f.savefig('plot-1.png', bbox_inches='tight')
	f.savefig("plot-1.pdf", bbox_inches='tight')
	f.savefig("plot-1.eps", bbox_inches='tight')

	#RENDER AND SHOW IMAGE
	plt.show()


if('logscale' in examples):

	#DEFINE DATA
	x = np.linspace(0.1, 100,1000)
	y1  = 10**x
	y2  = x
	y3  = np.log10(x)

	#DEFINE FIG+AX OBJECTS 
	fig, axes = plt.subplots(2, 2)

	#LINEAR SCALES
	ax  = axes[0][0]
	ax.set_yscale('linear')
	ax.set_xscale('linear')
	ax.set_xlim([0.1,10])
	ax.set_ylim([0.1,10])
	ax.set_aspect('equal')
	ax.plot(x,y1,x,y2,x,y3)

	#LOG SCALE ON X
	#SIMILAR TO: y=f(x) --> f(log(x))
	ax  = axes[0][1]
	ax.set_yscale('log')
	ax.set_xscale('linear')
	ax.set_xlim([0,5])
	ax.set_ylim([0.1,100])
	ax.plot(x,y1,x,y2,x,y3)

	#LOG SCALE ON Y
	#SIMILAR TO: y=f(x) --> log(y) 
	ax  = axes[1][0]
	ax.set_xscale('log')
	ax.set_yscale('linear')
	ax.set_xlim([0.1,5])
	ax.set_ylim([0.1,3])
	ax.plot(x,y1,x,y2,x,y3)

	#LOG SCALE ON BOTH
	ax  = axes[1][1]
	ax.set_yscale('log')
	ax.set_xscale('log')
	ax.set_xlim([0.1,10])
	ax.set_ylim([0.1,10])
	ax.plot(x,y1,x,y2,x,y3)

	#RENDER
	plt.show()


if('sparklines-1' in examples):
	#https://stackoverflow.com/questions/27543605/creating-sparklines-using-matplotlib-in-python
	import matplotlib.pyplot as plt
	import numpy as np


	data = np.cumsum(np.random.rand(1000)-0.5)
	data = data - np.mean(data)

	fig = plt.figure()
	ax1 = fig.add_subplot(411) # nrows, ncols, plot_number, top sparkline
	ax1.plot(data, 'b-')
	ax1.axhline(c='grey', alpha=0.5)

	ax2 = fig.add_subplot(412, sharex=ax1) 
	ax2.plot(data, 'g-')
	ax2.axhline(c='grey', alpha=0.5)

	ax3 = fig.add_subplot(413, sharex=ax1)
	ax3.plot(data, 'y-')
	ax3.axhline(c='grey', alpha=0.5)

	ax4 = fig.add_subplot(414, sharex=ax1) # bottom sparkline
	ax4.plot(data, 'r-')
	ax4.axhline(c='grey', alpha=0.5)

	for axes in [ax1, ax2, ax3, ax4]: # remove all borders
	    plt.setp(axes.get_xticklabels(), visible=False)
	    plt.setp(axes.get_yticklabels(), visible=False)
	    plt.setp(axes.get_xticklines(), visible=False)
	    plt.setp(axes.get_yticklines(), visible=False)
	    plt.setp(axes.spines.values(), visible=False)


	# bottom sparkline
	plt.setp(ax4.get_xticklabels(), visible=True)
	plt.setp(ax4.get_xticklines(), visible=True)
	ax4.xaxis.tick_bottom() # but onlyt the lower x ticks not x ticks at the top

	plt.tight_layout()
	plt.show()


if('sparklines-2' in examples):

	# create some random data
	x = np.cumsum(np.random.rand(1000)-0.5)

	# plot it
	fig, ax = plt.subplots(1,1,figsize=(10,3))
	plt.plot(x, color='k')
	plt.plot(len(x)-1, x[-1], color='r', marker='o')

	# remove all the axes
	for k,v in ax.spines.items():
	    v.set_visible(False)
	ax.set_xticks([])
	ax.set_yticks([])

	#show it
	plt.show()


if('small-multiples' in examples):

	#https://www.python-graph-gallery.com/125-small-multiples-for-line-chart

	# libraries
	import matplotlib.pyplot as plt
	import numpy as np
	import pandas as pd
	 
	# Make a data frame
	df=pd.DataFrame({'x': range(1,11), 'y1': np.random.randn(10), 'y2': np.random.randn(10)+range(1,11), 'y3': np.random.randn(10)+range(11,21), 'y4': np.random.randn(10)+range(6,16), 'y5': np.random.randn(10)+range(4,14)+(0,0,0,0,0,0,0,-3,-8,-6), 'y6': np.random.randn(10)+range(2,12), 'y7': np.random.randn(10)+range(5,15), 'y8': np.random.randn(10)+range(4,14), 'y9': np.random.randn(10)+range(4,14) })
	 
	# Initialize the figure style
	plt.style.use('seaborn-darkgrid')
	 
	# create a color palette
	palette = plt.get_cmap('Set1')
	 
	# multiple line plot
	num=0
	for column in df.drop('x', axis=1):
	    num+=1
	 
	    # Find the right spot on the plot
	    plt.subplot(3,3, num)
	 
	    # plot every group, but discrete
	    for v in df.drop('x', axis=1):
	        plt.plot(df['x'], df[v], marker='', color='grey', linewidth=0.6, alpha=0.3)
	 
	    # Plot the lineplot
	    plt.plot(df['x'], df[column], marker='', color=palette(num), linewidth=2.4, alpha=0.9, label=column)
	 
	    # Same limits for every chart
	    plt.xlim(0,10)
	    plt.ylim(-2,22)
	 
	    # Not ticks everywhere
	    if num in range(7) :
	        plt.tick_params(labelbottom='off')
	    if num not in [1,4,7] :
	        plt.tick_params(labelleft='off')
	 
	    # Add title
	    plt.title(column, loc='left', fontsize=12, fontweight=0, color=palette(num) )

	# general title
	plt.suptitle("How the 9 students improved\nthese past few days?", fontsize=13, fontweight=0, color='black', style='italic', y=1.02)
	 
	# Axis titles
	plt.text(0.5, 0.02, 'Time', ha='center', va='center')
	plt.text(0.06, 0.5, 'Note', ha='center', va='center', rotation='vertical')

	# Show the graph
	plt.show()


if('3D-plot-1' in examples):

	import matplotlib.pyplot as plt
	import numpy as np

	#3D 
	from matplotlib import cm
	from mpl_toolkits.mplot3d import Axes3D


	def fun(x, y):
		#print(x.shape)
		#return np.sin(x)*np.sin(y)
		return np.exp(-((x-1)/0.75)**2)*np.exp(-(y/1.5)**2)
		#TODO: ADD MULTIVARIABLE GAUSSIAN WITH NON IDENTITY COVARIANCE MATRIX

	#DEFINE FIGURE
	fig = plt.figure(figsize=(15,15))
	ax = fig.add_subplot(111, projection='3d')

	#DEFINE MESH FOR PLOTING
	# np.arange --> Return evenly spaced values within a given interval.
	xbound=4; dx=0.2; x = np.arange(-xbound,xbound, dx)
	ybound=4; dy=0.2; y = np.arange(-ybound,ybound, dy)

	#MERGE ARRAYS INTO 2D MESH
	#np.meshgrid Return coordinate matrices from coordinate vectors.
	X, Y = np.meshgrid(x, y)

	#TO BETTER UNDERSTAND MESH, SET dx=dy=2 AND UNCOMMENT
	# print(x.shape,y.shape,X.shape,Y.shape)
	# print(x,y)
	# print(X)
	# print(Y)

	#CONVERT MESH MATRIX TO VECTOR AND EVALUTE FUNCTION ON MESH COMPONENT WISE
	zs = np.array(fun(np.ravel(X), np.ravel(Y)))
	Z = zs.reshape(X.shape) #RESHAPE TO MATCH ORIGINAL MESH

	#3D PLOTS 
	#ax.scatter(X, Y, Z+0.001, marker='o') # RAW DATA
	# ax.contour3D(X, Y, Z, 50, cmap='binary') #CONTOUR

	zshift=1 #shift for visulization

	surf=ax.plot_surface(X, Y, Z+zshift, cmap=cm.coolwarm) #INTERPOLATED ONTO SMOOTH SURFACE AND APPLY COLOR MAP  
	num_contour=5

	#CONTOUR PROJECTIONS ON AXIS 
	cset = ax.contourf(X, Y, Z+zshift, num_contour, zdir='z', offset=np.min(Z), cmap=cm.coolwarm)
	cset = ax.contourf(X, Y, Z+zshift, zdir='x', offset=-xbound, cmap=cm.coolwarm)
	cset = ax.contourf(X, Y, Z+zshift, zdir='y', offset=xbound, cmap=cm.coolwarm)
	fig.colorbar(surf, ax=ax, shrink=0.5, aspect=5)

	#AXIS RANGE
	ax.set_zlim(0,np.max(Z)+1.5*zshift)


	FS=18	#FONT SIZE
	plt.xticks(fontsize=FS); plt.yticks(fontsize=FS);  

	ax.set_xlabel('X', fontsize=FS)
	ax.set_ylabel('Y', fontsize=FS)
	ax.set_zlabel('Z', fontsize=FS)

	plt.show()


if('annimation-1' in examples):

	import numpy as np
	import matplotlib.pyplot as plt

	#PARAMETERS
	dt=0.01		#time to pause between frames in seconds 
	x0=0.0; dx=0.1  #mesh parameters
	Nframe=100 

	plt.figure() #INITIALIZE FIGURE 
	FS=18
	plt.xlabel('Time (s)', fontsize=FS)
	plt.ylabel('Amplitude (cm)', fontsize=FS)
	for i in range(0,Nframe):
		x=x0+i*dx; y=np.sin(x)
		plt.plot(x,y,'bo')
		plt.pause(dt)

	plt.show()




if('bar-1' in examples):

	import matplotlib.pyplot as plt


	labels = ['G1', 'G2', 'G3', 'G4', 'G5']
	men_means = [20, 35, 30, 35, 27]
	women_means = [25, 32, 34, 20, 25]
	men_std = [2, 3, 4, 1, 2]
	women_std = [3, 5, 2, 3, 3]
	width = 0.35       # the width of the bars: can also be len(x) sequence

	fig, ax = plt.subplots()

	ax.bar(labels, men_means, width, yerr=men_std, label='Men')
	ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means,
	       label='Women')

	ax.set_ylabel('Scores')
	ax.set_title('Scores by group and gender')
	ax.legend()

	plt.show()


if('annimation-2' in examples):

	import numpy as np
	import matplotlib.pyplot as plt
	import time

	#PARAMETERS
	dt=0.005		#time to pause between frames in seconds 
	NP=100 

	x = np.linspace(0,10,NP)
	y = np.exp(-0.1*x)*np.sin(5*x)

	plt.ion()  #Enable interactive mode.
	fig,ax = plt.subplots(3,1,figsize=(15,15))
	ax[0].plot(x,y,'-')
	ax[1].plot(x,y,'-',)

	plt.show()

	for i in range(0,len(x)):

		ax[0].clear()

		ax[0].plot(x,y,'-'); ax[0].plot(x[i],y[i],'bo')
		ax[1].plot(x[i],y[i],'ro')
		ax[2].plot(x[i],y[i],'ro')

		plt.draw()
		plt.pause(dt)
	exit()





# import numpy as np

# x=np.linspace(0,0.25*2*np.pi,100)
# y1=np.sin(x)
# y2=np.cos(x)

# print(sum(y1*y2))
# print(np.dot(y1,y2))
# # import matplotlib as mpl
# # import matplotlib.pyplot as plt
# # import numpy as np



# # examples=['basic']


# # # The simplest way of creating a Figure with an
# # # Axes is using pyplot.subplots
# # if('basic' in examples):
# # 	fig, ax = plt.subplots()  # Create a figure containing a single axes.
# # 	ax.plot([1, 2, 3, 4], [1, 4, 2, 3]);  # Plot some data on the axes.
# # 	plt.show()





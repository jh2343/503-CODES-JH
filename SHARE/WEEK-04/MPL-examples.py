

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#RUN ONE
examples=['logscale']

#RUN ALL
# examples=[
# 'basic-1',
# 'basic-2',
# 'subplots-1',
# 'customization-1',
# 'logscale']

# 'small-multiples',
# 'sparklines',
# 'logscale']


##SIMPLE STATIC 1D PLOT 
if('basic-1' in examples):
	plt.plot([1, 2, 3, 4],[1, 2, 3, 4],'o')

	#SET FIGURE LABELS 
	FS=18	 
	plt.xlabel('x', fontsize=FS)
	plt.ylabel('y', fontsize=FS)
	plt.show()

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
			ax_ij.set_title(f'Plot ({row_num+1}, {col_num+1})')
			ax_ij.set_xlabel('x_'+str(row_num)+str(col_num), fontsize=14)
			ax_ij.set_ylabel('x_'+str(row_num)+str(col_num), fontsize=14)

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

	#SPECIFY FONT SIZE
	FS=14

	#DEFINE FIG+AX OBJECTS 
	f, ax = plt.subplots()
	#https://www.canva.com/colors/color-wheel/
	ax.plot(x,y,'o',color='#FF0012', markersize=10, label='Data')
	ax.plot(x,ye, color='#0012FF',linewidth=4, label='Ground truth')
	ax.plot(x,ye,color='#12FF00', linewidth=1, linestyle='dashed')

	#SET LEGEND
	ax.legend()

	#SET FIGURE SIZE
	f.set_size_inches(10, 6)

	#FIGURE TITLE
	f.suptitle('Decaying oscillations', fontsize=20)

	#AXIS LABELS
	ax.set_xlabel('Time (ps)', fontsize=FS)
	ax.set_ylabel('Amplitude (cm)', fontsize=FS)

	#X-Y PLOT RANGE
	ax.set_xlim([-40,0])
	ax.set_ylim([-1750,1750])

	#AXIS TIC VALUES
	ax.set_xticks([-40,-30,-20,-10,0],fontsize=20)
	ax.set_yticks([-2000,-1000,0,1000,2000],fontsize=20)

	#CONTROL AXIS TICK FORMAT
	ax.yaxis.set_major_formatter(plt.FormatStrFormatter('%4.0f'))
	ax.xaxis.set_major_formatter(plt.FormatStrFormatter('%.1f'))

	#AXIS TIC FONT SIZE
	ax.tick_params(axis='both', which='major', labelsize=FS)
	ax.tick_params(axis='both', which='minor', labelsize=FS)

	#SAVE IMAGES
	f.savefig('plot-1.png', bbox_inches='tight')
	f.savefig("plot-1.pdf", bbox_inches='tight')

	#RENDER AND SHOW IMAGE
	plt.show()


if('logscale' in examples):

	#DEFINE DATA
	x = np.linspace(0.1, 5,1000)
	y1  = 10**x
	y2  = x
	y3  = np.log10(x)

	fig, axes = plt.subplots(2, 2)

	#LINEAR SCALES
	ax  = axes[0][0]
	ax.set_yscale('linear')
	ax.set_xscale('linear')
	ax.plot(x,10**x,x,np.log10(x))





	#SIMILAR TO: y=f(x) --> log(y) 
	# ax.plot(x,np.log10(y1),'o'); plt.show(); 
	# ax.set_yscale('log')

	#SIMILAR TO: y=f(log(x)) --> log(y) 
	#ax.plot(np.log10(x),y1,'o'); plt.show(); exit()
	# ax.set_xscale('log')

	# ax.plot(x,y1,'-')
	plt.show()




	#PLOT 
	# fig, ax = plt.subplots()
	#exit()







if('sparklines' in examples):
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

	# # create some random data
	# x = np.cumsum(np.random.rand(1000)-0.5)

	# # plot it
	# fig, ax = plt.subplots(1,1,figsize=(10,3))
	# plt.plot(x, color='k')
	# plt.plot(len(x)-1, x[-1], color='r', marker='o')

	# # remove all the axes
	# for k,v in ax.spines.items():
	#     v.set_visible(False)
	# ax.set_xticks([])
	# ax.set_yticks([])

	# #show it
	# plt.show()



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





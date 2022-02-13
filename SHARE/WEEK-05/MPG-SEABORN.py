#J. HICKMAN 2021-05-26

import  pandas  as 	pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np 
from matplotlib.backends.backend_pdf import PdfPages

#LOAD DATA
df = sns.load_dataset("mpg")
HUE='origin'

#--------------------------------
#EXPLORE THE DATASET NUMERICALLY
#--------------------------------

print("----------------------")
print("DATAFRAME INFO:")
print("----------------------")
print("shape:", df.shape)
print("number of rows:", len(df.index))
print("number of col:",  len(df.columns))
print("column names:", df.columns)
print("keys:",  df.keys(),type(df.keys()))
print("info",df.info() )
print("head", df.head())
print("TYPES\n", df.dtypes)

print("----------------------")
print("BASIC STATISTICS:")
print("----------------------")
print(df.describe())

print("----------------------")
print("CORRELATION MATRIX:")
print("----------------------")
print(df.corr())

#--------------------------------
#EXPLORE THE DATASET VISUALLY 
#--------------------------------

#INITIALIZE OBJECT TO SAVE MULTIPLE PDFS
pp = PdfPages('mpg.pdf')

#BASIC PAIR PLOT-1
f=sns.pairplot(df);
#plt.show()
pp.savefig(f.fig)

#BASIC PAIR PLOT-2
f=sns.pairplot(df, diag_kind='kde')  
# f.fig.set_size_inches(8,8); 
#plt.show()
pp.savefig(f.fig)


#FULL PAIR PLOT
f=sns.pairplot(df, diag_kind='kde', kind="hist", hue=HUE)  # SLOWER
# plt.show()
# f.fig.suptitle('MPG DATASET', fontsize=24)
#USE THE SEABORN.SET() FUNCTION TO SET FONT SIZE IN SEABORN PLOT

pp.savefig(f.fig)


pp.close()

#-------------------------
#BASIC DATAFRAME PLOTTING 
#-------------------------
#(GENERAL) SHOULD WORK WITH ARBITRARY DATAFRAME
#ACTS ON ENTIRE DATAFRAME

def pd_general_plots(df,HUE=None):
	#NOTE: CERTAIN PLOTS ONLY WORK IF HUE=CATERGORICAL

	#-------------------------
	#FULL CORRELOGRAM
	#-------------------------	
	sns.set_theme(style="white")
	corr = df.corr()  #Compute the correlation matrix

	# # Generate a mask for the upper triangle
	mask = np.triu(np.ones_like(corr, dtype=bool)) 
	f, ax = plt.subplots(figsize=(11, 9)) #initialize figure

	cmap = sns.diverging_palette(230, 20, as_cmap=True) #custom diverging colormap

	# # Draw the heatmap with the mask and correct aspect ratio
	sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
	            square=True, linewidths=.5, cbar_kws={"shrink": .5})
	plt.show()


	#-------------------------
	#DENSITY PLOT PROJECTED ONTO FIRST COL
	#-------------------------

	if(HUE!=None):
		#GET NAME OF FIRST COLUMN
		colname = df.columns[0]

		# Plot the distribution of clarity ratings, conditional on carat
		sns.displot(
		    data=df,
		    x=colname, hue=HUE,
		    kind="kde", height=6,
		    multiple="fill", alpha=.5,    palette="ch:rot=-.25,hue=1,light=.5",

		)
		plt.show()

	#-------------------------
	#CORRELOGRAM+DENDROGRAMS
	#-------------------------	
	sns.clustermap(corr, center=0, cmap=cmap, vmax=.3, 
	             linewidths=4, cbar_kws={"shrink": .5})
	plt.show()


	#-------------------------
	#VIOLIN PLOTS (LOGSCALE)
	#-------------------------
	f, ax = plt.subplots(figsize=(7, 6))
	ax.set_xscale("log")
	sns.set_theme()
	sns.violinplot(data=df, palette="Set3", inner="points", orient="h")
	plt.show()


#------------------------------------------
#DATAFRAME PLOTTING USING 3 COLUMNS (X,Y,Z)
#-------------------------------------------
#DEFAULT IS FIRST 3 COLUMNS
def pandas_2D_plots(df,col_to_plot=[0,1,2], HUE=None):

	#NOTES:
	# X=NUMERIC CONTINUOUS col_to_plot[0]
	# Y=NUMERIC CONTINUOUS col_to_plot[1]
	# Z=NUMERIC CONTINUOUS col_to_plot[2] (USED FOR SIZE AND COLORING)

	# HUE=DISCRETE OR CATEGORICAL

	#GET COLUMN NAMES FOR PLOTTING
	xname=df.columns[col_to_plot[0]]
	yname=df.columns[col_to_plot[1]]
	zname=df.columns[col_to_plot[2]]
	# print(xname,yname,zname); exit()

	#ERROR CHECK 
	if(str(type(df)) != "<class 'pandas.core.frame.DataFrame'>"): 
		raise ValueError("input variable is not panda DataFrame")

	if(len(df.columns)<3): raise ValueError("not enough columns")
	#print("number of col:",  len(df.columns))


	# #-------------------------
	# #SCATTER PLOT
	# #-------------------------
	plt.figure(figsize=(12,8))
	sns.scatterplot(x=xname,y=yname,data=df,hue=HUE)
	plt.show()

	sns.scatterplot(x=xname,y=yname,data=df,hue=zname) #HUE CAN BE
	sns.kdeplot(x=xname,y=yname,data=df, levels=5, color="b", linewidths=1)
	plt.show()

	sns.scatterplot(x=xname,y=yname,data=df,hue=HUE,size=zname) #HUE CAN BE
	plt.show()


	#-------------------------
	#VARIOUS PAIR PLOT STYLES
	#-------------------------

	#FIND KEYS FOR PLOTTING BASED ON PROVIDED INDICES
	keys_to_plot=[]; indx=0;  
	for col in df:
		if(indx in col_to_plot ):
			keys_to_plot.append(col); 
		indx+=1	# for col in df:
	if(HUE!=None and HUE not in keys_to_plot): keys_to_plot.append(HUE)	
	print("keys_to_plot",keys_to_plot)	

	sns.pairplot(df[keys_to_plot], kind='kde',hue=HUE)       #VERY SLOW BUT LOOKS GOOD
	plt.show()

	sns.pairplot(df[keys_to_plot], diag_kind='kde',hue=HUE)  #FAST
	plt.show()

	plt1=sns.pairplot(df[keys_to_plot], diag_kind='kde',hue=HUE)  #FAST
	plt1.map_lower(sns.kdeplot, levels=4, color=".2")  #SLOWER BUT BETTER 
	plt.show()


	#-------------------------
	#JOINTPLOT
	#-------------------------
	# Show the joint distribution using kernel density estimation
	sns.jointplot(
	    data=df,
	    x=xname, y=yname,
	    kind="kde", hue=HUE
	)	
	plt.show()


	# #-------------------------
	# #BOX AND WHISKER
	# #-------------------------
	# #ONLY WORKS FOR CATEGORICAL HUE
	if(HUE!=None):
		for name in [xname,yname]:
			# Plot the orbital period with horizontal boxes
			sns.boxplot(x=name, y=HUE, data=df,
			            whis=[0, 100], width=.6, palette="vlag")

			# # Add in points to show each observation
			sns.stripplot(x=name, y=HUE, data=df,
			              size=4, color=".3", linewidth=0)
			plt.show()


			sns.boxenplot(x=HUE, y=name,
		              color="b", 
		              scale="linear", data=df)
			plt.show()

			#SWARM PLOT
			ax = sns.swarmplot(data=df, x=xname, y=HUE, hue=HUE)
			ax.set(ylabel="")
			plt.show()


	#-------------------------
	#RELPLOT
	#-------------------------

	sns.relplot(x=xname, y=yname, hue=HUE, size=zname,
            sizes=(40, 400), alpha=.5, palette="muted",
            height=6, data=df)
	plt.show()




#RUN FUNCTIONS 

# pd_general_plots(df)  
pd_general_plots(df,HUE='origin') 

# pandas_2D_plots(df)
# pandas_2D_plots(df,HUE='origin')
pandas_2D_plots(df,col_to_plot=[4,5,0],HUE='origin')






#-------------------------------------------
#RUN SCRIPT 
#-------------------------------------------
#NOTE: CERTAIN PLOTS ONLY WORK IF HUE=CATERGORICAL

#----------------------
#DATASET-1: 
#CALIFORNIA HOUSING CENSUS
#----------------------

#source=https://medium.com/analytics-vidhya/house-price-prediction-regression-with-tensorflow-keras-4fc49fae7123

# #READ CSV DATA INTO PANDAS DATAFRAME
# df=pd.read_csv('housing.csv')

# # #EVALUATE FUNCTIONS FOR GIVEN DATAFRAM
# get_pd_info(df);  

# # pd_general_plots(df)  
# pd_general_plots(df,HUE='ocean_proximity')  #SLOWER BUT NICER

# # pandas_2D_plots(df)
# # pandas_2D_plots(df,HUE='ocean_proximity')
# pandas_2D_plots(df,col_to_plot=[0,1,8],HUE='ocean_proximity')


#----------------------
#DATASET-2: CAR MPG DATA 
#----------------------





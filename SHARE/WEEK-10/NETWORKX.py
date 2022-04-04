


EXAMPLE=""

# EXAMPLE="NX_TO_PYVIS_1"
if(EXAMPLE=="NX_TO_PYVIS_1"):
	from pyvis.network import Network
	import networkx as nx
	import matplotlib.pyplot as plt

	nx_graph = nx.cycle_graph(10)
	nx_graph.nodes[1]['title'] = 'Number 1'
	nx_graph.nodes[1]['group'] = 1
	nx_graph.nodes[3]['title'] = 'I belong to a different group!'
	nx_graph.nodes[3]['group'] = 10
	nx_graph.add_node(20, size=20, title='couple', group=2)
	nx_graph.add_node(21, size=15, title='couple', group=2)
	nx_graph.add_edge(20, 21, weight=5)
	nx_graph.add_node(25, size=25, label='lonely', title='lonely node', group=3)

	#BASIC NETWORK-X PLOT
	nx.draw(nx_graph)
	plt.show()


	nt = Network('500px', '500px')
	# populates the nodes and edges data structures
	nt.from_nx(nx_graph)
	nt.show('nx.html')
	exit()

EXAMPLE="NX_TO_PYVIS_2"
if(EXAMPLE=="NX_TO_PYVIS_2"):
	from pyvis.network import Network
	import networkx as nx
	import matplotlib.pyplot as plt

	#GENERATE GRAPH
	G = nx.complete_graph(50)

	#BASIC NETWORK-X PLOT
	nx.draw(G)
	plt.show()

	#SEND TO PYVIS
	nt = Network('500px', '500px')
	nt.from_nx(G)
	nt.show('nx.html')


EXAMPLE="NX_TO_PYVIS_CUSTOM"
if(EXAMPLE=="NX_TO_PYVIS_CUSTOM"):
	from pyvis.network import Network
	import networkx as nx
	import matplotlib.pyplot as plt

	#GENERATE GRAPH
	G = nx.complete_graph(50)

	#SEND TO PYVIS
	nt = Network('500px', '500px')
	nt.from_nx(G)

	#PYVIS CUSTOMIZATION
	#nt.show_buttons(filter_=['physics'])
	# nt.show_buttons(filter_=['layout'])
	nt.show_buttons(filter_=['nodes'])
	# nt.show_buttons(filter_=['edges'])

	# #SET PYVIS OPTIONS
	# nt.set_options("""
	# var options = {
	#   "physics": {
	#     "forceAtlas2Based": {
	#       "springLength": 350
	#     },
	#     "minVelocity": 0.75,
	#     "solver": "forceAtlas2Based",
	#     "timestep": 0.01
	#   }
	# }
	# """)

	nt.show('nx.html')

# EXAMPLE="NX_DRAW_CUSTOMIZATION"
if(EXAMPLE=="NX_DRAW_CUSTOMIZATION"):
	import networkx as nx
	import matplotlib.pyplot as plt

	#GENERATE GRAPH
	G = nx.complete_graph(5)

	#BASIC PLOT
	nx.draw(G)
	plt.show()

	#CUSTOMIZE
	#specifiy x-y positions for plotting
	pos=nx.circular_layout(G)

	#initialize plot
	fig, ax = plt.subplots()
	nx.draw(
	G,
	node_color='blue',
	edgecolors="black",
	edge_color="black", 
	linewidths=2,
	font_color="white",
	font_weight="bold",
	node_size=500,
	width=2,
	with_labels=True,
	pos=pos,
	ax=ax
	)
	ax.set(title='Basic NetworkX plot')
	ax.set_aspect('equal', 'box')
	#fig.savefig("test.png")
	plt.show()



# EXAMPLE="NX_EXPLORE_LAYOUT"
if(EXAMPLE=="NX_EXPLORE_LAYOUT"):
	import networkx as nx
	import matplotlib.pyplot as plt

	#GENERATE GRAPH
	G = nx.complete_graph(10)

	for i in range(1,7+1):
		#if(i==1): title="Layout: Spring";       pos = nx.fruchterman_reingold_layout(G,iterations=200)
		if(i==1): title="Layout: Spring";       pos = nx.spring_layout(G,iterations=200)
		if(i==2): title="Layout: Spectral";     pos = nx.spectral_layout(G)
		if(i==3): title="Layout: Circular";     pos = nx.circular_layout(G)
		if(i==4): title="Layout: Kamada-Kawai"; pos = nx.kamada_kawai_layout(G)
		if(i==5): title="Layout: Random";       pos = nx.random_layout(G)
		if(i==6): title="Layout: Shell";        pos = nx.shell_layout(G)
		#CAN MANUALLY SPECIFY GRAPH LOCATIONS WITH A DICTIONARY OF (X,Y) ARRAYS 
		if(i==7): 
			title="Layout: Manual"; pos={}; j=0; i=0
			for k in range(0,len(list(G.edges))):
				if(k%5==0): j=j+1
				if(k%5==0): i=0
				i=i+1
				pos[k]=[j,i]

		fig, ax = plt.subplots()
		nx.draw(
			G,
			node_color="blue",
			node_size=500,
			font_color="white",
			font_weight="bold",
			with_labels=True,
			pos=pos,
		)
		ax.set(title=title)
		ax.set_aspect('equal', 'box')
		plt.title(title)
		plt.show()

EXAMPLE="NX_PLOT_WITH_ATTRIBUTES"
if(EXAMPLE=="NX_PLOT_WITH_ATTRIBUTES"):

	import networkx as nx
	import matplotlib.pyplot as plt
	import random
	import numpy as np

	#GENERATE GRAPH
	N=20

	G = nx.complete_graph(N)
	G = nx.gnp_random_graph(N, 0.1, seed=10374196)

	#ASSIGN RANDOM ATTRIBUTES TO NODES+EDGES
	for u in G.nodes():	G.nodes[u]['attribute']=0.2+1*random.uniform(0, 1) 
	for u,v in G.edges(): G[u][v]['weight']=5*random.uniform(0, 1) 

	#PRINT NODE+EDGES
	for node in G.nodes(data=True): print(node)
	for line in nx.generate_edgelist(G, data=True): print(line)

	#SPECIFIY X-Y POSITIONS FOR PLOTTING
	pos=nx.circular_layout(G)
	pos=nx.spring_layout(G,k=10./np.sqrt(N),iterations=500)
	# pos=nx.random_layout(G)

	#GENERATE PLOT
	fig, ax = plt.subplots()

	#assign colors based on attributes
	weights_n 	= [G.nodes[u]['attribute'] for u in G.nodes()]
	weights_e 	= [G[u][v]['weight'] for u,v in G.edges()]

	#SAMPLE CMAP FOR COLORS 
	cmap=plt.cm.get_cmap('Blues')
	colors_e 	= [cmap(G[u][v]['weight']/5.0) for u,v in G.edges()]
	colors_n 	= [cmap(G.nodes[u]['attribute']/1.2) for u in G.nodes()]

	#VARIOUS METHODS FOR VISUALIZING SIZE

	#LABELS (DICT)
	labels={}
	for n,d in nx.degree(G): labels[n]=d #str(n)+"-"+str(d) 

	#WEIGHTS
	# node_size=1000*weights_n

	#DEGREE CENTRALITY
	centrality=nx.degree(G)
	centrality=np.array([d for n,d in centrality]); #print(G_DEGREE)
	node_size=1000*centrality/max(centrality)
	colors_n = node_size
	colors_n = [cmap(u/max(centrality)) for u in centrality]

	#EIGEN CENTRALITY
	# centrality = nx.eigenvector_centrality(G)
	# centrality = np.array([centrality[n] for n in centrality]); #print(G_DEGREE)
	# node_size=1000*centrality/max(centrality)
	# colors_n = [cmap(u/max(centrality)) for u in centrality]


	#EIGEN CENTRALITY
	# centrality = nx.betweenness_centrality(G)
	# centrality = np.array([centrality[n] for n in centrality]); #print(G_DEGREE)
	# node_size=1000*centrality/max(centrality)
	# colors_n = [cmap(u/max(centrality)) for u in centrality]


	#PLOT
	nx.draw(
	G,
	node_color=colors_n,
	edgecolors="black",
	edge_color=colors_e,
	linewidths=2,
	labels=labels,
	font_color="white",
	font_weight="bold",
	node_size=node_size, 
	width=weights_e,
	with_labels=True,
	pos=pos,
	ax=ax
	)
	#define color map
	# plt.cm.get_cmap('YlOrBr')

	ax.set(title='Color and size plotted by attribute')
	ax.set_aspect('equal', 'box')
	# plt.colorbar(cmap)

	# fig.savefig("test.png")
	plt.show()


#SOCIAL NETWORK EXAMPLES
# G = nx.karate_club_graph()
# G = nx.davis_southern_women_graph()
# G = nx.florentine_families_graph()
# G = nx.les_miserables_graph()


# EXAMPLE="NX_DEGREE_HISTOGRAM_PLOT"
if(EXAMPLE=="NX_DEGREE_HISTOGRAM_PLOT"):
	# MODIFIED FROM 
	# https://networkx.org/documentation/stable/auto_examples/drawing/plot_degree.html
	import networkx as nx
	import numpy as np
	import matplotlib.pyplot as plt

	#GENERATE GRAPH
	#gnp_random_graph(n, p=, seed=None, directed=False)
	#p=connection probablity
	G = nx.gnp_random_graph(20, 0.2, seed=10374196)

	#COMPUTE DEGREE: --> "LIST" WITH NODE DEGREES
	G_DEGREE=G.degree(); print(G_DEGREE,G_DEGREE[5],type(G_DEGREE)) 

	#SORT DEGREE AND STORE IN LIST 
	degree_sequence = sorted((d for n, d in G_DEGREE), reverse=True)
	dmax = max(degree_sequence)   #MAX DEGREE

	#INITIALIZE MPL FIGURE+AX
	fig = plt.figure("Degree of a random graph", figsize=(8, 8))
	# Create a gridspec for adding subplots of different sizes
	axgrid = fig.add_gridspec(5, 4)

	#PLOT NETWORK IN UPPER GRID SPACES 
	ax0 = fig.add_subplot(axgrid[0:3, :])
	pos = nx.spring_layout(G)
	nx.draw(G,pos=pos,ax=ax0)
	ax0.set_title("Network Graph: G")

	#INITIALIZE MPL FIGURE+AX
	# fig = plt.figure("Degree of a random graph", figsize=(8, 8))
	# # Create a gridspec for adding subplots of different sizes
	# axgrid = fig.add_gridspec(5, 4)

	# #PLOT NETWORK IN UPPER GRID SPACES 
	# ax0 = fig.add_subplot(axgrid[0:3, :])
	# pos = nx.spring_layout(G)
	# #initialize plot
	# fig, ax = plt.subplots()
	# nx.draw(
	# G,
	# node_color='blue',
	# edgecolors="black",
	# edge_color="black", 
	# linewidths=2,
	# font_color="white",
	# font_weight="bold",
	# width=2,
	# with_labels=True,
	# pos=pos,
	# ax=ax0
	# )
	# ax0.set_title("Network Graph: G")


	#PLOT RANK (IMPORTANCE BASED ON DEGREE) VS DEGREE)
	ax1 = fig.add_subplot(axgrid[3:, :2])
	ax1.plot(degree_sequence, "b-", marker="o")
	ax1.set_title("Degree Rank Plot")
	ax1.set_ylabel("Degree")
	ax1.set_xlabel("Rank")

	#PLOT RANK HISTOGRAM
	ax2 = fig.add_subplot(axgrid[3:, 2:])
	ax2.bar(*np.unique(degree_sequence, return_counts=True))
	ax2.set_title("Degree histogram")
	ax2.set_xlabel("Degree")
	ax2.set_ylabel("# of Nodes")

	fig.tight_layout()
	plt.show()

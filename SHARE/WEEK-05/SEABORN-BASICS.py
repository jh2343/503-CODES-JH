

import  matplotlib.pyplot as plt
import  seaborn as sns
import  pandas  as  pd


#RUN ONE
examples=['various_examples']

#RUN ALL 
# examples=['theme','basic','various_examples']

#EXAMPLE
if('theme' in examples):
    #SOURCE:
    #https://seaborn.pydata.org/generated/seaborn.set_theme.html
    
    #DEFAULT, seaborn plots will be made with the 
    #current values of the matplotlib rcParams:
    sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])
    plt.show()

    #NO ARGUMENTS --> ACTIVATE SEABORN’S “DEFAULT” THEME:
    sns.set_theme()
    sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])
    plt.show()

    #SPECIFY ARGUMENTS
    #CAN USE MATPLOT LIB COLOR PALETTES
    #There are five preset seaborn styles: 
    #darkgrid, whitegrid, dark, white, and ticks
    sns.set_theme(style="whitegrid", palette="Set1")
    sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])
    plt.show()

    #SET STYLE/PALETTE ARGUMENT SEPARATLY
    sns.set_theme()
    sns.set_palette("Pastel1")
    sns.set_style("whitegrid")
    # sns.set_style("dark")
    # sns.set_style("white")
    sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])
    plt.show()


#EXAMPLE
if('basic' in examples):

    #GENERATE DATA
    df = pd.DataFrame({"C1": [7,1,5,6,3,10,5,8],
                       "C2" : [1,2,8,4,3,9,5,2]})

    #DATAFRAME
    print(df)

    #PLOT-1
    #returns a MPL ax object
    f = sns.lineplot(data = df)
    #edit axis type object simlar to MPL
    FS=14
    f.set_xlabel("X-Axis", fontsize=FS)
    f.set_ylabel("Y-Axis", fontsize=FS)
    #AXIS TIC FONT SIZE
    f.tick_params(axis='both', which='major', labelsize=FS)
    plt.legend(labels=["Legend_Day1","Legend_Day2"], fontsize=FS)
    plt.show()

    #PLOT-2
    #returns an object with f.fig and f.ax attributes
    f = sns.relplot(data  = df, x="C1", y="C2")
    f.fig.suptitle('Title', fontsize=FS)
    f.ax.tick_params(axis='both', which='major', labelsize=FS)
    f.ax.set_xlabel("X-Axis", fontsize=FS)
    f.ax.set_ylabel("Y-Axis", fontsize=FS)
    plt.show()




#SOURCE: MODIFIED FROM 
#https://seaborn.pydata.org/introduction.html

if('various_examples' in examples):

    # LOAD AN EXAMPLE DATASET
    tips = sns.load_dataset("tips")
    print(tips)

    # RELPLOT
    # This function provides access to several different 
    # axes-level functions that show the relationship between 
    # two variables with semantic mappings of subsets.
    # The kind parameter selects the underlying axes-level 
    # function to use:
    sns.relplot(
        data=tips,
        x="total_bill", y="tip", col="time",
        hue="smoker", style="smoker", size="size",
    )

    #DOTS DATA
    dots = sns.load_dataset("dots")
    print(dots)
    sns.relplot(
        data=dots, kind="line",
        x="time", y="firing_rate", col="align",
        hue="choice", size="coherence", style="choice",
        facet_kws=dict(sharex=False),
    )

    #STATISTICAL ESTIMATION AND ERROR BARS
    fmri = sns.load_dataset("fmri")
    sns.relplot(
        data=fmri, kind="line",
        x="timepoint", y="signal", col="region",
        hue="event", style="event",
    )
    #lmplot --> Plot data and regression model fits across a FacetGrid.
    sns.lmplot(data=tips, x="total_bill", y="tip", col="time", hue="smoker")


    #INFORMATIVE DISTRIBUTIONAL SUMMARIES
    sns.displot(data=tips, x="total_bill", col="time", kde=True)

    #CDF
    sns.displot(data=tips, kind="ecdf", x="total_bill", col="time", hue="smoker", rug=True)


    #SPECIALIZED PLOTS FOR CATEGORICAL DATA

    #SWARM PLOT
    sns.catplot(data=tips, kind="swarm", x="day", y="total_bill", hue="smoker")

    #VIOLIN PLOT
    sns.catplot(data=tips, kind="violin", x="day", y="total_bill", hue="smoker", split=True)

    #BAR CHART
    sns.catplot(data=tips, kind="bar", x="day", y="total_bill", hue="smoker")


    #COMPOSITE VIEWS ONTO MULTIVARIATE DATASETS
    penguins = sns.load_dataset("penguins")
    sns.jointplot(data=penguins, x="flipper_length_mm", y="bill_length_mm", hue="species")

    sns.pairplot(data=penguins, hue="species")


    g = sns.PairGrid(penguins, hue="species", corner=True)
    g.map_lower(sns.kdeplot, hue=None, levels=5, color=".2")
    g.map_lower(sns.scatterplot, marker="+")
    g.map_diag(sns.histplot, element="step", linewidth=0, kde=True)
    g.add_legend(frameon=True)
    g.legend.set_bbox_to_anchor((.61, .6))


    # OPINIONATED DEFAULTS AND FLEXIBLE CUSTOMIZATION
    sns.relplot(
        data=penguins,
        x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g"
    )

    sns.set_theme(style="ticks", font_scale=1.25)
    g = sns.relplot(
        data=penguins,
        x="bill_length_mm", y="bill_depth_mm", hue="body_mass_g",
        palette="crest", marker="x", s=100,
    )
    g.set_axis_labels("Bill length (mm)", "Bill depth (mm)", labelpad=10)
    g.legend.set_title("Body mass (g)")
    g.figure.set_size_inches(6.5, 4.5)
    g.ax.margins(.15)
    g.despine(trim=True)


    plt.show()

import matplotlib.pyplot as plt
import seaborn  as sns
import pandas   as pd
import numpy    as np

# LIST OF POSSIBLE EXAMPLES 
# example = 'basic'
example =  'theme'
# example = "tips"
# example = 'dots'
# example = 'fmri'
# example = 'penquins'

# EXAMPLE
if "basic" == example:

    # GENERATE DATA
    df = pd.DataFrame({"C1": [7, 1, 5, 6, 3, 10, 5, 8], "C2": [1, 2, 8, 4, 3, 9, 5, 2]})

    # DATAFRAME
    print(df)

    # PLOT-1
    # returns a MPL ax object
    ax = sns.lineplot(data=df)
    # edit axis type object simlar to MPL
    FS = 14
    ax.set_xlabel("X-Axis", fontsize=FS)
    ax.set_ylabel("Y-Axis", fontsize=FS)
    # AXIS TIC FONT SIZE
    ax.tick_params(
        axis="both", 
        which="major", 
        labelsize=FS)
    plt.legend(labels=["Legend_Day1", "Legend_Day2"], fontsize=FS)
    plt.show()

    # PLOT-2
    # returns an object with f.fig and f.ax attributes
    f = sns.relplot(data=df, x="C1", y="C2")
    f.fig.suptitle("TEST", fontsize=FS)
    f.ax.tick_params(axis="both", which="major", labelsize=FS)
    f.ax.set_xlabel("X-Axis", fontsize=FS)
    f.ax.set_ylabel("Y-Axis", fontsize=FS)
    plt.show()


# EXAMPLE
if "theme" == example:
    # SOURCE:
    # https://seaborn.pydata.org/generated/seaborn.set_theme.html

    # DEFAULT, seaborn plots will be made with the
    # current values of the matplotlib rcParams:
    sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])
    plt.show()

    # NO ARGUMENTS --> ACTIVATE SEABORN’S “DEFAULT” THEME:
    sns.set_theme()
    sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])
    plt.show()

    # SPECIFY ARGUMENTS
    # CAN USE MATPLOT LIB COLOR PALETTES
    # There are five preset seaborn styles:
    # darkgrid, whitegrid, dark, white, and ticks
    sns.set_theme(style="whitegrid", palette="Set1")
    sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])
    plt.show()

    # SET STYLE/PALETTE ARGUMENT SEPARATLY
    # sns.set_theme()
    sns.set_palette("Pastel1")
    sns.set_style("whitegrid")
    # sns.set_style("dark")
    # sns.set_style("white")
    sns.barplot(x=["A", "B", "C"], y=[1, 3, 2])
    plt.show()


if "tips" == example:

    # LOAD AN EXAMPLE DATASET
    df = sns.load_dataset("tips")
    print(df)

    # RELPLOT
    # This function provides access to several different
    # axes-level functions that show the relationship between
    # two variables with semantic mappings of subsets.
    # The kind parameter selects the underlying axes-level
    # function to use:
    sns.relplot(
        data=df,
        x="total_bill",
        y="tip",
        col="time",
        hue="smoker",
        style="smoker",
        size="size",
    )
    # plt.show(); exit()
    plt.show()

    # lmplot --> Plot data and regression model fits across a FacetGrid.
    sns.lmplot(
        data=df, 
        x="total_bill", 
        y="tip", 
        col="time", 
        hue="smoker")
    plt.show()

    # INFORMATIVE DISTRIBUTIONAL SUMMARIES
    sns.displot(
        data=df,
        x="total_bill", 
        col="time",
        kde=True
        )
    plt.show()

    # CDF
    sns.displot(
        data=df, 
        kind="ecdf", 
        x="total_bill", 
        col="time", 
        hue="smoker", 
        rug=True
    )
    plt.show()

    # SPECIALIZED PLOTS FOR CATEGORICAL DATA

    # SWARM PLOT-1
    sns.catplot(
        data=df, 
        kind="swarm", 
        x="day", 
        y="total_bill", 
        hue="smoker")
    plt.show()

    # VIOLIN PLOT
    sns.catplot(
        data=df, 
        kind="violin", 
        x="day", 
        y="total_bill", 
        hue="smoker", 
        split=True
    )
    plt.show()

    # BAR CHART
    sns.catplot(
        data=df, 
        kind="bar",
        x="day", 
        y="total_bill", 
        hue="smoker")
    plt.show()


if "dots" == example:

    # DOTS DATA
    df = sns.load_dataset("dots")
    print(df)
    sns.relplot(
        data=df,
        kind="line",
        x="time",
        y="firing_rate",
        col="align",
        hue="choice",
        size="coherence",
        style="choice",
        facet_kws=dict(sharex=False),
    )
    plt.show()


# SOURCE: MODIFIED FROM
# https://seaborn.pydata.org/introduction.html

if "fmri" == example:

    # STATISTICAL ESTIMATION AND ERROR BARS
    df = sns.load_dataset("fmri")
    print(df)
    sns.relplot(
        data=df,
        kind="line",
        x="timepoint",
        y="signal",
        col="region",
        hue="event",
        style="event",
    )
    plt.show()


if "penquins" == example:


    # COMPOSITE VIEWS ONTO MULTIVARIATE DATASETS
    df = sns.load_dataset("penguins")
    print(df)
    print(df.describe())

    #INDIVIDUAL PAIR PLOT 
    sns.jointplot(
            data=df, 
            x="flipper_length_mm", 
            y="bill_length_mm", 
            hue="species"
                 )   
    plt.show()

    #PAIR PLOT MATRIX
    sns.pairplot(
            data=df, 
            hue="species"
                )
    plt.show()

    # PAIR PLOT MATRIX
    g = sns.PairGrid(df, hue="species", corner=True)
    g.map_lower(sns.kdeplot, hue=None, levels=5, color=".2")
    g.map_lower(sns.scatterplot, marker="+")
    g.map_diag(sns.histplot, element="step", linewidth=0, kde=True)
    g.add_legend(frameon=True)
    g.legend.set_bbox_to_anchor((0.61, 0.6))
    plt.show()

    # # PAIR PLOT 
    sns.relplot(
                data=df, 
                x="bill_length_mm", 
                y="bill_depth_mm", 
                hue="body_mass_g"
                )
    plt.show()


    # # ANOTHER PAIR PLOT
    sns.set_theme(style="ticks", font_scale=1.25)
    g = sns.relplot(
        data=df,
        x="bill_length_mm",
        y="bill_depth_mm",
        hue="body_mass_g",
        palette="crest",
        marker="x",
        s=100,
    )
    g.set_axis_labels("Bill length (mm)", "Bill depth (mm)", labelpad=10)
    g.legend.set_title("Body mass (g)")
    g.figure.set_size_inches(6.5, 4.5)
    g.ax.margins(0.15)
    g.despine(trim=True)
    plt.show()


    #PAIR PLOT+HIST+CORR HEAT MAP
    f = sns.pairplot(df,hue='species')
    
 
    (xmin, _), (_, ymax) = f.axes[0, 0].get_position().get_points()
    (_, ymin), (xmax, _) = f.axes[-1, -1].get_position().get_points()

    ax = f.fig.add_axes([xmin, ymin, xmax - xmin, ymax - ymin], facecolor='none')

    corr1 = df.corr()
    mask1 = np.tril(np.ones_like(corr1, dtype=bool))
    sns.heatmap(corr1, 
                mask=mask1, 
                cmap='RdBu', 
                vmax=.5, 
                vmin=-.5,
                linewidths=.5, 
                cbar=False, annot=True, annot_kws={'size': 22}, ax=ax)
    ax.set_xticks([])
    ax.set_yticks([])
    # ax.xaxis.tick_top()
    # ax.yaxis.tick_right()

    plt.show()


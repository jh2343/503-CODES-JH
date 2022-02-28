# conda install -c plotly plotly
# pip install dash


example = ""

# PLOTLY
# example = "PLOTLY:SCATTERPLOT-1"
# example = "PLOTLY:SCATTERPLOT-2"
# example = "PLOTLY:THEMES"
# example = "PLOTLY:SCATTERPLOT-3"
# example = "PLOTLY:LINEPLOT-1"
# example = "PLOTLY:FACETS"
# example = "PLOTLY:BARGRAPHS"
# example = "PLOTLY:HISTOGRAMS"
# example = "PLOTLY:BOX-VIOLIN-STRIP"
# example = "PLOTLY:MARGINAL"
# example = "PLOTLY:SCATTERMATRIX"
# example = "PLOTLY:PARALLEL_COORD"
# example = "PLOTLY:TREEMAP"
# example = "PLOTLY:SLIDER"
# example = "PLOTLY:MPL_CONVERSION-1"

# DASH
# example = "DASH:BARGRAPH"
# example = "DASH:BASIC"


# ALTAIR
# conda install -c conda-forge altair vega_datasets
# example = "ALTAIR:BASIC"
# example = "ALTAIR:LINECHART"
# example = "ALTAIR:BAR-1"
# example = "ALTAIR:PAIRPLOT"
# example = "ALTAIR:MPG"
# example = "ALTAIR:MPG-2"



# ---------------------------------
# ALTAIR
# ---------------------------------

if example == "ALTAIR:BASIC":
    import altair as alt
    import pandas as pd

    # GENERATE DATA
    df = pd.DataFrame({"a": list("CCCDDDEEE"), "b": [2, 7, 4, 1, 2, 6, 8, 4, 7]})

    # PLOT
    fig = (
        alt.Chart(df)
        .mark_point()
        .encode(
            x="a",
            y="b",
            color="a",
        )
    )
    fig.save("ALTAIR.html")



if example == "ALTAIR:LINECHART":

    import altair as alt
    from vega_datasets import data

    source = data.driving()

    fig = (
        alt.Chart(source)
        .mark_line(point=True)
        .encode(
            alt.X("miles", scale=alt.Scale(zero=False)),
            alt.Y("gas", scale=alt.Scale(zero=False)),
            order="year",
        )
        .interactive()
    )
    fig.save("ALTAIR.html")



if example == "ALTAIR:BAR-1":

    import altair as alt
    import pandas as pd

    df = pd.DataFrame({"a": list("CCCDDDEEE"), "b": [2, 7, 4, 1, 2, 6, 8, 4, 7]})

    # EXAMPLE
    fig = (
        alt.Chart(df)
        .mark_bar()
        .encode(
            x="a",
            y="average(b)",
        )
    )
    fig.save("ALTAIR.html")


if example == "ALTAIR:PAIRPLOT":
    # https://altair-viz.github.io/user_guide/saving_charts.html

    import altair as alt
    from vega_datasets import data

    source = data.cars()
    print(source)
    fig = (
        alt.Chart(source)
        .mark_circle()
        .encode(
            alt.X(alt.repeat("column"), type="quantitative"),
            alt.Y(alt.repeat("row"), type="quantitative"),
            color="Origin:N",
            tooltip=["Name", "Miles_per_Gallon", "Year"],
        )
        .properties(width=150, height=150)
        .repeat(
            row=["Horsepower", "Acceleration", "Miles_per_Gallon"],
            column=["Miles_per_Gallon", "Acceleration", "Horsepower"],
        )
        .interactive()
    )

    fig.save("ALTAIR.html")

if example == "ALTAIR:MPG":
    import altair as alt
    import pandas as pd
    import seaborn as sns

    mpg = sns.load_dataset("mpg")
    print(mpg.head())

    # BLANK CANVAS
    # fig = alt.Chart(mpg).mark_point()
    # fig.save("ALTAIR-1.html")

    # 1D SCATTER PLOT
    # fig = alt.Chart(mpg).mark_point().encode(x="horsepower")
    # fig.save("ALTAIR-1.html")

    # 2D SCATTER PLOT (STATIC)
    fig = (
        alt.Chart(mpg)
        .mark_point()
        .encode(
            x="horsepower",
            y="mpg",
            color="origin",
        )
    )
    fig.save("ALTAIR-2.html")

    # 2D SCATTER PLOT (INTERACTIVE)
    fig = (
        alt.Chart(mpg)
        .mark_point()
        .encode(
            x="horsepower",
            y="mpg",
            color="origin",
        )
    ).interactive()
    fig.save("ALTAIR-3.html")

    # AUTOMATIC AGGREGATIONS
    fig = (
        alt.Chart(mpg)
        .mark_point()
        .encode(x="horsepower", y="average(mpg)", color="origin")
    )
    fig.save("ALTAIR-4.html")

    # MORE EXPLICITLY,
    fig = (
        alt.Chart(mpg)
        .mark_bar()
        .encode(
            alt.X("cylinders", type="quantitative"),
            alt.Y(
                "mpg",
                type="quantitative",
                aggregate="average",
            ),
        )
    )
    fig.save("ALTAIR-5.html")

    # NOTE THAT CHANGING THE DATA TYPE FOR CYLINDERS FROM QUANTITATIVE TO
    # ORDINAL CHANGES ITS REPRESENTATION ON THE GRAPH
    fig = (
        alt.Chart(mpg)
        .mark_bar()
        .encode(
            alt.X(
                "cylinders",
                type="ordinal",
            ),
            alt.Y(
                "mpg",
                type="quantitative",
                aggregate="average",
            ),
        )
    )
    fig.save("ALTAIR-6.html")

    # THE NOTATION HERE IS A SHORTCUT FOR THE PREVIOUS NOTATION, BUT
    # ACHIEVES THE SAME PURPOSE. MORE DETAILS AVAILABLE HERE
    fig = (
        alt.Chart(mpg)
        .mark_bar()
        .encode(
            alt.X("cylinders:O"),
            alt.Y("average(mpg):Q"),
        )
    )
    fig.save("ALTAIR-7.html")

    #     #EXAMPLE
    fig = (
        alt.Chart(mpg)
        .mark_circle(size=60)
        .encode(
            x="horsepower",
            y="mpg",
            color="origin",
            tooltip=["origin", "horsepower", "mpg"],
        )
        .interactive()
    )
    fig.save("ALTAIR-8.html")


if example == "ALTAIR:MPG-2":
    # https://altair-viz.github.io/gallery/dot_dash_plot.html
    import altair as alt
    from vega_datasets import data

    source = data.cars()

    # Configure the options common to all layers
    brush = alt.selection(type="interval")
    base = alt.Chart(source).add_selection(brush)

    # Configure the points
    points = base.mark_point().encode(
        x=alt.X("Miles_per_Gallon", title=""),
        y=alt.Y("Horsepower", title=""),
        color=alt.condition(brush, "Origin", alt.value("grey")),
    )

    # Configure the ticks
    tick_axis = alt.Axis(labels=False, domain=False, ticks=False)

    x_ticks = base.mark_tick().encode(
        alt.X("Miles_per_Gallon", axis=tick_axis),
        alt.Y("Origin", title="", axis=tick_axis),
        color=alt.condition(brush, "Origin", alt.value("lightgrey")),
    )

    y_ticks = base.mark_tick().encode(
        alt.X("Origin", title="", axis=tick_axis),
        alt.Y("Horsepower", axis=tick_axis),
        color=alt.condition(brush, "Origin", alt.value("lightgrey")),
    )

    # Build the chart
    y_ticks | (base & points & x_ticks & y_ticks)

    y_ticks.save("ALTAIR.html")


# ---------------------------------
# PLOTLY
# ---------------------------------



if example == "PLOTLY:MPL_CONVERSION-1":

    # IMPORT MODULES
    import numpy as np
    import matplotlib.pyplot as plt
    import chart_studio.plotly as py
    #conda install -c plotly chart-studio
    import plotly.tools as tls
    import plotly

    # CREATE DATA ARRAYS
    x = np.linspace(-2.0 * np.pi, 2.0 * np.pi, 51)
    y = np.sin(x)

    # MAKE A MPL PLOT
    mpl_fig = plt.figure()
    plt.plot(x, y, 'ko--')
    plt.title('sin(x) from -2*pi to 2*pi')
    plt.xlabel('x')
    plt.ylabel('sin(x)')
    plt.show()

    #CONVERT
    plotly_fig = tls.mpl_to_plotly(mpl_fig)

    #UPDATE THEME
    plotly_fig.update_layout(template='plotly_white')

    #SAVE
    plotly.offline.plot(plotly_fig, filename="PLOTLY.html")



if example == "PLOTLY:SCATTERPLOT-1":
    import plotly.express as px
    import seaborn as sns

    penguins = sns.load_dataset("penguins")
    fig = px.scatter(
        data_frame=penguins,
        x="bill_length_mm",
        y="body_mass_g",
    )
    fig.show()
    #fig.write_html("PLOTLY.html", auto_open=True)


if example == "PLOTLY:SCATTERPLOT-2":
    import plotly.express as px
    import seaborn as sns

    penguins = sns.load_dataset("penguins")
    fig = px.scatter(
        data_frame=penguins,
        x="bill_length_mm",
        y="body_mass_g",
        color="species",
        template="plotly_white",
    )
    fig.show()
    #fig.write_html("PLOTLY.html", auto_open=True)


if True: #example == "PLOTLY:THEMES":
    # https://plotly.com/python/templates/
    import plotly.express as px

    df = px.data.gapminder()
    print(df)
    df_2007 = df.query("year==2007")

    for template in [
        "plotly",
        "plotly_white",
        "plotly_dark",
        "ggplot2",
        "seaborn",
        "simple_white",
        "none",
    ]:
        fig = px.scatter(
            df_2007,
            x="gdpPercap",
            y="lifeExp",
            size="pop",
            color="continent",
            log_x=True,
            size_max=60,
            template=template,
            title="Gapminder 2007: '%s' theme" % template,
        )
        fig.show()


if example == "PLOTLY:SCATTERPLOT-3":
    import plotly.express as px
    import seaborn as sns

    penguins = sns.load_dataset("penguins")
    fig = px.scatter(
        data_frame=penguins,
        x="bill_length_mm",
        y="body_mass_g",
        color="species",
        template="plotly_white",
        labels=dict(
            bill_length_mm="Bill length (mm)",
            body_mass_g="Body mass (g)",
            species="Species",
        ),
        title="Palmer Penguins",
    )

    # UPDATE TOOL TIP
    fig.update_traces(
        customdata=penguins,
        hovertemplate="Species: %{color}<br>Island: %{customdata[1]}<br>Sex: %{customdata[6]}",
    )

    fig.show()
    # fig.write_html("PLOTLY.html", auto_open=True)


if example == "PLOTLY:LINEPLOT-1":
    import plotly.express as px
    import seaborn as sns

    # EXAMPLE-1
    gap = px.data.gapminder()
    df = gap.query("continent != 'Asia'")
    fig = px.line(
        df,
        x="year",
        y="lifeExp",
        color="continent",
        line_group="country",
        hover_name="country",
        height=1000,
        width=1000,
        template="presentation",
        labels=dict(lifeExp="Life expectancy", year="Year"),
    )
    fig.update_layout(showlegend=False)
    fig.show()

    # EXAMPLE-2
    df = gap.query('continent=="Asia"')
    fig = px.line(
        df,
        x="year",
        y="lifeExp",
        color="country",
        height=1000,
        width=1000,
        labels=dict(
            lifeExp="Life expectancy",
            year="Year",
        ),
    )
    fig.update_traces(
        customdata=df,
        hovertemplate="<b>%{customdata[0]}</b><br>Year=%{x}<br>Life Expectancy=%{y}",
    )
    fig.update_layout(showlegend=False)
    fig.show()

    # fig.write_html("PLOTLY.html")  # , auto_open=True)


if example == "PLOTLY:FACETS":
    import plotly.express as px
    import seaborn as sns

    gap = px.data.gapminder()

    fig = px.line(
        data_frame=gap,
        x="year",
        y="lifeExp",
        color="country",
        facet_col="continent",
        facet_col_wrap=3,  # << facet_col is the key
        labels={"lifeExp": "Life expectancy"},
        width=1000,
        height=400,
    ).update_layout(showlegend=False)
    fig.show()
    # fig.write_html("PLOTLY.html")


# CATEGORICAL VARIABLES

if example == "PLOTLY:BARGRAPHS":
    import plotly.express as px
    import seaborn as sns

    tips = px.data.tips()
    print(tips)

    # DEFAULT
    fig = px.bar(
        tips,
        x="day",
        y="total_bill",
        width=500,
        height=500,
        labels={
            "day": "Day",
            "total_bill": "Total bill",
        },
    )
    fig.show()
    # fig.write_html("PLOTLY.html")

    # RE-ORDER THE BARS IN ALPHABETICAL ORDER
    fig = px.bar(
        tips,
        x="day",
        y="total_bill",
        category_orders={"day": ["Thur", "Fri", "Sat", "Sun"]},
        width=500,
        height=500,
        labels={"day": "Day", "total_bill": "Total bill"},
    )
    fig.show()
    # fig.write_html("PLOTLY.html")

    # ADD A GROUPING VARIABLE
    fig = px.bar(
        tips,
        x="day",
        y="total_bill",
        color="smoker",
        barmode="group",
        category_orders={"day": ["Thur", "Fri", "Sat", "Sun"]},
        width=500,
        height=500,
        labels={"day": "Day", "total_bill": "Total bill"},
    )
    fig.show()
    # fig.write_html("PLOTLY.html")

    # ADD FACITING GROUPING VARIABLE
    fig = px.bar(
        tips,
        x="day",
        y="total_bill",
        color="smoker",
        barmode="group",
        facet_col="sex",
        category_orders={
            "day": ["Thur", "Fri", "Sat", "Sun"],
            "sex": ["Male", "Female"],
            "smoker": ["Yes", "No"],
        },
        labels={
            "day": "Day",
            "total_bill": "Total bill",
            "smoker": "Smoker",
            "sex": "Sex",
        },
        width=1000,
        height=400,
    )
    # fig.write_html("PLOTLY.html")
    fig.show()


# STATISTICAL PLOTS

if example == "PLOTLY:HISTOGRAMS":
    import plotly.express as px
    import seaborn as sns

    tips = px.data.tips()
    print(tips)

    # HISTOGRAM, NORMALIZED TO HAVE AREA 1
    fig = px.histogram(
        tips,
        x="total_bill",
        nbins=20,
        histnorm="probability density",
        color_discrete_sequence=["indianred"],
        labels={"total_bill": "Total bill"},
        width=400,
        height=400,
    )
    fig.show()

    # GROUPED HISTOGRAM
    fig = px.histogram(
        tips,
        x="total_bill",
        color="sex",
        labels={"total_bill": "Total bill"},
        width=400,
        height=400,
    )
    fig.show()

    fig = px.histogram(
        tips,
        x="total_bill",
        color="sex",
        labels={"total_bill": "Total bill"},
        marginal="box",  # or 'rug' or 'violin'
        width=500,
        height=500,
    )
    fig.show()

    # THE HISTOGRAM, APPLIED TO A CATEGORICAL VARIABLE,
    # PRODUCES A FREQUENCY BAR PLOT
    fig = px.histogram(
        tips,
        x="day",
        category_orders={"day": ["Thur", "Fri", "Sat", "Sun"]},
        width=400,
        height=400,
    )

    # order by value
    fig.update_xaxes(categoryorder="total ascending")
    fig.show()

    # Bar plots of values of one variable grouped by categories
    # of another
    fig = (
        px.histogram(tips, x="day", y="tip", histfunc="avg", width=400, height=400)
        .update_xaxes(categoryorder="total ascending")
        .update_layout(yaxis_tickformat="$")
    )
    fig.show()


# CONTINUOUS VS CATEGORICAL VARIABLE

if example == "PLOTLY:BOX-VIOLIN-STRIP":

    import plotly.express as px
    import seaborn as sns

    tips = px.data.tips()
    print(tips)

    # BOXPLOT
    fig = px.box(
        tips,
        x="day",
        y="total_bill",
        labels={"total_bill": "Total bill"},
        width=400,
        height=400,
    )
    fig.show()

    # VIOLIN PLOT
    fig = px.violin(
        tips,
        x="day",
        y="total_bill",
        labels={"total_bill": "Total bill"},
        width=400,
        height=400,
    )
    fig.show()

    # STRIP PLOT
    fig = px.strip(
        tips,
        x="day",
        y="total_bill",
        labels={"total_bill": "Total bill"},
        width=400,
        height=400,
    )
    fig.show()


# MARGINAL PLOT
if example == "PLOTLY:MARGINAL":

    import plotly.express as px
    import seaborn as sns

    tips = px.data.tips()
    print(tips)

    fig = px.scatter(
        tips,
        x="total_bill",
        y="tip",
        marginal_x="histogram",
        marginal_y="violin",
        labels=dict(total_bill="Total bill", tip="Tip"),
        title="Tips vs Total bill",
        width=400,
        height=400,
    )
    fig.show()

    fig = px.density_heatmap(
        tips,
        x="total_bill",
        y="tip",
        marginal_x="histogram",
        marginal_y="histogram",
        color_continuous_scale=px.colors.sequential.Viridis,
        nbinsx=50,
        nbinsy=50,
        labels=dict(total_bill="Total bill", tip="Tip"),
        title="Joint distribution of tip and total bill",
        width=400,
        height=400,
    )

    fig.show()


if example == "PLOTLY:SCATTERMATRIX":

    import plotly.express as px
    import seaborn as sns

    penguin = sns.load_dataset("penguins")

    fig = px.scatter_matrix(penguin, width=1200, height=1200)
    fig.show()

    fig = px.scatter_matrix(
        penguin,
        dimensions=[
            "bill_length_mm",
            "bill_depth_mm",
            "flipper_length_mm",
            "body_mass_g",
        ],
        color="species",
        width=1000,
        height=1000,
        labels=dict(
            bill_length_mm="Bill length (mm)",
            bill_depth_mm="Bill depth (mm)",
            flipper_length_mm="Flipper length (mm)",
            body_mass_g="Body mass (g)",
        ),
    ).update_traces(diagonal_visible=False)
    fig.show()


if example == "PLOTLY:PARALLEL_COORD":

    import plotly.express as px
    import seaborn as sns

    penguin = sns.load_dataset("penguins")

    penguin["species"] = penguin.species.astype("category")
    penguin["species_id"] = penguin.species.cat.codes
    fig = px.parallel_coordinates(
        penguin,
        color="species_id",
        color_continuous_scale=px.colors.diverging.Tealrose,
        height=300,
        width=1000,
    )
    fig.show()


if example == "PLOTLY:TREEMAP":

    import plotly.express as px
    import seaborn as sns
    import numpy as np

    df = px.data.gapminder().query("year == 2007")
    df["world"] = "world"  # in order to have a single root node
    fig = px.treemap(
        df,
        path=["world", "continent", "country"],  # << sets hierarchy
        values="pop",
        color="lifeExp",
        hover_data=["iso_alpha"],
        color_continuous_scale="RdBu",
        color_continuous_midpoint=np.average(df["lifeExp"], weights=df["pop"]),
    )
    fig.show()


if example == "PLOTLY:SLIDER":

    import plotly.express as px
    import seaborn as sns

    gap = px.data.gapminder()
    fig = px.scatter(
        gap,
        x="gdpPercap",
        y="lifeExp",
        animation_frame="year",  # <<
        animation_group="country",  # <<
        size="pop",
        color="continent",
        hover_name="country",
        log_x=True,
        size_max=55,
        range_x=[100, 100000],
        range_y=[25, 90],
    )
    fig.show()


# ---------------------------------
# DASH
# ---------------------------------


if example == "DASH:BARGRAPH":

    # https://dash.plotly.com/layout
    # Run this app with `python app.py` and
    # visit http://127.0.0.1:8050/ in your web browser.

    from dash import Dash, html, dcc
    import plotly.express as px
    import pandas as pd

    app = Dash(__name__)

    # assume you have a "long-form" data frame
    # see https://plotly.com/python/px-arguments/ for more options
    df = pd.DataFrame(
        {
            "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
            "Amount": [4, 1, 2, 2, 4, 5],
            "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"],
        }
    )

    fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

    app.layout = html.Div(
        children=[
            html.H1(children="Hello Dash"),
            html.Div(
                children="""
            Dash: A web application framework for your data.
        """
            ),
            dcc.Graph(id="example-graph", figure=fig),
        ]
    )

    if __name__ == "__main__":
        app.run_server(debug=True)


if example == "DASH:BASIC":

    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Input, Output
    import plotly.graph_objects as go

    app = dash.Dash(__name__)

    app.layout = html.Div(
        [
            html.P("Color:"),
            dcc.Dropdown(
                id="dropdown",
                options=[
                    {"label": x, "value": x}
                    for x in ["Gold", "MediumTurquoise", "LightGreen"]
                ],
                value="Gold",
                clearable=False,
            ),
            dcc.Graph(id="graph"),
        ]
    )

    @app.callback(Output("graph", "figure"), [Input("dropdown", "value")])
    def display_color(color):
        fig = go.Figure(data=go.Bar(y=[2, 3, 1], marker_color=color))
        return fig

    app.run_server(debug=True)



# ---------------------------------
# BOKEH
# ---------------------------------


# from bokeh.io import output_file, show
# from bokeh.models import GeoJSONDataSource
# from bokeh.plotting import figure
# from bokeh.sampledata.sample_geojson import geojson

# geo_source = GeoJSONDataSource(geojson=geojson)
# fig = figure()
# fig.circle(x="x", y="y", alpha=0.9, source=geo_source)
# # output_file("geojson.html")
# show(fig)


# LINEPLOT
# # import libraries
# from bokeh.plotting import figure, output_file, show

# # Setup some data
# x = [1, 2, 3, 4, 5]
# y = [6, 7, 2, 4, 5]
# # output_file("lines2.html")
# myPlot2 = figure(title="Another Line Example", x_axis_label="x", y_axis_label="y")
# # Add two lines
# myPlot2.line(x, y, legend="Line 1", line_width=2, line_color="green")
# myPlot2.line(x, x, legend="Line 2", line_width=2, line_color="red")
# # Show the results
# show(myPlot2)


# # HISTOGRAM
# from bokeh.plotting import Histogram, output_file, show
# from bokeh.sampledata.autompg import autompg as data

# # output_file("histogram.html",)
# # Select histogram plot type
# myPlot3 = Histogram(data["mpg"], title="MPG Distribution")
# #### THIS GAVE ME AN ERROR:  , color="red")
# show(myPlot3)


# from bokeh.plotting import scatter, output_file, show
# from bokeh.sampledata.autompg import autompg as data

# #####SCATTER
# scatter = scatter(
#     data,
#     x="mpg",
#     y="hp",
#     color="cyl",
#     marker="origin",
#     title="Auto MPG",
#     xlabel="Miles Per Gallon",
#     ylabel="Horsepower",
# )
# # output_file('scatter.html')
# show(scatter)


# exit()



# ---------------------------------
# STREAMLIT
# ---------------------------------

# import streamlit as st
# import pandas as pd
# import numpy as np

# st.title('Uber pickups in NYC')

# DATE_COLUMN = 'date/time'
# DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
#             'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

# @st.cache
# def load_data(nrows):
#     data = pd.read_csv(DATA_URL, nrows=nrows)
#     lowercase = lambda x: str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data

# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache)")

# if st.checkbox('Show raw data'):
#     st.subheader('Raw data')
#     st.write(data)

# st.subheader('Number of pickups by hour')
# hist_values = np.histogram(data[DATE_COLUMN].dt.hour, bins=24, range=(0,24))[0]
# st.bar_chart(hist_values)

# # Some number in the range 0-23
# hour_to_filter = st.slider('hour', 0, 23, 17)
# filtered_data = data[data[DATE_COLUMN].dt.hour == hour_to_filter]

# st.subheader('Map of all pickups at %s:00' % hour_to_filter)
# st.map(filtered_data)


# import altair as alt
# from vega_datasets import data

# source = data.flights_5k.url

# brush = alt.selection_interval(encodings=["x"])

# base = (
#     alt.Chart(source)
#     .transform_calculate(time="hours(datum.date) + minutes(datum.date) / 60")
#     .mark_bar()
#     .encode(y="count():Q")
#     .properties(width=600, height=100)
# )

# tmp = alt.vconcat(
#     base.encode(
#         alt.X(
#             "time:Q",
#             bin=alt.Bin(maxbins=30, extent=brush),
#             scale=alt.Scale(domain=brush),
#         )
#     ),
#     base.encode(
#         alt.X("time:Q", bin=alt.Bin(maxbins=30)),
#     ).add_selection(brush),
# )

# base | brush

# base.save("ALTAIR.html")


# exit()


# import altair as alt
# from vega_datasets import data

# source = data.seattle_weather()

# zoom = alt.selection_interval(encodings=["x", "y"])

# minimap = (
#     alt.Chart(source)
#     .mark_point()
#     .add_selection(zoom)
#     .encode(
#         x="date:T",
#         y="temp_max:Q",
#         color=alt.condition(zoom, "weather", alt.value("lightgray")),
#     )
#     .properties(
#         width=200,
#         height=200,
#         title="Minimap -- click and drag to zoom in the detail view",
#     )
# )

# detail = (
#     alt.Chart(source)
#     .mark_point()
#     .encode(
#         x=alt.X(
#             "date:T", scale=alt.Scale(domain={"selection": zoom.name, "encoding": "x"})
#         ),
#         y=alt.Y(
#             "temp_max:Q",
#             scale=alt.Scale(domain={"selection": zoom.name, "encoding": "y"}),
#         ),
#         color="weather",
#     )
#     .properties(width=600, height=400, title="Seattle weather -- detail view")
# )

# detail | minimap
# detail.save("ALTAIR.html")

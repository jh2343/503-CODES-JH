# conda install -c plotly plotly
# pip install dash


example = ""


# BOKEH
# example = "BOKEH:HISTOGRAM-1"
# example = "BOKEH:LINEPLOT"
# example = "BOKEH:SLIDER"
# example = "BOKEH:BASIC"

# ---------------------------------
# BOKEH
# ---------------------------------

# example = "BOKEH:BASIC"
if example == "BOKEH:BASIC":
    from bokeh.io import output_file, show
    from bokeh.models import GeoJSONDataSource
    from bokeh.plotting import figure
    from bokeh.sampledata.sample_geojson import geojson

    geo_source = GeoJSONDataSource(geojson=geojson)
    print(geo_source)
    fig = figure()
    fig.circle(
        x="x",
        y="y",
        alpha=0.9,
        source=geo_source,
    )
    # output_file("geojson.html")
    show(fig)

# example = "BOKEH:LINEPLOT"
if example == "BOKEH:LINEPLOT":

    # LINEPLOT
    # import libraries
    from bokeh.plotting import figure, output_file, show

    # Setup some data
    x = [1, 2, 3, 4, 5]
    y = [6, 7, 2, 4, 5]
    # output_file("lines2.html")
    myPlot2 = figure(
        title="Another Line Example",
        x_axis_label="x",
        y_axis_label="y",
    )
    # Add two lines
    myPlot2.line(
        x,
        y,
        legend="Line 1",
        line_width=2,
        line_color="green",
    )
    myPlot2.line(
        x,
        x,
        legend="Line 2",
        line_width=2,
        line_color="red",
    )
    # Show the results
    show(myPlot2)

example = "BOKEH:SLIDER"
if example == "BOKEH:SLIDER":

    from bokeh.layouts import layout
    from bokeh.models import Div, RangeSlider, Spinner
    from bokeh.plotting import figure, show

    # prepare some data
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [4, 5, 5, 7, 2, 6, 4, 9, 1, 3]

    # create plot with circle glyphs
    p = figure(
        x_range=(1, 9),
        width=500,
        height=250,
    )
    points = p.circle(
        x=x,
        y=y,
        size=30,
        fill_color="#21a7df",
    )

    # set up textarea (div)
    div = Div(
        text="""
              <p>Select the circle's size using this control element:</p>
              """,
        width=200,
        height=30,
    )

    # set up spinner
    spinner = Spinner(
        title="Circle size",
        low=0,
        high=60,
        step=5,
        value=points.glyph.size,
        width=200,
    )
    spinner.js_link("value", points.glyph, "size")

    # set up RangeSlider
    range_slider = RangeSlider(
        title="Adjust x-axis range",
        start=0,
        end=10,
        step=1,
        value=(p.x_range.start, p.x_range.end),
    )
    range_slider.js_link(
        "value",
        p.x_range,
        "start",
        attr_selector=0,
    )
    range_slider.js_link(
        "value",
        p.x_range,
        "end",
        attr_selector=1,
    )

    # create layout
    layout = layout(
        [
            [div, spinner],
            [range_slider],
            [p],
        ]
    )

    # show result
    show(layout)


# example = "BOKEH:HISTOGRAM-1"
if example == "BOKEH:HISTOGRAM-1":
    # SOURCE: https://docs.bokeh.org/en/latest/docs/gallery/histogram.html

    import numpy as np
    import scipy.special

    from bokeh.layouts import gridplot
    from bokeh.plotting import figure, show

    def make_plot(
        title,
        hist,
        edges,
        x,
        pdf,
        cdf,
    ):
        p = figure(
            title=title,
            tools="",
            background_fill_color="#fafafa",
        )
        p.quad(
            top=hist,
            bottom=0,
            left=edges[:-1],
            right=edges[1:],
            fill_color="navy",
            line_color="white",
            alpha=0.5,
        )
        p.line(
            x,
            pdf,
            line_color="#ff8888",
            line_width=4,
            alpha=0.7,
            legend_label="PDF",
        )
        p.line(
            x,
            cdf,
            line_color="orange",
            line_width=2,
            alpha=0.7,
            legend_label="CDF",
        )

        p.y_range.start = 0
        p.legend.location = "center_right"
        p.legend.background_fill_color = "#fefefe"
        p.xaxis.axis_label = "x"
        p.yaxis.axis_label = "Pr(x)"
        p.grid.grid_line_color = "white"
        return p

    # Normal Distribution

    mu, sigma = 0, 0.5

    measured = np.random.normal(mu, sigma, 1000)
    hist, edges = np.histogram(measured, density=True, bins=50)

    x = np.linspace(-2, 2, 1000)
    pdf = 1 / (sigma * np.sqrt(2 * np.pi)) * np.exp(-((x - mu) ** 2) / (2 * sigma**2))
    cdf = (1 + scipy.special.erf((x - mu) / np.sqrt(2 * sigma**2))) / 2

    p1 = make_plot("Normal Distribution (μ=0, σ=0.5)", hist, edges, x, pdf, cdf)

    # Log-Normal Distribution

    mu, sigma = 0, 0.5

    measured = np.random.lognormal(mu, sigma, 1000)
    hist, edges = np.histogram(
        measured,
        density=True,
        bins=50,
    )

    x = np.linspace(0.0001, 8.0, 1000)
    pdf = (
        1
        / (x * sigma * np.sqrt(2 * np.pi))
        * np.exp(-((np.log(x) - mu) ** 2) / (2 * sigma**2))
    )
    cdf = (1 + scipy.special.erf((np.log(x) - mu) / (np.sqrt(2) * sigma))) / 2

    p2 = make_plot("Log Normal Distribution (μ=0, σ=0.5)", hist, edges, x, pdf, cdf)

    # Gamma Distribution

    k, theta = 7.5, 1.0

    measured = np.random.gamma(k, theta, 1000)
    hist, edges = np.histogram(measured, density=True, bins=50)

    x = np.linspace(0.0001, 20.0, 1000)
    pdf = x ** (k - 1) * np.exp(-x / theta) / (theta**k * scipy.special.gamma(k))
    cdf = scipy.special.gammainc(k, x / theta)

    p3 = make_plot("Gamma Distribution (k=7.5, θ=1)", hist, edges, x, pdf, cdf)

    # Weibull Distribution

    lam, k = 1, 1.25
    measured = lam * (-np.log(np.random.uniform(0, 1, 1000))) ** (1 / k)
    hist, edges = np.histogram(measured, density=True, bins=50)

    x = np.linspace(0.0001, 8, 1000)
    pdf = (k / lam) * (x / lam) ** (k - 1) * np.exp(-((x / lam) ** k))
    cdf = 1 - np.exp(-((x / lam) ** k))

    p4 = make_plot("Weibull Distribution (λ=1, k=1.25)", hist, edges, x, pdf, cdf)

    show(
        gridplot(
            [p1, p2, p3, p4], ncols=2, width=400, height=400, toolbar_location=None
        )
    )



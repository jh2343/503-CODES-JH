import pandas as pd, numpy as np
import hvplot.pandas  # noqa
import holoviews as hv

# GENERATE DATA
idx = pd.date_range("1/1/2000", periods=1000)
df = pd.DataFrame(np.random.randn(1000, 4), index=idx, columns=list("ABCD")).cumsum()
# print(df)

# PLOT
out1 = df.hvplot(y=["A", "B","C","D"])
hv.save(out1, "hvplot-1.html")

# print(type(out))
# pd.options.plotting.backend = "holoviews"
# out2=df.A.hist()

# CUSTOMIZE
out2 = df.hvplot(
    x="A",
    y="B",
    color="red",
    alpha=0.1,
    kind="scatter",
    logx=False,
    xlabel="X Axis",
    ylabel="Y Axis",
)
hv.save(out2, "hvplot-2.html")

#COMBINE
out3 = out1 + out2
# hvplot.show(out)
hv.save(out3, "hvplot-3.html")




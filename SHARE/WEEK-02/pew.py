
import pandas as pd
import numpy  as np

print("---------------")
df1 = pd.read_csv('data/pew.csv')
print(df1)

# INCORRECT PIVOTS ON INDEX NOT COLUMN
# print("---------------")
# df2 = df1.melt()
# print(df2)

print("---------------")
df2 = df1.melt(id_vars=["religion"])
print(df2)

print("---------------")
df2 = df1.melt(id_vars=["religion"], var_name = 'income_groups', value_name='counts')
print(df2)

#REVERSE OPERATION
print("---------------")
df2 = (df2.pivot_table(index="religion", columns = "income_groups", values="counts")
    .reset_index()
    .rename_axis(None, axis=1))
print(df2)



import numpy  as np
import pandas as pd

df = pd.read_csv('data/gapminder.csv')
print("----ORIGINAL----")
print(df.head())

print("----GROUP BY CONTINENT----")
print((df.groupby('continent')).head())
# print('----\n',df.groupby('continent').tail())

print("----AVERAGE LIFE EXPECTANCY BY CONTINENT----")
print(df.groupby('continent')['lifeExp'].mean())

print("----AVERAGE LIFE EXPECTANCY BY COUNTRY----")
print(df.groupby('country')['lifeExp'].mean())

print("----AVERAGE LIFE EXPECTANCY BY CONTINENT AND YEAR----")
print(df.groupby(['continent','year'])['lifeExp'].mean())

print("----AVERAGE+MEDIAN EXPECTANCY BY YEAR----")
print(df.groupby('year')['lifeExp'].agg([np.mean,np.median]))
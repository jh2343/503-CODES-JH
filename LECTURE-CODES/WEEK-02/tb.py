
import pandas as pd

#READ
tb = pd.read_csv('data/tb.csv')
print("ORIGINAL \n", tb.head(3))

#MELT
tb1 = tb.melt(id_vars = ['iso2','year'], var_name = 'demo', value_name='counts')
print("AFTER MELT \n", tb1.head(3))

#SPLIT
tb2 = (tb1.assign(                               # create new columns
  gender = lambda x: x.demo.str[0].astype(str),
  age = lambda x: x.demo.str[1:].astype(str))
  .drop('demo', axis=1)                           # Remove old column
)
print("AFTER SPLIT \n", tb1.head(3))

print(tb2.head(3))


# TB = pd.read_csv('data/tb1.csv').melt(id_vars=['country','iso2','iso3','year'], var_name='demo', value_name='counts')
# TB.head(3)


# tmp = TB.demo.str.split('new[_]*([a-z]+)_([mf])([0-9]+)', expand=True)
# tmp.columns = ['id','type','gender','age','v5']
# TB1 = pd.concat([TB.drop('demo', axis=1),tmp.iloc[:,1:4]], axis=1)
# TB1.head()
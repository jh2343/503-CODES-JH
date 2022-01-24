#MODIFIED FROM: https://pandas.pydata.org/docs/user_guide/10min.html

import numpy as np
import pandas as pd

#SERIES
print("----------------------")
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

#DATES
print("----------------------")
dates = pd.date_range("20130101", periods=4)
print(dates)

#DATA-FRAME (FROM NP ARRAY)
# np.random.seed(seed=123243)
values=np.array([[-2,0,1,2],[1,2,3,4],[5,6,7.,8],[9,10,11,12]])
df = pd.DataFrame(values, index=dates, columns=list("ABCD"))
print(list("ABCD"))

#VIEWING DATA
print('------A------\n',df)
print('------B------\n',df.dtypes)
print(df.head())
print(df.tail(3))
print(df.index)
print(df.columns)
print(df.T)															#TRANSPOSE
print('------C------\n',df.to_numpy())
print('------D------\n',df.describe())								#GET BASIC STATISTICS 
print('------E------\n',df.sort_index(axis=0, ascending=False))  	#SORT BY AXIS
print('------F------\n',df.sort_values(by="B"))						#SORT BY VALUES 

#SELECTION

print('------G------\n',df["A"])									#GET COLUMN A
print('------H------\n',df[0:3])									#SLICE BY ROWS
print('------I------\n',df[0:3]["A"])
print('------J------\n',df.loc[dates[0]])							#EXTRACT ROW FOR dates[0]
print('------K------\n',df.loc[:, ["A", "B"]])						
print('------L------\n',df.loc["2013-01-02", ["A", "B"]])
print('------M------\n',df.loc['2013-01-02', "A"])					#RETURN A VALUE 

#SELECT BY INDEX VALUE "LOCATION" (SIMILAR TO NUMPY)
print('------O------\n',df.iloc[3])								 
print('------P------\n',df.iloc[1:2, 0:2])								 
print('------Q------\n',df.iloc[[1, 2, 3], [0, 2]])
print('------R------\n',df.iloc[1:3, :])
print('------S------\n',df.iloc[1, 1])


print("------BOOLEAN INDEXING------")
print(df[df["A"] > 0])
print('------------\n',df[df > 0])
df2 = df.copy()
df2["E"] = ["one", "two", "three", "four"]
print('------------\n',df2)
print('------------\n',df2[df2["E"].isin(["two", "four"])]) 		#SELECT VARIABLE IN LIST



# print("------SETTING------")


print("\n------MISSING DATA------")
df1=df[df > -1]
print(df1)
#TO DROP ANY ROWS THAT HAVE MISSING DATA.
tmp=df1.dropna(how="any")
print('------------')
print(tmp)
tmp=df1.fillna(value=5)
print('------------')
print(tmp)
print('------------')
print(pd.isna(df1))		#BOOLEAN MASK

# 

#---------------
# OPERATIONS
#---------------
print("\n------STATS------")
print(df)
print('------------')
print(df.mean(0)) 	#axis=0 (down rowns)
print('------------')
print(df.mean(1)) 	#axis=1 (accross columns)


print("\n------APPLY FUNCTIONS------")
print(df)
print('------------')
print(df.apply(np.cumsum)) 	#CUMULATIVE SUM DOWN COLUMN
print('------------')
print(df.apply(lambda x: x.max() - x.min()))

#DATA-FRAME (FROM NP DICTIONARY)
# print("----------------------")
# df2 = pd.DataFrame(
#     {
#         "A": 1.0,
#         "B": pd.Timestamp("20130102"),
#         "C": pd.Series(1, index=list(range(4)), dtype="float32"),
#         "D": np.array([3] * 4, dtype="int32"),
#         "E": pd.Categorical(["test", "train", "test", "train"]),
#         "F": "foo",
#     }
# )
# print(df2)
# print(df2.dtypes)


 

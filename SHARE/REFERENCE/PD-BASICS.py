#MODIFIED FROM: https://pandas.pydata.org/docs/user_guide/10min.html

import numpy as np
import pandas as pd
import seaborn as sns



#SPECIFY WHICH EXAMPLE TO RUN
# example="melting-and-pivoting"
# example="np-reshaping"
# example="series-concat"
# example='dataframe-concat'
example="joining-dataframes"
# example="get-info"
# example="lambda-functions"
# example="splitting"
# example="apply"



#SPLIT BY COMMA THEN EXPAND THEN CONCAT
df=pd.concat([df, df['Diagnosis'].str.split(', ', expand=True)], axis=1)



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


if(example=='mutate'):

	#-----------------------------
	print("----READ----")
	#-----------------------------
	mpg = pd.read_csv('data/mpg.csv')
	print(mpg.head(10))

	#-----------------------------
	print("----MUTATE----")
	#-----------------------------
	mpg['cty'] = mpg['cty'] * 1.609/3.7854 # mile/gallon --> km/l
	mpg['hwy'] = mpg['hwy'] * 1.609/3.7854
	mpg['avg'] = (mpg.cty + mpg.hwy)/2
	print(mpg.head())

	#-----------------------------
	print("----SELECT----")
	#-----------------------------
	print(mpg[['year','manufacturer','avg']])

	#-----------------------------
	print("----FILTER----")  
	#-----------------------------
	print(mpg[mpg.manufacturer=='audi'])

	#-----------------------------
	print("----ARRANGE----")  
	#-----------------------------
	print(mpg.sort_values(by=['avg'], ascending=False))

	#-----------------------------
	print("----CONVERT----")  
	#-----------------------------
	print(mpg.dtypes)
	mpg['manufacturer']=mpg.manufacturer.astype('category')
	mpg['model']=mpg.model.astype('string')
	print('--------')
	print(mpg.dtypes)


if(example=='get-info'):

        df = sns.load_dataset("mpg")
        #ERROR CHECK
        if(str(type(df)) != "<class 'pandas.core.frame.DataFrame'>"):
                raise ValueError("input variable is not panda DataFrame")

        #GENERAL STUFF THAT IS
        print("----------------------")
        print("GENERAL:")
        print("----------------------")
        print(df.index)
        print(df.columns)
        print("number of rows:", len(df.index))
        print("number of col:",  len(df.columns))
        print("keys:",  df.keys(),type(df.keys()))
        print("info",df.info() )
        print("head", df.head())
        print("TYPES", df.dtypes)

        print("----------------------")
        print("BASIC STATISTICS:")
        print("----------------------")
        print(df.describe())

        print("----------------------")
        print("CORRELATION MATRIX:")
        print("----------------------")
        print(df.corr())



if(example=='np-reshaping'):
    print("----------",example,"----------")
    #NUMPY RESHAPING (USE DF FOR PRETTY PRINT)
    A=np.array([[11,12,13],[21,22,23]])
    print('-----\n',pd.DataFrame(A))
    print('-----\n',pd.DataFrame(A.reshape(6,1)))
    print('-----\n',pd.DataFrame(A.reshape(1,6)))
    print('-----\n',pd.DataFrame(A.reshape(3,2)))
    print('-----\n',pd.DataFrame(A.T))
    print('-----\n',pd.DataFrame(np.transpose(A)))

if(example=='joining-dataframes'):
    print("----JOINING DATAFRAMES---")
    df1 = pd.DataFrame([['x1', 'y1','p1'], ['x2', 'y2','p2'], ['x3', 'y3','p3']], columns=['x', 'y','p'])
    df2 = pd.DataFrame([['x1', 'y1','w1', 'z1']
                      , ['x2','y2', 'w2', 'z2']
                      , ['x4','y4', 'w4', 'z4']],columns=['x', 'y','w', 'z'])
    print("INPUTS:")
    print(df1,'\n')
    print(df2)

    print("------")
    print('INNER JOIN: \n',df1.merge(df2, how='inner'))
    print('LEFT JOIN:  \n',df1.merge(df2, how='left'))
    print('RIGHT JOIN: \n',df1.merge(df2, how='right'))
    print('OUTER JOIN: \n',df1.merge(df2, how='outer'))
    # print('INNER: \n',df1.merge(df2, how='inner', left_on='x', right_on='x'))



if(example=='apply'):
    #Apply a function along an axis of the DataFrame.
    df1 = pd.DataFrame([[1, 2], [3, 2]], columns=['A', 'B'])
    print(df1)
    print("ADD\n",df1.apply(lambda x: x.A+x.B, axis=1))
    df1=df1.apply(lambda x: [1, 2], axis=1)
    print(df1)

if(example=="lambda-functions"):
    # https://www.w3schools.com/python/python_lambda.asp
    # A lambda function is a small anonymous function.
    # A lambda function can take any number of arguments, 
    # but can only have one expression.

    x = lambda a : a + 10
    print("EX-1:",x(5))

    x = lambda a, b : a * b
    print("EX-2:",x(5, 6))

    def myfunc(n):
        return lambda a : a * n
    mytripler = myfunc(3)
    print("EX-3:",mytripler(11))


if(example=="splitting"):

    #---------------------------------
    # SPLITTING STRINGS INTO MULTIPLE COLUMN  
    #---------------------------------
    df1 = pd.DataFrame([['m143'], ['f1232']], columns=['A'])
    print("ORIGNIAL-0\n",df1)
    
    #SPLITTING m143 --> m 143
    #Series.str()-- >Vectorized string functions for Series and Index.
    df1["MF"]  = df1.A.str[0]
    df1["NUM"] = df1.A.str[1:]
    df1=df1.drop('A',axis=1)                                 
    print("MODIFIED-0\n",df1)

    #---------------------------------
    # SPLITTING A LIST STORED AS A STRING
    #---------------------------------
    # #Series.str()-- >Vectorized string functions for Series and Index.
    df1 = pd.DataFrame([['[1, 2]','[3, 4]'], ['[NA, 6]','[7, 8]']], columns=['A', 'B'])
    print("ORIGNIAL-1\n",df1)

    df1[['A1','A2']] = pd.DataFrame(df1.A.str.replace('[','', regex=True).str.replace(']','', regex=True).str.split(',').tolist())
    df1[['B1','B2']] = pd.DataFrame(df1.B.str.replace('[','', regex=True).str.replace(']','', regex=True).str.split(',').tolist())
    df1=df1.drop(['A','B'],axis=1)                                 
    print("MODIFIED-1\n",df1)

    #---------------------------------
    # # SPLITTING STRINGS INTO MULTIPLE COLUMNS (ALTERNATIVE METHOD)
    #---------------------------------
    # df1 = pd.DataFrame([['m143'], ['f1232']], columns=['A'])
    # print("ORIGNIAL-0\n",df1)

    # #SPLITTING m143 --> m 143
    # df1 = df1.assign(                               # create new columns
    #   MF    = lambda x: x.A.str[0].astype(str),
    #   NUM   = lambda x: x.A.str[1:].astype(str)).drop('A', axis=1)                     # Remove old column
    # print("MODIFIED-0\n",df1)

    #---------------------------------
    # #SPLITTING STRINGS INTO MULTIPLE COLUMN (ALTERNATIVE METHOD)
    #---------------------------------
    # df1 = pd.DataFrame([['m143'], ['f1232']], columns=['A'])
    # print("ORIGNIAL-0\n",df1)

    # #SPLITTING m143 --> m 143
    # df1 = df1.assign(                          # create new columns
    #   MF    = df1.A.str[0],
    #   NUM   = df1.A.str[1:],
    #                 ).drop('A', axis=1)        # Remove old column
    # print("MODIFIED-0\n",df1)

    #---------------------------------
    # SPLITTING A LIST STORED AS A STRING (ALTERNATIVE METHOD)
    #---------------------------------
    # df1 = pd.DataFrame([['[1, 2]','[3, 4]'], ['[5, 6]','[7, 8]']], columns=['A', 'B'])
    # print("ORIGNIAL-2\n",df1)
    # df1['A']  = df1.apply(lambda x: x.A.replace('[','').replace(']','').split(','), axis=1)
    # df1['B']  = df1.apply(lambda x: x.B.replace('[','').replace(']','').split(','), axis=1)
    # df1[['A1','A2']] = pd.DataFrame(df1.A.tolist())
    # df1[['B1','B2']] = pd.DataFrame(df1.B.tolist())
    # df1=df1.drop(['A','B'],axis=1)
    # print("MODIFIED-2\n",df1)


if(example=="series-concat"):
    #CONCATINATING SERIES
    s1 = pd.Series(['a', 'b'])
    s2 = pd.Series(['c', 'd'])
    print("----CONCAT SERIES---")
    print(s1)
    print(pd.concat([s1, s2],axis=0))
    print(pd.concat([s1, s2],axis=1))


if(example=="dataframe-concat"):
    #CONCATINATING DATA FRAMES
    print("----CONCAT DATAFRAMES---")
    df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
    df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
    print("INPUTS:")
    print(df1)
    print(df2)
    print("CONCAT:")
    print(pd.concat([df1, df2],axis=0))
    print(pd.concat([df1, df2],axis=1))
    # print("JOINS:")
    # print(pd.concat([df1, df2], join="inner"))
    # print(pd.concat([df1, df2], join="outer"))

if(example=='melting-and-pivoting'):

    #----------------------
    #CONSIDER A SURVEY
    #----------------------
    # with 3 participants (subject) 
    # and  2 measurements (HEIGHT,WEIGHT)=(H,W)
    #print("----------",example,"----------")

    print("----WIDE FORMAT----")
    # ONE "OBSERVATION" IS ONE "PARTICIPANT"

    df1 = pd.DataFrame(
        {'ID': {0: 'ID0', 1: 'ID1', 2: 'ID2'},
         'H' : {0: "H0" , 1: "H1" , 2: "H2"},
         'W' : {0: "W0" , 1: "W1" , 2: "W2"}  ,
         'A' : {0: "A0" , 1: "A1" , 2: "A2"}
         }
                       )
    print("----LONG FORMAT----")
    # ONE "OBSERVATION" IS ONE "MEASUREMENT" OF A PARTICIPANT

    #NEED TELL IT WHAT AN "OBSERVATION" (ID) IS
    df2=pd.melt(df1, id_vars =['ID']) 
    print(df2)
    print(pd.melt(df1, id_vars =['ID','H']))
    print(pd.melt(df1, id_vars =['ID','H','W']))
    # RENAME
    # print(df.melt(id_vars=["ID"], var_name = 'var-name', value_name='VALUE'))

    #CONVERT BACK
    print("----WIDE FORMAT----")
    df2=df2.pivot(*df2).rename_axis(columns = None).reset_index() 
    print(df2)

    print("----USING INDEX NOT ID----")
    print(df1)
    print(df1.index)
    print(df1.columns)

    df2.index=df1['ID']
    df2=df2.drop(['ID'],axis=1)
    print(df2)
    print(df2.index)
    print(df2.columns)    
    print(pd.melt(df2))



    # print(df2.pivot_table(index="ID",columns=['value'])) #.reset_index().rename_axis(None, axis=1))







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


 

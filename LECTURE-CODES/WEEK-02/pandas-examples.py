#MODIFIED FROM: 
#https://pandas.pydata.org/docs/reference/api/pandas.concat.html

import pandas  as pd
import numpy   as np
import seaborn as sns

#SPECIFY WHICH EXAMPLE TO RUN
example="melting-and-pivoting"
# example="np-reshaping"
# example="series-concat"
# example='dataframe-concat'
# example="joining-dataframes"
# example="get-info"
# example="lambda-functions"
example="splitting"
example="apply"


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
    df1 = pd.DataFrame([['x1', 'y1'], ['x2', 'y2'], ['x3', 'y3']], columns=['x', 'y'])
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
    df1["NUM"] = df1.A.str[0:]
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








exit()

# #CONCATINATING SERIES











# df1 = pd.DataFrame({'lkey': ['foo', 'bar', 'baz', 'foo'],
#                     'value': [1, 2, 3, 5]})
# df2 = pd.DataFrame({'rkey': ['foo', 'bar', 'baz', 'foo'],
#                     'value': [5, 6, 7, 8]})

# print("INPUTS:")
# print(df1)
# print(df2)
# print("OUTPUTS:")
# print(df1.merge(df2, left_on='lkey', right_on='rkey'))
# # print(df1.merge(df2, how='inner', on='a'))

#INNER AND OUTER JOIN WITH CONCAT COMMAND
# print("----JOINING DATAFRAMES---")
# df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
# df3 = pd.DataFrame([['e', 5, 'cat'], ['f', 6, 'dog']],columns=['letter', 'number', 'animal'])
# print("INPUTS:")
# print(df1)
# print(df3)
# print("OUTPUTS:")
# print(pd.concat([df1, df3], join="inner"))
# print(pd.concat([df1, df3], join="outer"))


# print(pd.concat([df1, df3]))









# print(pd.concat([s1, s2], ignore_index=True))












#XTRA CODE 

# values=[["H0","W0"],["H1","W1"],["H2","W2"]]
# df = pd.DataFrame(values, index=["ID0","ID1","ID2"], columns=list("HW"))
# df=pd.melt(df) 
# print(df)

# df["method"]=['ruler','laser','laser','scale-1','scale-1','scale-2']
# print('----------')
# print(df)



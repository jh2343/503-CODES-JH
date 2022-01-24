#MODIFIED FROM: 
#https://pandas.pydata.org/docs/reference/api/pandas.concat.html

import pandas as pd
import numpy  as np

#SPECIFY WHICH EXAMPLE TO RUN
example="melting"
example="np-reshaping"
example="series-concat"
example='dataframe-concat'
example="joining-dataframes"


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

if(example=='melting'):

    #----------------------
    #CONSIDER A SURVEY
    #----------------------
    # with 3 participants (subject) 
    # and  2 measurements (HEIGHT,WEIGHT)=(H,W)

    print("----------",example,"----------")

    print("-----------")
    print("WIDE FORMAT")
    print("-----------")
    # ONE "OBSERVATION" IS ONE "PARTICIPANT"

    df = pd.DataFrame(
        {'ID': {0: 'ID0', 1: 'ID1', 2: 'ID2'},
         'H' : {0: "H0" , 1: "H1" , 2: "H2"},
         'W' : {0: "W0" , 1: "W1" , 2: "W2"},
         'A' : {0: "A0" , 1: "A1" , 2: "A2"}
         }
                       )
    print(df)

    print("-----------")
    print("LONG FORMAT")
    print("-----------")
    # ONE "OBSERVATION" IS ONE "MEASUREMENT" OF A PARTICIPANT

    #NEED TELL IT WHAT AN "OBSERVATION" (ID) IS
    df=pd.melt(df, id_vars =['ID']) 
    print(df)

    #CONVERT BACK
    print("-----------")
    print("WIDE FORMAT")
    print("-----------")
    df=df.pivot(*df).rename_axis(columns = None).reset_index() 
    print(df)








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



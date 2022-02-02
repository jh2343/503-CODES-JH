
#-------------------------------
#NOTE THIS IS JUST OF LIST OF COMMANDS 
#FOR REFERENCE AND WILL NOT RUN
#-------------------------------

# IMPORT
import pandas as pd
 
# LOAD CSV
df = pd.read_csv('input.csv')

#SAVE CSV
df.to_csv('output.csv') #, sep='\t')
df.to_csv('output.csv',index=False) #dont write index 

#RENAME COLUMN
df=df.rename(columns={"year_C": "year"})

# MELTING
pd.melt(df1, id_vars =['ID']) 
pd.melt(df1, id_vars =['ID','H'])

# BY REPEATING FIRST 5 COLUMNS 0,1,2,3,4
df=pd.melt(df, id_vars =df.columns[0:5]); # print(df)

#REPLACE NAN 
dfA=dfA.fillna('False')

dfA["A"]=dfA["A"].fillna(False)  #one column only



# SPLITTING A LIST THAT IS STORED AS A STRING
# #Series.str()-- >Vectorized string functions for Series and Index.
df1 = pd.DataFrame([['[1, 2]','[3, 4]'], ['[NA, 6]','[7, 8]']], columns=['A', 'B'])
print("ORIGNIAL-\n",df1)
df1[['A1','A2']] = pd.DataFrame(df1.A.str.replace('[','', regex=True).str.replace(']','', regex=True).str.split(',').tolist())
df1=df1.drop(['A'],axis=1)                                 
print("MODIFIED-\n",df1)

#SERIES CONCATINATION
pd.concat([s1, s2],axis=0)
pd.concat([s1, s2],axis=1)

#DATAFRAME CONCATINATION
pd.concat([df1, df2],axis=0)
pd.concat([df1, df2],axis=1)

#JOINING
df1 = pd.DataFrame([['x1', 'y1'], ['x2', 'y2'], ['x3', 'y3']], columns=['x', 'y'])
df2 = pd.DataFrame([['x1', 'y1','w1', 'z1']
                  , ['x2','y2', 'w2', 'z2']
                  , ['x4','y4', 'w4', 'z4']],columns=['x', 'y','w', 'z'])
print("INPUTS:")
print(df1,'\n')
print(df2)
print("OUTPUTS:")
print('INNER JOIN: \n',df1.merge(df2, how='inner'))
print('LEFT JOIN:  \n',df1.merge(df2, how='left'))
print('RIGHT JOIN: \n',df1.merge(df2, how='right'))
print('OUTER JOIN: \n',df1.merge(df2, how='outer'))


#KEEP ONLY ROWS FOR WHICH COLUMN A='Y'
df = df[df['A'] == 'Y']

#REMOVE A COLUMN(S)
df = df.drop('A',axis=1)
df = df.drop(['A','B','C'],axis=1)

#MAKE A NEW COLUMN "A" BY SELECTING A SUB-STRING FROM col1
df["A"]  = df.col1.str[0:2]


#MAKE NEW ROW FROM BOOLEAN OPERATION ON ROW "B" 
df['A'] = df['B'].apply(lambda x: True if ((x=="cat") | (x=="dog")) else False)

# MUTATE 
mpg['cty'] = mpg['cty'] * 1.609/3.7854 # mile/gallon --> km/l
mpg['hwy'] = mpg['hwy'] * 1.609/3.7854
mpg['avg'] = (mpg.cty + mpg.hwy)/2

# SELECT
mpg[['year','manufacturer','avg']]

# FILTER 
mpg[mpg.manufacturer=='audi']

# ARRANGE 
 mpg.sort_values(by=['avg'], ascending=False)

# CHANGE DATA TYPE 
mpg['manufacturer']=mpg.manufacturer.astype('category')
mpg['model']=mpg.model.astype('string')


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


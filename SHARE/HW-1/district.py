#IMPORT
import pandas as pd

#READ
df = pd.read_csv('data/districts.csv')
print("START\n",df)


#RENAME id
df=df.rename(columns={"id": "district_id"})
 
#SPLIT ARRAYS INTO PARTS
df[['N_mun_pop_0_500','N_mun_pop_500_2000','N_mun_pop_2000_10000','N_mun_pop_10000_INF']] = pd.DataFrame(df.municipality_info.str.replace('[','', regex=True).str.replace(']','', regex=True).str.split(',').tolist())
df[['unemployment_rate_95','unemployment_rate_96']] = pd.DataFrame(df.unemployment_rate.str.replace('[','', regex=True).str.replace(']','', regex=True).str.split(',').tolist())
df[['crime_rate_95','crime_rate_96']] = pd.DataFrame(df.commited_crimes.str.replace('[','', regex=True).str.replace(']','', regex=True).str.split(',').tolist())
df=df.drop(['municipality_info','unemployment_rate','commited_crimes'],axis=1); 

#SAVEs
df.to_csv('districts_py.csv',index=False) #, sep='\t')
print("END\n",df)
# 

#--------------
#XTRA CODE
#-------------- 

# CRIME RATE 

#MELT CRIME COLUMN 
# df=pd.melt(df, id_vars =df.columns[0:14]); 

# #SPLIT 
# df["year_C"]  = df.variable.str[1:]
# df=df.drop('variable',axis=1); 
# df=df.rename(columns={"value": "crime_rate"})
# # df["year"]  = df.variable.str[0]



# # UNEMPLOYMENT

# #MOVE U95 and U96 TO END (METHOD-1)
# tmp=['U95','U96'] 
# df2 = df[tmp].copy()
# df = df.drop(tmp, axis=1)
# df = pd.concat([df, df2],axis=1)
# print(df)

# #MELT
# df=pd.melt(df, id_vars =df.columns[0:len(df.iloc[0])-2]); 

# #SPLIT
# df["year_U"]  = df.variable.str[1:]
# df=df.drop('variable',axis=1); 
# df=df.rename(columns={"value": "unemployment_rate"})

# #REMOVE LINES WHERE year_U != year_C
# df = df[df['year_U'] == df['year_C']
# df=df.drop('year_U',axis=1); 
# df=df.rename(columns={"year_C": "year"})


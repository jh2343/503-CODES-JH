import pandas as pd

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

#NOTES:

#DEFINITIONS
# MUTATE  = TRANSFORM A COLUMN WITH SOME FUNCTION
# SELECT  = SELECT SOME COLUMNS IN THE DATA
# FILTER  = KEEP ONLY ROWS THAT MEET SOME DATA CRITERION
# ARRANGE = ORDER THE DATA FRAME BY VALUES OF A COLUMN(S)

#CONVERSION
# CONVERT THE CITY AND HIGHWAY FUEL 
# EFFICIENCY TO KM/L, AND
# FIND AVERAGE FUEL EFFICIENCY
# 1 mile=1.60934KM
# 1 gallon=3.7854 liter

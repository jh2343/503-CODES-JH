library(tidyverse)

#-----------------------------
print("----READ----")
#-----------------------------
mpg1 <- read_csv('data/mpg.csv')
head(mpg1)

#-----------------------------
print("----MUTATE----")
#-----------------------------
# OPTION-1: SEND MPG TO MUTATE
 mpg2 <- mutate(mpg1, cty = cty * 1.6/3.8,
         hwy = hwy * 1.6/3.8, 
         avg = (cty + hwy)/2)
head(mpg2); #print(mpg2['avg'])

#-----------------------------
print("----MUTATE----")
#-----------------------------
#OPTION-2: PIPE MPG INTO MUTATE 
mpg1 <- mpg1 %>% mutate(cty = cty * 1.6/3.8,
         hwy = hwy * 1.6/3.8, 
         avg = (cty + hwy)/2)
head(mpg1)

#-----------------------------
print("----SELECT----")
#-----------------------------
mpg2 <- mpg1 %>% select(year, manufacturer, avg)
head(mpg2)

#-----------------------------
print("----FILTER----")  
#-----------------------------
mpg2 <- mpg1 %>% filter(manufacturer=='audi')
head(mpg2)

#-----------------------------
print("----ARRANGE----")  
#-----------------------------
mpg2 <-mpg1 %>% arrange(-year)
head(mpg2)

#-----------------------------
print("----FILTER THEN ARRANGE----")  
#-----------------------------
#CHAIN TOGETHER 
mpg2 <-mpg1 %>% filter(manufacturer=='audi') %>% arrange(-year)  
head(mpg2,3)

#-----------------------------
#CONVERT TO FACTOR 
#-----------------------------
mpg2['model']=as.factor(mpg2$model)
head(mpg2,3)


#NOTES:

# %>% (similar to | in linux) is called the forward pipe operator in R.
# It provides a mechanism 
# for chaining commands with a new forward-pipe operator, %>%. 
# This operator will forward a value, or the result of an expression,
# into the next function call/expression.
# It is defined by the package magrittr (CRAN) and is heavily used by dplyr (CRAN).


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


library("tidyverse")

#READ
tb <- read_csv('data/tb.csv')


#PRINTING
print(df,n=1)
print(df %>% select(unemployment_rate))
print(df %>% pull(unemployment_rate) )



library('tidyverse')

print("----ORIGINAL----")
gap <- read_csv('data/gapminder.csv')
head(gap)

print("----GROUP BY CONTINENT----")
gap %>% group_by(continent)

print("----AVERAGE LIFE EXPECTANCY BY CONTINENT----")
gap %>% group_by(continent) %>% summarize(avgLifeExp = mean(lifeExp))


print("----AVERAGE LIFE EXPECTANCY BY COUNTRY----")
gap %>% group_by(country) %>% summarize(avgLifeExp = mean(lifeExp))

print("----AVERAGE LIFE EXPECTANCY BY CONTINENT AND YEAR----")
gap %>% group_by(continent, year) %>% summarize(mean(lifeExp))

print("----AVERAGE+MEDIAN EXPECTANCY BY YEAR----")
gap %>% group_by(year) %>% summarize(means = mean(lifeExp), medians = median(lifeExp))



# WE NEED TO MELT THIS DATASET TO MAKE IT TIDY
pew1 <- pew %>% pivot_longer(cols = c(-religion), names_to = 'income_groups', values_to = 'counts')
print(pew1)


#WE REVERSE THIS PROCESS BY PIVOTING THE DATA SET
pew2 <- pew1 %>% pivot_wider(id_cols = c(religion), names_from = 'income_groups', values_from = 'counts')
head(pew2,2)


#READ
tb <- read_csv('data/tb.csv')
print("ORIGINAL")
head(tb, 3)

#MELT
tb1 <- tb %>% pivot_longer(cols=m014:f65, names_to='demo', values_to='counts')
print("AFTER MELT")
head(tb1, 3)

#SPLIT
tb2 <- tb1 %>% separate(demo, c('gender','age'), sep = "[,]")
print("AFTER SPLIT ")
print(head(tb2, 3))



# TB <-  read_csv('data/tb1.csv') %>% 
#   pivot_longer(cols = starts_with('new'),names_to='demo', values_to='counts')
# head(TB, 3)

# TB1 <- TB %>% extract(demo, c('type','gender','age'),  regex = 'new[_]*([a-z]+)_([mf])([0-9]+$)')
# head(TB1)

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

#LOAD DATA
df1 <- read_csv('data/toy-1.csv')
df2 <- read_csv('data/toy-2.csv')


print("----ORIGINAL----")
head(df1)
head(df2)

print("----INNER JOIN----")
df1 %>% inner_join(df2) %>% head()
df1 %>% inner_join(df2, by = c('x')) %>% head()
df1 %>% inner_join(df2, by = c('x' , 'w')) %>% head()

print("----LEFT JOIN----")
df1 %>% left_join(df2) %>% head()
# df1 %>% left_join(df2,by = c('x' , 'y')) %>% head()

print("----RIGHT JOIN----")
df1 %>% right_join(df2) %>% head()

print("----FULL JOIN----")
df1 %>% full_join(df2) %>% head()


# library(tibble)
# tibble(mtcars)
# head(mtcars)
# glimpse(mtcars)
# glimpse(mtcars[3:4])
# colnames(mtcars)






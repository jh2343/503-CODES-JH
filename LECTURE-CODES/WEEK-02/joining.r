
library('tidyverse')

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

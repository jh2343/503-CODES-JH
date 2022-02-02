

library("tidyverse")

#READ
tb <- read_csv('data/tb.csv')
print("ORIGINAL")
head(tb, 3)

#MELT
tb1 <- tb %>% pivot_longer(cols=m014:f65, names_to='demo', values_to='counts')
print("AFTER MELT")
head(tb1, 3)

#SPLIT
tb2 <- tb1 %>% separate(demo, c('gender','age'), sep = 1)
print("AFTER SPLIT ")
print(head(tb2, 3))



# TB <-  read_csv('data/tb1.csv') %>% 
#   pivot_longer(cols = starts_with('new'),names_to='demo', values_to='counts')
# head(TB, 3)

# TB1 <- TB %>% extract(demo, c('type','gender','age'),  regex = 'new[_]*([a-z]+)_([mf])([0-9]+$)')
# head(TB1)
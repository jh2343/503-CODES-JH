

library(tidyverse)

pew <- read_csv('pew.csv')
head(pew)

# WE NEED TO MELT THIS DATASET TO MAKE IT TIDY

pew1 <- pew %>% pivot_longer(cols = c(-religion), names_to = 'income_groups', values_to = 'counts')
head(pew1)

# There is a difference in row-order between the R and Python solutions.
# R sorts by the id variable(s), Python sorts on the column containing
# the old column headers. Analytically, this can be fixed, and is often not important for visualization.


#WE REVERSE THIS PROCESS BY PIVOTING THE DATA SET
pew2 <- pew1 %>% pivot_wider(id_cols = c(religion), names_from = 'income_groups', values_from = 'counts')
head(pew2,2)


# mis <- rjson::fromJSON(file='miserables.json')
# print(mis)
# # class(mis)

# mis <- jsonlite::fromJSON('data/miserables.json')
# class(mis)
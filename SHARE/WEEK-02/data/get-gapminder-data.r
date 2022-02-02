
# install.packages("gapminder")
library("gapminder")  #TO PULL DATASET
library("tidyverse")  #FOR WRITING
print(gapminder)
write_csv(gapminder,'gapminder.csv')
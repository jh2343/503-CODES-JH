
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

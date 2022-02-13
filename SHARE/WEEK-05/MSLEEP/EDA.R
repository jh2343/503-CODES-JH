library(tidyverse)

#MISSING VALUE VIZ LIBRARIES 
#RUN FOLLOWING TO INSTALL --> install.packages("systemfonts", type = "source")
library(visdat)
library(hrbrthemes)
library(naniar)


#DATA SUMMARY PACKAGE
library(skimr)
# install.packages('devtools')
# devtools::install_github("rstudio/ggvis", build_vignettes = FALSE)


#DOWNLOAD AND SAVE DATASET
# data(msleep); print(msleep)
# write.table(msleep , file = "msleep.csv", sep=",", row.names = FALSE)


#READ FILE 
df <- read_csv('msleep.csv')

#CHANGE NAME OF OUTPUT FILE
pdf(file="msleep.pdf")

#-----------------------
#INTIIAL NUMERICAL EXPLORE
#-----------------------

print("-----PRINT----")
print(df)

#slice and explore select columns/rows 
# print(df$name)
# print(df[1:3,])
# print(df[,1])
# print(df %>% select( where(is.numeric)))
df %>% slice_max(bodywt, n=5)


print("-----TAIL----")
tail(df)

print("-----STR----")
str(df)

print("-----GLIMPSE----")
glimpse(df)

print("-----DATA SUMMARY: BASE----")

#Base R provides a method that gets you information
#, but is not very good
df %>% select(vore, where(is.numeric)) %>% 
mutate(vore = as.factor(vore)) %>% 
summary()

print("-----DATA SUMMARY: SKIMR----")
#skimr provides a more attractive output
skim(msleep) #%>% knit_print(render=knit_print)

print("-----DATA SUMMARY: MANUAL----")
df %>% select( where(is.numeric)) %>% 
  pivot_longer(names_to = 'Variable', values_to = 'value', cols=everything()) %>% 
  group_by(Variable) %>% 
  summarise(Mean = mean(value, na.rm=T),
            Median = median(value, na.rm=T),
            SD = sd(value, na.rm=T))




# #GGPLOT2 PLOT HISTOGRAMS  
# df %>% select(where(is.numeric)) %>% 
#   pivot_longer(names_to = "Variable", values_to="value", cols=everything()) %>% 
#   ggplot(aes(x = value)) + geom_histogram() + 
#   facet_wrap(~Variable, scales='free')

# #LOG-BASE-10 TRANFORM
df1 <- df %>% 
  select(vore, where(is.numeric)) %>% 
  mutate(across(ends_with('wt'), log10))

# df %>% select(where(is.numeric)) %>% 
#   pivot_longer(names_to = "Variable", values_to="value", cols=everything()) %>% 
#   ggplot(aes(x = value)) + geom_histogram() + 
#   facet_wrap(~Variable, scales='free')



print("-----GROUP SUMMARIES----")
library(tableone)
df %>% 
  select(vore, where(is.numeric)) %>% 
  CreateTableOne(vars = setdiff(names(.), 'vore'),
                 strata='vore') %>% 
  kableone()



df %>% 
  select(vore, where(is.numeric)) %>% 
  pivot_longer(names_to = 'variables', values_to = 'values',cols = c(-vore)) %>% 
  group_by(vore, variables) %>% 
  summarize(M = mean(values, na.rm=T)) %>% 
  pivot_wider(names_from=vore, values_from = M) %>% 
  knitr::kable(digits=2) 
  #  %>% 
  # kable_styling()


ggplot(df, aes(sleep_total))+geom_density() + facet_wrap(~vore)


#BIVARIATE GRAPH
GGally::ggpairs(df %>% select(starts_with('sleep')))

#BIVARIATE GRAPH
ggplot(df, aes(x = bodywt, y = sleep_rem))+
  geom_point() + 
  geom_smooth()

ggplot(df1, aes(x = bodywt, y = sleep_rem))+
  geom_point() + 
  geom_smooth()


#CORRELATION HEAT MAP
vis_cor(df  %>% select( where(is.numeric)))


#RELATING A CONTINUOUS TO A CATEGORICAL VARIABLE
ggplot(df1, aes(x = vore, y = bodywt))+geom_boxplot()
ggplot(df, aes(x = vore, y = bodywt))+geom_boxplot() # Original scale


ggplot(df1, aes(x = vore, y = sleep_rem ))+geom_boxplot()



#-----------------------
#VISUALLY EXPLORE MISSING VALUES
#USING naniar PACKAGE
#-----------------------

gg_miss_var(df) # Proportion missing by variable
gg_miss_upset(msleep) # Missing data patterns


#-----------------------
#VISUALLY EXPLORE MISSING VALUES
#USING vis_dat PACKAGE
#-----------------------

theme_set(theme_ipsum())
vis_dat(df)
vis_miss(df)

#-----------------------
#REMOVING MISSING VALUES
#----------------------

#REMOVE ALL ROWS WITH NA IN THEM
# df <- drop_na(df)
# vis_miss(df)

#REMOVE ANY COLUMN WITH NA 
# df <-  df[ , colSums(is.na(df)) == 0]
# vis_miss(df)

#HYBRID REMOVE SELECT COL THEN REMOVE ALL ROWS WITH NA 
# df <-  df[ , c(1,2,3,4,6)] #SELECT WHAT TO KEEP 

# Dplyr remove select col by column number
df <- select(df, c(-5,-7,-8,-10))
df <- drop_na(df) 	#remove all rows with NA
vis_miss(df)





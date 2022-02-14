library(tidyverse)

#-----------------------------
# SETUP
#-----------------------------

#READ FILE 
df <- read_csv('msleep.csv')

#CHANGE NAME OF OUTPUT FILE
pdf(file="msleep-2.pdf")


#----------------------------------------------------
# GRAPHICAL EDA
#----------------------------------------------------

#-----------------------
# VARIOUS PLOTS
#-----------------------

# GGPLOT2 PLOT HISTOGRAMS  
msleep %>% select(where(is.numeric)) %>% 
  pivot_longer(names_to = "Variable", values_to="value", cols=everything()) %>% 
  ggplot(aes(x = value)) + geom_histogram() + 
  facet_wrap(~Variable, scales='free')

# #LOG-BASE-10 TRANFORM
df1 <- df %>% 
  select(vore, where(is.numeric)) %>% 
  mutate(across(ends_with('wt'), log10))


#RE-PLOT HISTOGRAMS  
df1 %>% select(where(is.numeric)) %>% 
  pivot_longer(names_to = "Variable", values_to="value", cols=everything()) %>% 
  ggplot(aes(x = value)) + geom_histogram() + 
  facet_wrap(~Variable, scales='free')

#SMOOTH HISTOGRAM PLOT (KDE)
ggplot(df, aes(sleep_total))+geom_density() + facet_wrap(~vore)

#BIVARIATE GRAPH
ggplot(df, aes(x = bodywt, y = sleep_rem))+
  geom_point() + 
  geom_smooth()

#BIVARIATE GRAPH WITH CORRELATION VALUES AND PAIRPLOT
print("--TEST--")
df %>%select(starts_with('sleep'))
GGally::ggpairs(df %>% select(starts_with('sleep')))

#RELATING A CONTINUOUS TO A CATEGORICAL VARIABLE
ggplot(df1, aes(x = vore, y = bodywt))+geom_boxplot()
ggplot(df, aes(x = vore, y = bodywt))+geom_boxplot() # Original scale
ggplot(df1, aes(x = vore, y = sleep_rem ))+geom_boxplot()


quit()





















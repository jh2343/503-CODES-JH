library(tidyverse)

#MISSING VALUE VIZ LIBRARIES 
#RUN FOLLOWING TO INSTALL --> install.packages("systemfonts", type = "source")
library(visdat)
library(hrbrthemes)
library(naniar)


# #-----------------------------
# # SETUP
# #-----------------------------

# #DATA SUMMARY PACKAGE
library(skimr)
# install.packages('devtools')
# devtools::install_github("rstudio/ggvis", build_vignettes = FALSE)

#DOWNLOAD AND SAVE DATASET
# data(msleep); print(msleep)
# write.table(msleep , file = "msleep.csv", sep=",", row.names = FALSE)

#READ FILE 
df <- read_csv('msleep.csv')

#CHANGE NAME OF OUTPUT FILE
pdf(file="msleep-1.pdf")


#----------------------------------------------------
# NON-GRAPHICAL EDA
#----------------------------------------------------


#-----------------------
# FIRST LOOK AT THE DATA 
#-----------------------
print("PRINT:")
print(df)

print("TAIL:")
tail(df)

print("STR:")
str(df)
print("GLIMPSE:")
glimpse(df)

#-----------------------
#SELECTING SUBSETS OF THE DATA
#-----------------------
#SLICING: MAY NEED TO MANUALLY REMOVE ROW/COLUMN 
# slice and explore select columns/rows 

print("SELECT COLUMN(S):")
print(df$name)
print(df[,1])
select(df,vore)
df %>%select(vore)
df %>%select(vore,order)
df %>%select(c(vore,order,conservation))


print("CHANGE COLUMN TO FACTOR:")
df <- df %>% mutate(vore = as.factor(vore))
print(df); 

print("SELECT ROWS:")
print(df[1:3,])

print("ISOLATE ONLY NUMERIC ROWS:")
print(df %>% select( where(is.numeric)))

print("ISOLATE VORE COLUMN AND ALL NUMERIC COLUMNS:")
df %>%select(vore, where(is.numeric))

print("SORT BY sleep_total AND SLICE")
df %>% slice_max(sleep_total, n=10)

print("SELECT ONLY COLUMNS YOU TO KEEP ")
df[ , c(1,2,3,6,7)] 

#-----------------------
# REMOVING MISSING VALUES
#-----------------------

print("REMOVE ALL ROWS WITH NA IN THEM")
drop_na(df)

print("REMOVE ANY COLUMN WITH NA")
df[ , colSums(is.na(df)) == 0]

print("#HYBRID: REMOVE SELECT COL THEN REMOVE ALL ROWS WITH NA ")
df2 <- select(df, c(-5,-7,-8,-10))
drop_na(df2)   #remove all rows with NA


#-----------------------
# DATA SUMMARIES 
#-----------------------

#THEN LOOK AT THE STATISTICS
print("-----DATA SUMMARY: BASE----")

#METHOD-1: BASE-R
print("FULL")
summary(df)
#Base R provides a method that gets you information, but is not very good

print("PARTIAL")
df %>% select(vore, where(is.numeric)) %>% 
summary()

print("-----DATA SUMMARY: SKIMR----")
#skimr provides a more attractive output
skim(df) #%>% knit_print(render=knit_print)


print("-----DATA SUMMARY: MANUAL----")
df %>% select( where(is.numeric)) %>% 
  pivot_longer(names_to = 'Variable', values_to = 'value', cols=everything()) %>% 
  group_by(Variable) %>% 
  summarise(Mean = mean(value, na.rm=T),
            Median = median(value, na.rm=T),
            SD = sd(value, na.rm=T))

print("-----GROUP SUMMARIES-1----")
library(tableone)
df %>% 
  select(vore, where(is.numeric)) %>% 
  CreateTableOne(vars = setdiff(names(.), 'vore'),
                 strata='vore') %>% 
  kableone()

print("-----GROUP SUMMARIES-2----")
df %>% 
  select(vore, where(is.numeric)) %>% 
  pivot_longer(names_to = 'variables', values_to = 'values',cols = c(-vore)) %>% 
  group_by(vore, variables) %>% 
  summarize(M = mean(values, na.rm=T)) %>% 
  pivot_wider(names_from=vore, values_from = M) %>% 
  knitr::kable(digits=2) 
  #  %>% 
  # kable_styling()


# ----------------------------------------------------
# GRAPHICAL EDA
# ----------------------------------------------------

#-----------------------
# VISUALLY EXPLORE MISSING VALUES
# USING naniar PACKAGE
#-----------------------

gg_miss_var(df) # Proportion missing by variable
gg_miss_upset(msleep) # Missing data patterns

#-----------------------
# VISUALLY EXPLORE MISSING VALUES
# USING vis_dat PACKAGE
#-----------------------

theme_set(theme_ipsum())
vis_dat(df)
vis_miss(df)

#CORRELATION HEAT MAP
vis_cor(df  %>% select( where(is.numeric)))








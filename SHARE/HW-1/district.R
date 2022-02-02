

library("tidyverse")


#READ
df <- read_csv('data/districts.csv')

#RENAME id
df <- rename(df, "district_id" = "id")

#PRINTING
# print(df,n=1)
# print(df %>% select(unemployment_rate))
# print(df %>% pull(unemployment_rate) )

#PRINT
# print(df %>% select(unemployment_rate))
# print(df %>% select(commited_crimes))
print(df %>% select(municipality_info))

#SPLIT INTO COLUMNS USING COMMA DELIMITER AND REMOVE [ ]
df <-  df %>% separate(unemployment_rate, c('unemployment_rate_95','unemployment_rate_96'), sep = ",", remove = TRUE)
df$unemployment_rate_95 <- as.numeric(str_replace(df$unemployment_rate_95, "\\[", ''))
df$unemployment_rate_96 <- as.numeric(str_replace(df$unemployment_rate_96, "\\]", ''))

#PRINT
print(df %>% select(unemployment_rate_95))
print(df %>% select(unemployment_rate_96))

#SPLIT INTO COLUMNS USING COMMA DELIMITER AND REMOVE [ ]
df <-  df %>% separate(commited_crimes, c('crime_95','crime_96'), sep = ",", remove = TRUE)
df$crime_95 <- as.integer(str_replace(df$crime_95, "\\[", ''))
df$crime_96 <- as.integer(str_replace(df$crime_96, "\\]", ''))

#SPLIT INTO COLUMNS USING COMMA DELIMITER AND REMOVE [ ]
df <-  df %>% separate(municipality_info, c('N_mun_pop_0_500','N_mun_pop_500_2000','N_mun_pop_2000_10000','N_mun_pop_10000_INF'), sep = ",", remove = TRUE)
df$N_mun_pop_0_500 <- as.integer(str_replace(df$N_mun_pop_0_500, "\\[", ''))
df$N_mun_pop_500_2000 <- as.integer(df$N_mun_pop_500_2000)
df$N_mun_pop_2000_10000 <- as.integer(df$N_mun_pop_2000_10000)
df$N_mun_pop_10000_INF <- as.integer(str_replace(df$N_mun_pop_10000_INF, "\\]", ''))

# WRITE
write.table(df , file = "districts_r.csv", sep=",", row.names = FALSE)


# #PRINT
# print(df %>% select(N_mun_pop_0_500))
# print(df %>% select(N_mun_pop_500_2000))
# print(df %>% select(N_mun_pop_2000_10000))
# print(df %>% select(N_mun_pop_10000_INF))


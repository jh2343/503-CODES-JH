library("tidyverse")

#READ
df <- read_csv('data/loans.csv')
# print(df)
print(colnames(df)[1:4])

#RENAME id
df <- rename(df, "loan_id" = "id")

# 'loan_id','account_id','date','amount','payments'

#MELT
df <- df %>% pivot_longer(cols = colnames(df)[6:length(colnames(df))])

#REMOVE ROWS WITH '-' AND THEN GROUP X COLUMN
df <- df %>% filter(value=='X')
df <- df %>% select(-one_of('value'))

#SPLIT 24_A --> 24 A 
df <- df %>% separate(name, c('loan_term','letter'), sep = 2)
df$loan_term <- as.integer(df$loan_term)
df$letter <- str_replace(df$letter, "\\_", '')

# #CONVERT LETTER INTO default and expired 
df$loan_status <- ifelse(df$letter =="A" | df$letter =="B", "expired", "current")
df$loan_default <- ifelse(df$letter =="B" | df$letter =="D", TRUE, FALSE)
df <- df %>% select(-one_of('letter'))

# WRITE
write.table(df , file = "loans_r.csv", sep=",", row.names = FALSE)
print(df)



# #CONVERT LETTER INTO default and expired 
# df['loan_status']    = df['letter'].apply(lambda x: "expired" if ((x=="A") | (x=="B")) else "current")
# df['loan_default'] = df['letter'].apply(lambda x:  True if ((x=="B") | (x=="D")) else False)
# df=df.drop('letter',axis=1); 
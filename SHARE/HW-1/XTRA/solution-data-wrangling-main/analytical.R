library(tidyverse)

# Get the filenames with full paths
files <- list.files(pattern = "\\.csv", 
                    path = "data/", full.names = T)

# Function to read in a path and create an object in the 
# workspace with the name of the file without the .csv
read_and_assign <- function(f) {
  tname <- gsub("\\.csv", "", basename(f))
  d_in <- readr::read_csv(f)
  assign(x = tname, value = d_in, envir = .GlobalEnv)
}


library(purrr)
purrr::map(files, read_and_assign)

# need tidy loans
loans <- read_csv("loans_r.csv")

# Start building the analytics dataset. The unit is accounts
# so start with accounts table with renamed fields
# and left join everything else

an <- 
  accounts |> 
  rename(account_id = id, 
         open_date = date)

# Add the district name and remove the district id

an <- an |> 
  left_join(districts |> select(district_id = id,
                                district_name = name)) |> 
  select(-district_id)


# To get the number of customers, I need to aggregate the links table
# and join to master

an <- an |> 
  left_join(links |> count(account_id) |> rename(num_customers = n))


# To find the number of credit cards aggreagate cards table joined
# to links to get account id
# also replace NA's with 0 after joining

cards_links <- 
  cards |> left_join(links |> select(link_id = id, account_id))

an <- an |> 
  left_join(cards_links |> 
              count(account_id) |> 
              rename(credit_cards = n)) |> 
  mutate(credit_cards = replace_na(credit_cards, 0)) |> glimpse()

# Add loan info from the loans_r file (already read in) and 
# create a boolean wether there is a loan or not (any of the 
#loan fields will suffice)

an <- an |> 
  left_join(loans |> 
              select(-id,-date) |> 
              rename(loan_amount = amount,
                     loan_payments = payments)) |> 
  mutate(loan = ifelse(is.na(loan_amount), FALSE, TRUE))


## Analyze the transactions, by account_id

# for withdrawal, you need to filter by debits
withdrawals <- 
  transactions |> 
  filter(type == "debit") |> 
  group_by(account_id) |> 
  summarize(
    max_withdrawal = max(amount, na.rm = T),
    min_withdrawal = min(amount, na.rm = T)
  )

# for cc payments, you need to look only at debits with 
# credit card method
pmts_to_cc <- 
  transactions |> 
  filter(type == "debit", method == "credit card") |> 
  count(account_id) |> 
  rename(cc_payments = n)


# for balance, it's across all transactions for the account

balances <- 
  transactions |> 
  group_by(account_id) |> 
  summarize(
    max_balance = max(balance, na.rm = T),
    min_balance = min(balance, na.rm = T)
  )

# now join all the remaining stuff together

an <- 
  an |> 
  left_join(withdrawals) |> 
  left_join(pmts_to_cc) |> 
  left_join(balances)

# The order of the variables doesn't really matter

write_csv(an, file = "analytical_r.csv", na = "")

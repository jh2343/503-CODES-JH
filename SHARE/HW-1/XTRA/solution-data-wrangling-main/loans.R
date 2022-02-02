library(tidyverse)

loans <- read_csv("data/loans.csv")

# Tidy the data
loans |> 
  pivot_longer(cols = 6:25) |> # melt the cols 6-25, the A_XX
  filter(value == "X") |> # remove the rows with dashes, keep the X's
  select(-value) |> 
  separate(name, into = c("loan_term", "info"), sep = "_") |> 
  mutate(
    loan_status = ifelse(info %in% c("A", "B"), 
                         "expired",
                         "current"),
    loan_default = info %in% c("B", "D")
  ) |> 
  select(-info) -> loans_tidy

write_csv(loans_tidy, file = "loans_r.csv", na = "")

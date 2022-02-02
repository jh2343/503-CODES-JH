library(tidyverse)

district <- read_csv("data/districts.csv")

district |> 
  mutate(
    across(c(municipality_info, unemployment_rate, commited_crimes),
           function(x) gsub("\\[|\\]", "", x))
  ) |> 
  separate(col = municipality_info, 
             into = c("ct_mun_pop_lt_500",
                      "ct_mun_pop_500_1999",
                      "ct_mun_pop_2000_9999",
                      "ct_mun_pop_gt_10000"),
             sep = ",") |> 
  separate(col = unemployment_rate,
           into = c("unemployment_rate_95",
                    "unemployment_rate_96"),
           sep = ",") |> 
  separate(col = commited_crimes,
           into = c("commited_crimes_95",
                    "commited_crimes_96"),
           sep = ",") -> district_tidy

write_csv(district_tidy, file = "district_r.csv", na = "")           

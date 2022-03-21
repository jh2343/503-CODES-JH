  
library(tidyverse)

n  <-  5000
d2  <-  data.frame(x  =  rnorm(n),  y  =  rnorm(n))
# g <- ggplot(d2,  aes(x,  y))+geom_point()
g <- ggplot(d2,  aes(x,y))+geom_point(alpha  =  0.1)

plot(g)
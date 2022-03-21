#TICTOC --> LIBRARY FOR MEASURING TIME ELAPSE
library(tictoc)
#install.packages("tictoc")
library(tidyverse)

for (i in 1:25) {

	N=2**i

	tic(N)

	x<-seq(0, 2*3.1415,  2*3.1415/(N-1))
	y<-sin(x)
	#print(x); print(y)

	df=data.frame(x = x, y = y) #%>%
	    # pivot_longer(-x) 

	#print(df)
	gg <- ggplot(df,aes(x, y)) +
	    geom_point()
	plot(gg)
	# sleep_for_a_minute()
	toc()

}
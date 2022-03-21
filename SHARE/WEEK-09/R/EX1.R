library(rasterly)

#GENERATE DATA
N=2**25
print(N)
x<-seq(0, 2*3.1415,  2*3.1415/(N-1))
y<-sin(x)
d  <-  data.frame('x'=x,  'y'=y)

#START TIME 
start  =  Sys.time()

#PLOT
p  <-  d  %>%  rasterly(mapping  =  aes(x,  y))  %>%
rasterly_points()
p

#COMPUTE TIME ELAPSES
times  <-  (Sys.time()  -start)
print(times)

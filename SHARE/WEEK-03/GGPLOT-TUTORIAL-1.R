#MODIFIED FROM 
#http://r-statistics.co/Complete-Ggplot2-Tutorial-Part1-With-R-Code.html
#RSTUDIO: BLOCK COMMENT Ctrl + Shift + C

#-------------------------------
#SETUP
#-------------------------------
library(ggplot2)

# turn off scientific notation like 1e+06
options(scipen=999)

#LOAD DATA
#Loads specified data sets, or list the available data sets.
data("midwest", package = "ggplot2")  # load the data
# midwest <- read.csv("http://goo.gl/G1K41K") # alt source 

#EXPLORE DATA: DATA COMES IN AS A TIBBLE  
print(midwest)



#SCATTER PLOT-1
# aes=Aesthetic mappings describe how variables in the data 
# are mapped to visual properties (aesthetics) of geoms.
g <- ggplot(midwest, aes(x=area, y=poptotal)) + #TELL IT WHAT TO PLOT
geom_point()                                    #DO SCATTER PLOT
plot(g)                                         #GENERATE PLOT

#SCATTER PLOT-1 (ALT METHOD)
g <- ggplot(midwest, aes(x=area, y=poptotal)) + #TELL IT WHAT TO PLOT
g <- g+geom_point()                             #TELL IT TO DO SCATTER PLOT
plot(g)                                         #GENERATE PLOT

#SCATTER PLOT-2 (ADD MORE "LAYERS")
g <- ggplot(midwest, aes(x=area, y=poptotal)) + #TELL IT WHAT TO PLOT
geom_point() +                                  #DO SCATTER PLOT
# set se=FALSE to turnoff confidence bands
geom_smooth(method="lm")                        #ADD LINEAR BEST FIT LINE 
plot(g)                                         #GENERATE PLOT

#ADJUST AXIS LIMITS: (METHOD-1: DELETING)
#IMPORTANT NOTE: LIMITS EFFECT TRENDLINE (PLOTS OUTSIDE ARE EFFECTLY DELETED)
g <- ggplot(midwest, aes(x=area, y=poptotal))+  #TELL IT WHAT TO PLOT
geom_point() +                                  #DO SCATTER PLOT
geom_smooth(method="lm")+                       #ADD LINEAR BEST FIT LINE
xlim(c(0, 0.1))+                                #SET XLIMITS
ylim(c(0, 1000000))                             #SET YLIMITS
plot(g)                                         #GENERATE PLOT



#ADJUST AXIS LIMITS: (METHOD-2: ZOOMING)
#DOESN"T EFFECT POINTS OUTSIDE LIMITS
g <- ggplot(midwest, aes(x=area, y=poptotal))+     #TELL IT WHAT TO PLOT
geom_point() +                                     #DO SCATTER PLOT
geom_smooth(method="lm")+                          #ADD LINEAR BEST FIT LINE
coord_cartesian(xlim=c(0,0.1), ylim=c(0, 200000))+ #SET LIMITS
labs(title="Area Vs Population",                   #SET LABELS
subtitle="From midwest dataset",
y="Population", 
x="Area", 
caption="Midwest Demographics")
plot(g)                                            #GENERATE PLOT

#ALTERNATIVE
# g <- + ggtitle("Area Vs Population", subtitle="From midwest dataset") + xlab("Area") + ylab("Population")


#POINT SIZE AND COLOR 
g <- ggplot(midwest, aes(x=area, y=poptotal))+     #TELL IT WHAT TO PLOT
geom_point(col="steelblue", size=3) +              #DO SCATTER PLOT
geom_smooth(method="lm", col="firebrick")+         #ADD LINEAR BEST FIT LINE
coord_cartesian(xlim=c(0,0.1), ylim=c(0, 200000))+ #SET LIMITS
labs(title="Area Vs Population",                   #SET LABELS
subtitle="From midwest dataset",
y="Population", 
x="Area", 
caption="Midwest Demographics")
plot(g)                                            #GENERATE PLOT


#COLOR BASED ON ANOTHER COLUMN
# Not just color, but size, shape, stroke (thickness of boundary)
# and fill (fill color) can be used to discriminate groupings.
g <- ggplot(midwest, aes(x=area, y=poptotal))+     #TELL IT WHAT TO PLOT
geom_point(aes(col=state), size=3) +               #DO SCATTER PLOT
#LEGEND ADDED AUTOMATICALLY
# theme(legend.position="None")+                   #REMOVE LEGEND
#se=FALSE  --> TURN OFF CONFIDENCE BANDS 
geom_smooth(method="lm", col="firebrick", size=2)+ #ADD LINEAR BEST FIT LINE
coord_cartesian(xlim=c(0,0.1), ylim=c(0, 200000))+ #SET LIMITS
labs(title="Area Vs Population",                   #SET LABELS
subtitle="From midwest dataset",
y="Population", 
x="Area", 
caption="Midwest Demographics")+
scale_colour_brewer(palette = "Spectral")         #CHANGE COLOR PALETTE
plot(g)                                            #GENERATE PLOT

#SEE COLOR PALETTES
library(RColorBrewer)
head(brewer.pal.info, 10)


#AXIS FONT AND TICS
# Not just color, but size, shape, stroke (thickness of boundary)
# and fill (fill color) can be used to discriminate groupings.

# have used 2 methods for formatting
# labels: * Method 1: Using sprintf(). 
# (Have formatted it as % in below example) * Method 2: Using a custom user defined
# function. (Formatted 1000’s to 1K scale)
dx <- 0.02
FS <- 8
g <- ggplot(midwest, aes(x=area, y=poptotal))+     #TELL IT WHAT TO PLOT
geom_point(aes(col=state), size=3) +               #DO SCATTER PLOT
#LEGEND ADDED AUTOMATICALLY
# theme(legend.position="None")+                   #REMOVE LEGEND
#se=FALSE  --> TURN OFF CONFIDENCE BANDS 
geom_smooth(method="lm", col="firebrick", size=2)+ #ADD LINEAR BEST FIT LINE
coord_cartesian(xlim=c(0,0.1), ylim=c(0, 600000))+ #SET LIMITS
labs(title="Area Vs Population",                   #SET LABELS
subtitle="From midwest dataset",
y="Population", 
x="Area", 
caption="Midwest Demographics")+
scale_colour_brewer(palette = "Spectral")+         #CHANGE COLOR PALETTE
# scale_x_continuous(breaks=seq(0, 0.1, 0.02))     #XTICKS
# scale_x_continuous(breaks=seq(0, 0.1, 0.01), labels = letters[1:11])
scale_x_continuous(breaks=seq(0, 0.1, dx), labels = sprintf("%1.2f", seq(0, 0.1, dx))) +
scale_y_continuous(breaks=seq(0, 600000, 200000), labels = function(x){paste0(x/1000, 'K')})+
#FONT SIZE
# theme(text = element_text(size=FS))
theme(
axis.text.x = element_text(angle=90, hjust=1,size=FS),
axis.text.y = element_text(size=FS),
axis.title.x= element_text(size=FS), 
axis.title.y= element_text(size=FS) 
) 

plot(g)                                            #RENDER PLOT


#PRE-BUILT THEMES
?theme_bw #HELP

gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
geom_point(aes(col=state), size=3) + # Set color to vary based on state categories.
geom_smooth(method="lm", col="firebrick", size=2) + 
coord_cartesian(xlim=c(0, 0.1), ylim=c(0, 1000000)) + 
labs(title="Area Vs Population", subtitle="From midwest
dataset", y="Population", x="Area", caption="Midwest
Demographics")
gg <- gg + scale_x_continuous(breaks=seq(0, 0.1, 0.01))
# method 1: Using theme_set() theme_set(theme_classic()) # not run gg
# method 2: Adding theme Layer itself.
gg + theme_bw() + labs(subtitle="BW Theme")
gg + theme_classic() + labs(subtitle="Classic Theme")
plot(gg)                                            #RENDER PLOT


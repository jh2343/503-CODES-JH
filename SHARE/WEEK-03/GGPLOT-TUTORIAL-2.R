#MODIFIED FROM: http://r-statistics.co/Complete-Ggplot2-Tutorial-Part2-Customizing-Theme-With-R-Code.html

#MOST LOOK AND FEEL MODS CAN BE ACHIEVED USING THE THEME() FUNCTION

# Setup
options(scipen=999)
library(ggplot2)
data("midwest", package = "ggplot2")
theme_set(theme_bw())
# midwest <- read.csv("http://goo.gl/G1K41K")  # bkup data source

# Add plot components --------------------------------
gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
geom_point(aes(col=state, size=popdensity)) + 
geom_smooth(method="loess", se=F) +
xlim(c(0, 0.1)) +
ylim(c(0, 500000)) + 
labs(title="Area Vs Population", y="Population", x="Area", caption="Source: midwest")

plot(gg)  #RENDER PLOT


# THEME ACCEPTS --> 
# element_text(): Since the title, subtitle and captions are textual items, element_text() function is used to set it.
# element_line(): Likewise element_line() is use to modify line based components such as the axis lines, major and minor grid lines, etc.
# element_rect(): Modifies rectangle components such as plot and panel background.
# element_blank(): Turns off displaying the theme item.



# Base Plot
gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
geom_point(aes(col=state, size=popdensity)) + 
geom_smooth(method="loess", se=F) +
xlim(c(0, 0.1)) +
ylim(c(0, 500000)) + 
labs(title="Area Vs Population", y="Population", x="Area", caption="Source: midwest")

# Modify theme components -------------------------------------------
gg <- gg + 
theme(
#TITLE
  plot.title=element_text( 
  size=20, 
  face="bold", 
  family="American Typewriter",
  color="tomato",
  hjust=0.5,
  lineheight=1.2), 
#SUBTITLE 
  plot.subtitle=element_text(size=6, 
  family="American Typewriter",
  face="bold",
  hjust=0.5),
#CAPTION
  plot.caption=element_text(size=15),   
#X AXIS  
  axis.title.x=element_text(vjust=-0.5, size=12),  
  axis.text.x=element_text(size=10, angle = 30,vjust=.5),  # X axis text
#Y AXIS 
  axis.title.y=element_text(size=15),  # Y axis title
  axis.text.y=element_text(size=10))  # Y axis text

plot(gg)  #RENDER PLOT


#HOW TO CHANGE THE LEGEND TITLE

# Method 1: Using labs()
gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
  geom_point(aes(col=state, size=popdensity)) + 
  geom_smooth(method="loess", se=F) + xlim(c(0, 0.1)) + ylim(c(0, 500000)) + 
  labs(title="Area Vs Population", y="Population", x="Area", caption="Source: midwest")

gg <- gg + labs(color="STATE", size="Density")  # modify legend title
plot(gg)  #RENDER PLOT


Method 2: Using guides()

# Base Plot
gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
  geom_point(aes(col=state, size=popdensity)) + 
  geom_smooth(method="loess", se=F) + xlim(c(0, 0.1)) + ylim(c(0, 500000)) + 
  labs(title="Area Vs Population", y="Population", x="Area", caption="Source: midwest")

gg <- gg + guides(color=guide_legend("State"), size=guide_legend("Density"))  # modify legend title
plot(gg)

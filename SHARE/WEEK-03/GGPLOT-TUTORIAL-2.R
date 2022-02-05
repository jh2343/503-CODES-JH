#MODIFIED FROM: http://r-statistics.co/Complete-Ggplot2-Tutorial-Part2-Customizing-Theme-With-R-Code.html

# Setup
options(scipen=999)
library(ggplot2)
data("midwest", package = "ggplot2")
# midwest <- read.csv("http://goo.gl/G1K41K")  # bkup data source

#CHANGE NAME OF OUTPUT FILE
pdf(file="output-2.pdf")

#RUN ONE EXAMPLE
# examples_to_run=c("background-1")

#RUN ALL EXAMPLES
examples_to_run=c("background-1","faceting-2","faceting-1","annotation-2","annotation-1","legend-position","point-color","base-plot","modify-theme","modify-legend")


#-------------EXAMPLE-------------
if ("base-plot" %in% examples_to_run ) 
{

  #SET THEME
  theme_set(theme_bw())

  #SMOOTHING METHODS: 
  # https://ggplot2.tidyverse.org/reference/geom_smooth.html
  gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
  geom_point(aes(col=state, size=popdensity)) + 
  geom_smooth(method="loess", se=F) +
  xlim(c(0, 0.1)) +
  ylim(c(0, 500000)) + 
  labs(title="Area Vs Population", y="Population", x="Area (square miles)", caption="Source: midwest")
  plot(gg)  #RENDER PLOT

}


#-------------EXAMPLE-------------
if ("modify-theme" %in% examples_to_run ) 
{

  #SET THEME
  theme_set(theme_bw())

  # Base Plot
  gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
    geom_point(aes(col=state, size=popdensity)) + 
    geom_smooth(method="loess", se=F) + xlim(c(0, 0.1)) + ylim(c(0, 500000)) + 
    labs(title="Area Vs Population", y="Population", x="Area", caption="Source: midwest")

  # Modify theme components 
  gg <- gg + theme(
  plot.title=element_text(size=20, 
  face="bold", 
  color="tomato",
  hjust=0.5,
  lineheight=1.2),  # title  
  plot.subtitle=element_text(size=15, 
  family="American Typewriter",
  face="bold",
  hjust=0.5),  # subtitle
  plot.caption=element_text(size=15),  # caption
  axis.title.x=element_text(vjust=-4, size=15),  # X axis title
  axis.title.y=element_text(size=15),  # Y axis title
  axis.text.x=element_text(size=10, 
  angle = 30,
  vjust=.5),  # X axis text
  axis.text.y=element_text(size=10))  # Y axis text

  plot(gg)  #RENDER PLOT
}


#-------------EXAMPLE-------------
if ("modify-legend" %in% examples_to_run ) 
{
  #SET THEME
  theme_set(theme_bw())

  # Base Plot
  gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
    geom_point(aes(col=state, size=popdensity)) + 
    geom_smooth(method="loess", se=F) + xlim(c(0, 0.1)) + ylim(c(0, 500000)) + 
    labs(title="Area Vs Population", y="Population", x="Area", caption="Source: midwest")

  # gg <-gg + labs(color="State", size="Density")  # modify legend title

  gg <- gg + guides(color=guide_legend("State"), size=guide_legend("Density"))  # modify legend title

  plot(gg)  #RENDER PLOT
}


#-------------EXAMPLE-------------
if ("point-color" %in% examples_to_run ) 
{

  #SET THEME
  theme_set(theme_bw())

  # Base Plot
  gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
    geom_point(aes(col=state, size=popdensity)) + 
    geom_smooth(method="loess", se=F) + xlim(c(0, 0.1)) + ylim(c(0, 500000)) + 
    labs(title="Area Vs Population", y="Population", x="Area", caption="Source: midwest")

  gg <- gg + scale_color_manual(name="State", 
  labels = c("Illinois", 
  "Indiana", 
  "Michigan", 
  "Ohio", 
  "Wisconsin"), 
  values = c("IL"="blue", 
  "IN"="red", 
  "MI"="green", 
  "OH"="brown", 
  "WI"="orange"))

  plot(gg)  #RENDER PLOT
}




#-------------EXAMPLE-------------
if ("legend-position" %in% examples_to_run ) 
{

  #SET THEME
  theme_set(theme_bw())

  # Base Plot
  gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
    geom_point(aes(col=state, size=popdensity)) + 
    geom_smooth(method="loess", se=F) + xlim(c(0, 0.1)) + ylim(c(0, 500000)) + 
    labs(title="Area Vs Population", y="Population", x="Area", caption="Source: midwest")

  # No legend --------------------------------------------------
  gg <- gg + theme(legend.position="None") + labs(subtitle="No Legend")

  # # Legend to the left -----------------------------------------
  # gg + theme(legend.position="left") + labs(subtitle="Legend on the Left")

  # # legend at the bottom and horizontal ------------------------
  # gg + theme(legend.position="bottom", legend.box = "horizontal") + labs(subtitle="Legend at Bottom")

  # # legend at bottom-right, inside the plot --------------------
  # gg + theme(legend.title = element_text(size=12, color = "salmon", face="bold"),
  #            legend.justification=c(1,0), 
  #            legend.position=c(0.95, 0.05),  
  #            legend.background = element_blank(),
  #            legend.key = element_blank()) + 
  #   labs(subtitle="Legend: Bottom-Right Inside the Plot")

  # # legend at top-left, inside the plot -------------------------
  # gg + theme(legend.title = element_text(size=12, color = "salmon", face="bold"),
  #            legend.justification=c(0,1), 
  #            legend.position=c(0.05, 0.95),
  #            legend.background = element_blank(),
  #            legend.key = element_blank()) + 
  #   labs(subtitle="Legend: Top-Left Inside the Plot")

  plot(gg)  #RENDER PLOT
}



#-------------EXAMPLE-------------
if ("annotation-1" %in% examples_to_run ) 
{

  #SET THEME
  theme_set(theme_bw())

  # Filter required rows.
  midwest_sub <- midwest[midwest$poptotal > 300000, ]
  midwest_sub$large_county <- ifelse(midwest_sub$poptotal > 300000, midwest_sub$county, "")

  # Base Plot
  gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
    geom_point(aes(col=state, size=popdensity)) + 
    geom_smooth(method="loess", se=F) + xlim(c(0, 0.1)) + ylim(c(0, 500000)) + 
    labs(title="Area Vs Population", y="Population", x="Area", caption="Source: midwest")

  # Plot text and label ------------------------------------------------------
  # gg <-  gg + geom_text(aes(label=large_county), size=2, data=midwest_sub) + labs(subtitle="With ggplot2::geom_text") + theme(legend.position = "None")   # text

  gg <-  gg + geom_label(aes(label=large_county), size=2, data=midwest_sub, alpha=0.25) + labs(subtitle="With ggplot2::geom_label") + theme(legend.position = "None")  # label

  # # Plot text and label that REPELS eachother (using ggrepel pkg) ------------
  # library(ggrepel)
  # gg + geom_text_repel(aes(label=large_county), size=2, data=midwest_sub) + labs(subtitle="With ggrepel::geom_text_repel") + theme(legend.position = "None")   # text

  # gg + geom_label_repel(aes(label=large_county), size=2, data=midwest_sub) + labs(subtitle="With ggrepel::geom_label_repel") + theme(legend.position = "None")   # label

  plot(gg)  #RENDER PLOT

}


#-------------EXAMPLE-------------
if ("annotation-2" %in% examples_to_run ) 
{

  # Base Plot
  gg <- ggplot(midwest, aes(x=area, y=poptotal)) + 
  geom_point(aes(col=state, size=popdensity)) + 
  geom_smooth(method="loess", se=F) + xlim(c(0, 0.1)) + ylim(c(0, 500000)) + 
  labs(title="Area Vs Population", y="Population", x="Area", caption="Source: midwest")

  # Define and add annotation -------------------------------------
  library(grid)
  my_text <- "This text is at x=0.7 and y=0.8!"
  my_grob = grid.text(my_text, x=0.7,  y=0.8, gp=gpar(col="firebrick", fontsize=14, fontface="bold"))
  gg <- gg + annotation_custom(my_grob)

  plot(gg)  #RENDER PLOT

}



#-------------EXAMPLE-------------
# Faceting: Draw multiple plots within one figure
if ("faceting-1" %in% examples_to_run ) 
{

  # Base Plot
  g <- ggplot(mpg, aes(x=displ, y=hwy)) + 
        geom_point() + 
        geom_smooth(method="lm", se=FALSE) + 
        theme_bw()  # apply bw theme

  # Facet wrap with common scales
  g <- g + facet_wrap( ~ class, nrow=3) + labs(title="hwy vs displ", caption = "Source: mpg", subtitle="Ggplot2 - Faceting - Multiple plots in one figure")  # Shared scales

  # Facet wrap with free scales
  g <- g + facet_wrap( ~ class, scales = "free") + labs(title="hwy vs displ", caption = "Source: mpg", subtitle="Ggplot2 - Faceting - Multiple plots in one figure with free scales")  # Scales free

  plot(g)  #RENDER PLOT

}



#-------------EXAMPLE-------------
if ("faceting-2" %in% examples_to_run ) 
{

  # Base Plot
  g <- ggplot(mpg, aes(x=displ, y=hwy)) + 
        geom_point() + 
        labs(title="hwy vs displ", caption = "Source: mpg", subtitle="Ggplot2 - Faceting - Multiple plots in one figure") +
        geom_smooth(method="lm", se=FALSE) + 
        theme_bw()  # apply bw theme

  # Add Facet Grid
  g  <- g + facet_grid(manufacturer ~ class)  # manufacturer in rows and class in columns

  plot(g)  #RENDER PLOT

}



#-------------EXAMPLE-------------
if ("background-1" %in% examples_to_run ) 
{

  # Base Plot
  g <- ggplot(mpg, aes(x=displ, y=hwy)) + 
      geom_point() + 
      geom_smooth(method="lm", se=FALSE) + 
      theme_bw()  # apply bw theme

  # Change Plot Background elements -----------------------------------
  g <- g + theme(panel.background = element_rect(fill = 'khaki'),
          panel.grid.major = element_line(colour = "burlywood", size=1.5),
          panel.grid.minor = element_line(colour = "tomato", 
                                          size=.25, 
                                          linetype = "dashed"),
          panel.border = element_blank(),
          axis.line.x = element_line(colour = "darkorange", 
                                     size=1.5, 
                                     lineend = "butt"),
          axis.line.y = element_line(colour = "darkorange", 
                                     size=1.5)) +
    labs(title="Modified Background", 
         subtitle="How to Change Major and Minor grid, Axis Lines, No Border")

  plot(g)  #RENDER PLOT

}


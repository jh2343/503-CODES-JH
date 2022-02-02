# # Peek into data
# str(iris)
# head(iris)
# tail(iris)

# # Names, dimensions, etc.
# colnames(iris)
# dim(iris)

# # Basic stats
# colMeans(iris[-5])
# colSums(iris[-5])
# rowSums(iris[-5])
# summary(iris)

# # More suitable stats by Species
# aggregate(Sepal.Length ~ Species, data=iris, summary)
# aggregate(. ~ Species, data=iris, summary)
# aggregate(. ~ Species, data=iris, mean)
# aggregate(. ~ Species, data=iris, max)

library(datasets)
library(ggplot2)

#WILL SAVE EACH TO A PAGE IN A PDF "Rplots.pdf" IF RUN FROM COMMAND LINE
qplot(Sepal.Length, Sepal.Width, data = iris)


qplot(Petal.Length, Petal.Width, data = iris)



plen <- ggplot(data=iris, aes(x=Petal.Length, y=Petal.Width))
plen +
  geom_point() +
  coord_flip()


#A good plot should be self-contained. The measurement units are not clear. There’s no title to the plot. Let’s add these:
plen +
  geom_point() +
  ggtitle("Iris Petal Size Analysis\nData Source: Anderson (1935)") +
  labs(x="Petal Length (cm)", y="Petal Width (cm)")



#FURTHER
common_theme <- function() {
  ptcolor <- 'grey20' # plot text color
  theme(
    plot.title=element_text(size=14, lineheight=0.8, color=ptcolor, hjust=0.5),
    axis.title.x=element_text(color=ptcolor),
    axis.title.y=element_text(color=ptcolor))
}

plen +
  geom_point() +
  ggtitle("Iris Petal Size Analysis\nData Source: Anderson (1935)") +
  labs(x="Petal Length (cm)", y="Petal Width (cm)") +
  common_theme() +
  theme(plot.title=element_text(color="#2255DD"))



plen +
  geom_point(shape=iris$Species) +
  ggtitle("Iris Petal Size Analysis\nData Source: Anderson (1935)") +
  labs(x="Petal Length (cm)", y="Petal Width (cm)") +
  common_theme()



ggplot(data=iris, aes(x=Sepal.Length, y=Sepal.Width)) +
  geom_point(aes(colour=Species), shape=15, size=1.5) +
  ggtitle("Iris Sepal Size Analysis\nData Source: Anderson (1935)") +
  labs(x="Sepal Length (cm)", y="Sepal Width (cm)") +
  common_theme()


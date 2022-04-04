#----------------------------------------------------------
#ARM IN R: HELLO WORLD
#----------------------------------------------------------

# SOURCE: THIS CODE IS MODIFIED FROM JAN KIRENZ'S CODE AT  
# https://www.kirenz.com/post/2020-05-14-r-association-rule-mining/

#TO RUN FROM MACOS CMND LINE RQUIRED  brew install pandoc

#------------------------
# GET REQUIRED LIBRARIES 
#------------------------
library(arules)
library(arulesViz)
library(plotly)

# #-------------
# #OPTION-2: READ BASKET FORMAT FILE
# #-------------
#SEE: https://www.rdocumentation.org/packages/arules/versions/1.6-8/topics/read.transactions
trans <- read.transactions(
"transactions.txt", 
format = "basket",      #basket or single
header = FALSE,         #file contains header or not
sep = ",", 
rm.duplicates = FALSE,  #rm duplicates from transactions
cols = NULL,            
)


#BASIC INSPECTION OF TRANS OBJECT
# print(c("ITEM LIST:",   itemLabels(trans)))
# print("DIMENSION:");    dim(trans); #str(trans)
# print("SUMMARY:");      summary(trans)
# print("INSPECT:");      inspect(trans)
# print("MATRIX FORM:");  print(as(trans, "matrix"))
image(trans)
itemFrequencyPlot(trans, topN=10,  cex.names=1)
#------------------------
#TRAIN MODEL
#------------------------


#TRAIN: REMOVE EMPTY LHS RULES: Min Support 0.3, confidence as 0.5.
rules <- apriori(
trans, 
parameter = list(supp=0.001, conf=0.01, 
maxlen=10, 
minlen=2,
target= "rules"))
print("RULES:"); summary(rules); #inspect(rules)

#------------------------
#VISUALIZE RESULTS
#------------------------

plot(rules)
# subrules <- head(rules, n = 500, by = "support")
# subrules <- head(rules, n = 100, by = "confidence")
subrules <- head(rules, n = 500, by = "lift")

p <- plot(subrules, engine = "plotly")
htmlwidgets::saveWidget(as_widget(p), "plot-1.html")

p <- plot(subrules, max=2000, method = "graph",  engine = "htmlwidget")
htmlwidgets::saveWidget(as_widget(p), "network.html")
print("DONE")



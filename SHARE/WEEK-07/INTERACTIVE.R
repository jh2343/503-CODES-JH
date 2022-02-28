






#PLOTLY 
example='PLOTLY:SCATTERPLOT'
example='PLOTLY:LINEPLOT'

example='SHINY:BASIC'
example='SHINY:NORMAL_DISTRIBUTION'


if (example=="SHINY:BASIC") 
{

# SOURCE https://riptutorial.com/shiny/example/22770/simple-app

library(shiny)

# DEFINE UI FOR APPLICATION PRINT "HELLO WORLD" 
ui <- shinyUI(

  # Create bootstrap page 
  fluidPage(
    
    # Paragraph "Hello world"
    p("Hello world"),

    # Create button to print "Hello world" from server
    actionButton(inputId = "Print_Hello", label = "Print_Hello World"),

    # Create position for server side text
    textOutput("Server_Hello")
    
  )
)

# Define server logic required to print "Hello World" 
# when button is clicked
server <- shinyServer(function(input, output) {
  
  # Create action when actionButton is clicked
  observeEvent(input$Print_Hello,{

    # Change text of Server_Hello
    output$Server_Hello = renderText("Hello world from server side")
  })
})

#START SHINY APP
shinyApp(ui, server)

}




if (example=="SHINY:NORMAL_DISTRIBUTION") 
{
#SOURCE: https://shiny.rstudio.com/gallery/example-01-hello.html

library(shiny)

# Define UI for application that plots random distributions 
ui <- shinyUI(fluidPage(
  
  # Application title
  titlePanel("Hello Shiny!"),
  
  # Sidebar with a slider input for number of observations
  sidebarLayout(
    sidebarPanel(
      sliderInput("obs", 
                  "Number of observations:", 
                  min = 1, 
                  max = 4000, 
                  value = 500)
    ),
    
    # Show a plot of the generated distribution
    mainPanel(
      plotOutput("distPlot")
    )
  )
))

# Define server logic required to generate and plot a random distribution
server <- shinyServer(function(input, output) {
   
  # Expression that generates a plot of the distribution. The expression
  # is wrapped in a call to renderPlot to indicate that:
  #
  #  1) It is "reactive" and therefore should be automatically 
  #     re-executed when inputs change
  #  2) Its output type is a plot 
  #
  output$distPlot <- renderPlot({
        
    # generate an rnorm distribution and plot it
    dist <- rnorm(input$obs)
    hist(dist)
  })
  
})
     
#START SHINY APP
shinyApp(ui, server)

}

quit()


#-------------------------------
if (example=="PLOTLY:SCATTERPLOT") 
{

library(plotly)
library(palmerpenguins)
df <- penguins

print(df)

fig <- plot_ly(penguins,
x= ~bill_length_mm,
y= ~body_mass_g,
color = ~species,
type='scatter', 
mode='markers',
hovertemplate = paste("Species:",penguins$species,'<br>Island: ',penguins$island,"<br>Sex:",penguins$sex)
) %>% 
plotly::layout(
xaxis = list(title='Bill length (mm)'),
yaxis = list(title='Body mass (g)'),
title = 'Palmer Penguins'
)
htmlwidgets::saveWidget(as_widget(fig), "PLOTLY.html")

}
#-------------------------------





#-------------------------------
if (example=="PLOTLY:LINEPLOT") 
{

library(plotly)
library(gapminder)
df <- filter(gapminder, continent=='Asia')
print(df)
fig <- plot_ly(
df, 
x = ~year, 
y = ~lifeExp,
color = ~country, 
type='scatter', mode='lines',
hovertemplate=paste('<b>',df$country,'</b><br>Year=%{x}<br>Life Expectancy=%{y:.2f} yrs')) %>% 
plotly::layout(xaxis=list(title='Year'),
yaxis=list(title='Life Expectancy'),
showlegend=FALSE)

htmlwidgets::saveWidget(as_widget(fig), "PLOTLY.html")


}

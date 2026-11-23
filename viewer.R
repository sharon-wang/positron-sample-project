# Run this file to show web content in the Viewer pane.
library(htmltools)

page <- tags$div(
  tags$h1("Positron sample project"),
  tags$p("This page is shown in the Viewer pane."),
  tags$button("A button", onclick = "alert('Clicked')")
)
html_print(page)

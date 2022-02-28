
#EXPORT TO HTML WITH CODE
jupyter nbconvert example.ipynb  --to html --output output-1.html

#EXPORT TO PDF WITHOUT CODE
jupyter nbconvert example.ipynb  --to html --TemplateExporter.exclude_input=True --output output-2.html



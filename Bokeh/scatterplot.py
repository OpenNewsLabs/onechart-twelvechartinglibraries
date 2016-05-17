#import libraries
import pandas as pd
from bokeh.plotting import figure, show, output_file

#read data
data = pd.read_csv("data.csv")

#plot chart
p = figure(x_axis_type="log")
p.scatter(data['income'], data['health'], radius=data['population']/100000,
          fill_color='black', fill_alpha=0.6,line_color=None)

#write as html file and open in browser
output_file("scatterplot.html")
show(p)

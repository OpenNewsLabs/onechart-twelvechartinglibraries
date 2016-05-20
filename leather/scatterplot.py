import leather
import math
import csv
from operator import itemgetter

chart = leather.Chart('Income vs. health')

with open('data.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    data = list(reader)
    
    def size_dot_by_area(x, y, i):
        return math.sqrt(int(data[i]['population'])) / 1000

    dots = leather.Dots('rgba(0,0,0,0.5)', radius=size_dot_by_area)

    series = leather.Series(
        data,
        dots,
        x=lambda row, i: math.log(float(row['income'])),
        y=lambda row, i: float(row['health']))

    chart.add_series(series)

chart.set_x_axis(leather.Axis(name='Log GDP per capita'))
chart.set_y_axis(leather.Axis(name='Life expectancy in years'))
chart.to_svg('chart.svg')

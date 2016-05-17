setwd("Desktop")

#read csv
d = read.csv("data.csv", header=TRUE)

#import ggplot2 library
library(ggplot2)

#plot chart
ggplot(d) +
  geom_point(aes(x=log(income),y=health,size=population)) +
  expand_limits(x=0)
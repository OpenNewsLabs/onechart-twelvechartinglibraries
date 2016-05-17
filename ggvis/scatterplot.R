#import library
library(ggvis)
library(dplyr)

#set working directory
setwd("Desktop")

#read csv
d = read.csv("data.csv", header=TRUE)

#plot chart
d %>% 
  ggvis(~income, ~health) %>% 
  layer_points(size= ~population,opacity:=0.6) %>%
  scale_numeric("x",trans = "log",expand=0)

#set working directory
setwd("Desktop")

#read csv
d = read.csv("data.csv", header=TRUE)

#plot chart, set range for x-axis between 0 and 11
symbols(log(d$income),d$health,circles=d$population,xlim = c(0,11))
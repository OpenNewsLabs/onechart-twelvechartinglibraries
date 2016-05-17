#import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#read data
data = pd.read_csv("data.csv")

#plot chart
plt.scatter(np.log(data['income']), data['health'], s=data['population']/1000000, c='black')
plt.xlim(xmin=0) #set origin for x axis to zero
plt.show()

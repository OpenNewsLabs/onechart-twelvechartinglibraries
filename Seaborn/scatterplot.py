#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#read data
data = pd.read_csv("data.csv")

#plot chart
g = sns.regplot('income', 'health', data=data, color='k',fit_reg=False)
g.set_xscale('log')
plt.show()

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

pd.set_option('display.max_columns', None) #displays all columns of dataframe

m5 = pd.read_csv('m5_dr2.csv') #dataframe for messier 5
print(m5)

fig = plt.figure(figsize = [10,10])
plt.scatter(m5['ra'], m5['dec'])
plt.plot(229.6375, 2.0811, 'ro') # center x and y and color

plt.xlabel('ra (deg)')
plt.ylabel('dec (deg)')
plt.show()
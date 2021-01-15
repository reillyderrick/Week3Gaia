import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

closest = pd.read_csv('gaia_closest_100.csv')

plt.figure(figsize = [10, 10])
plt.hist(closest['ra'], color = 'm')

plt.title("Right ascension of closest 100 stars (deg) ")
plt.xlabel("Right ascension (deg)")
plt.ylabel("Star count")

plt.show()

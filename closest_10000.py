import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from matplotlib import cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap

pd.set_option('display.max_columns', None)

closest = pd.read_csv('gaia_closest_10000.csv')

plt.scatter(closest['bp_rp'], closest['abs_photo_mag'], s = .1, c = closest['dist'])

closest = closest.sort_values(by = 'dist')
closest = closest.dropna()

#print(closest['bp_rp'][0:10])
#print(closest['mag'][0:10])

plt.scatter(closest['bp_rp'][0:10], closest['abs_photo_mag'][0:10], color = 'r', s = 10, marker='*')

plt.title("Color-magnitude diagram of the 10000 closest stars")
plt.xlabel('BP-RP color')
plt.ylabel('Absolute g-band magnitude')

plt.ylim(30, -5)

plt.savefig('closest_1000.png')
plt.show()
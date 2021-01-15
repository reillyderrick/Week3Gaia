#distribution of proper motions of m92
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

m92 = pd.read_csv('m92_dr2.csv')

fig, (ax1, ax2) = plt.subplots(1, 2, figsize = (10,5), sharey = True) #two subplots
ax1.hist(m92['pmra'], label = 'PM_RA', color='m')
ax2.hist(m92['pmdec'], label = 'PM_DEC', color='b') #histograms showing distribution of different pms

ax1.set_ylabel('count')
ax1.set_xlabel('proper motion (mas/yr)')
ax2.set_xlabel('proper motion (mas/yr)')

ax1.legend()
ax2.legend()
plt.show()
plt.savefig('gaia_m92.png')

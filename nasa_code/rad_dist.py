import pandas as pd 
import matplotlib.pyplot as plt 
import numpy as np

kepler_data = pd.read_csv('confirmed_kepler_transiting.csv', comment = '#')
print(kepler_data.shape)

log_bins = np.logspace(np.log10(0.3), np.log(20), 50) #??? creating bins in log space

plt.hist(kepler_data['pl_rade'], bins = log_bins) #histogram

plt.xscale('log')

plt.xlabel('Radius') #labels
plt.ylabel('Count of planets')

plt.title('Distribution of planets by Earth radius')
plt.xlim(0, 100)

plt.savefig('rad_dist.png')
plt.show()
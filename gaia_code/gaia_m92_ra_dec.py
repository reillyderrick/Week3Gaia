#ra and dec of messier 92 gaia dr2
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

m92 = pd.read_csv('m92_dr2.csv')

plt.figure(figsize = [10,10])
plt.scatter(m92['ra'], m92['dec'])
plt.plot(259.2833, 43.1358, 'ro') #center coordinates from jupyter

plt.title('Messier 92 plotted in ra/dec space (degrees)')
plt.xlabel('ra (deg)')
plt.ylabel('dec (deg)')

plt.savefig('gaia_m92_ra_dec.png')
plt.show()

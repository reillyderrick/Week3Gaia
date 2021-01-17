#Why did you plot what you plotted? Do you notice any interesting features?:
#I plotted this to see if the number of stars in a system has any effect on the mass of the planets in the system.
#Although it appears that a wide majority of stars in single as well as multiple star systems have planets with a mass between
#0 and 20, it does not seem that 1 star systems effect planets' mass differently than 2 star systems, the masses seem to be more random

import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd 

systems = pd.read_csv('confirmed_kepler_transiting.csv', comment = '#')

stars1 = systems.loc[systems['sy_snum'] == 1]['pl_bmasse'] #planet masses of systems with 1 star
stars2 = systems.loc[systems['sy_snum'] == 2]['pl_bmasse'] #planet masses of systems with 2 stars
#stars3 = systems.loc[systems['sy_snum'] == 3]['pl_bmasse'] #planet masses of systems with 3 stars

fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, sharex = True)

#make three subplots by snum = 1, 2, 3 with hist of st_mass

ax1.hist(stars1, color = 'b', label = '1 star systems', bins = np.arange(0, 100, 1)) #change bins?
ax2.hist(stars2, color = 'r', label = '2 star systems', bins = np.arange(0, 100, 1))
#ax3.hist(stars3, color = 'g', label = '3 star systems', bins = np.arange(0, 5000, 100))

ax1.set_title('Distribution of planetary mass across systems with 1 star')
ax1.set_ylabel('Number of systems')
ax1.legend()

ax2.set_ylabel('Number of systems')
ax2.legend()

ax2.set_xlabel('Planet mass [Earth Mass]')
plt.xlim(-10, 100)

#ax3.set_ylabel('Number of systems')
#ax3.legend()

plt.savefig('num_smass.png')

plt.show()
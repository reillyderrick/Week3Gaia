import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 

planets = pd.read_csv('confirmed_kepler_transiting.csv', comment = '#') #dataframe

planets = planets[planets['pl_orbper'].notna()]

plt.scatter(planets['pl_orbper'], planets['pl_rade'], alpha = 0.5, color = 'm') #scatterplot

plt.title("Orbital period vs radius (in Earth units) of transiting planets") #title

plt.xlabel("Orbital period (days)") #labels
plt.ylabel("Radius (in Earth units)")

plt.xlim(0, 1000)

plt.savefig('orbper_rad.png')
plt.show()
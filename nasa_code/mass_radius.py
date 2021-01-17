import os
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt 

pd.set_option('display.max_columns', None)

example_data = pd.read_csv('confirmed_example.csv', comment='#')

plt.plot(example_data['pl_bmassj'], example_data['pl_radj'], '.m', alpha = 0.3) #plot (alpha makes transparent)

plt.xlabel('Mass [M$_J$]') #labels
plt.ylabel('Radius [R$_J$]')

plt.text(10**(-3), 1, f'n={len(example_data)}') #adds text to tell how many stars

plt.xscale('log') #setting x and y to be on a scale of log
plt.yscale('log')

plt.savefig('mass_radius.png')

plt.show()


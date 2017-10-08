import numpy as np
import matplotlib.pyplot as plt

t = np.arange(0.0,2.0,0.01)
s = 1 + np.sin(2* np.pi * t)

fig,ax = plt.subplots()
ax.plot(t,s)

ax.set(xlabel = 'time (s) ' , ylabel = 'voltage (mv)',
title = "My First Graph Made In Python")
ax.grid()
plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random
random.seed()
x = []
for i in range(5):
    x.append(random.uniform(0,1))

y = []
for i in range(5):
    y.append(random.uniform(0,1))

z = []
for i in range(5):
    z.append(random.uniform(0,1))

fig = plt.figure()
ax = fig.add_subplot(111, projection= '3d')

ax.scatter(x,y)
plt.show()

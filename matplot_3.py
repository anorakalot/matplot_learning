import matplotlib.pyplot as plt
import random
random.seed()
x = []
y = []
for i in range(5):
    x.append(random.randint(0,5))
for i in range(5):
    y.append(random.randint(0,5))


plt.scatter(x,y,c='orange')
plt.show()

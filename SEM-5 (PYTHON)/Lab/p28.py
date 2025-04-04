import matplotlib.pyplot as plt
import random
x=['a','b','c','d','e']
y=[10,12,8,15,9]
title="Rating"
colors=[tuple(random.random() for _ in range(3)) for _ in range(len(x))]
plt.bar(x,y, color=colors)
plt.xlabel('x')
plt.ylabel('Frequency')
plt.title(title)
plt.show()

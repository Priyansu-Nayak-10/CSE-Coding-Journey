from random import randrange as rr
import matplotlib.pyplot as plt
n_rolls=6000
rolls=[rr(1,7) for _ in range(n_rolls)]
unique_l=[ ]
for v in rolls:
    if v not in unique_l:
        unique_l.append(v)

n_l=sorted(unique_l) #x-values
l_f=[rolls.count(i) for i in n_l] #y-values
title='Rolling a six sided die {n_rolls} times'
colors=['red', 'green', 'blue', 'purple','black', 'grey']
plt.bar(n_l,l_f, color=colors)
plt.xlabel('Value')
plt.ylabel('frequency')
plt.title(title)
plt.show()

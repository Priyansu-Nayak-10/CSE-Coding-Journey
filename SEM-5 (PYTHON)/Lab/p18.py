"""
import random
l=[]
for x in range(10):
    outcome=random.randrange(2)
    l.append("H" if outcome==0 else "T")
print(l) """


""""
import random
p=[]
for x in range(20):
    outcome=random.randrange(1,7)
    p.append(outcome)
print(p)
"""

import random
p=[]
random.seed(10)
for x in range(20):
    outcome=random.randrange(1,7)
    p.append(outcome)
print(p)

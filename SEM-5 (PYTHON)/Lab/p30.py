from random import randrange as rr
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
n_rolls=6000
rolls=[rr(1,7) for _ in range(n_rolls)]
values,frequencies=np.unique(rolls,return_counts=True)
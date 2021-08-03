import numpy as np
import random

randArray = np.random.randint(0,9,(10,10)) + 1

for i in range(0, 10, 2):
  randArray[i] = 0

randArray

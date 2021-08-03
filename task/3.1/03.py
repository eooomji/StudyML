## 더 나은 방법 생각해보기
import numpy as np
import random

randArray = np.random.randint(0,9,(10,10)) + 1

for i in range(0, 10, 2):
  randArray[i] = 0

for i in range(1, 10, 2):
  randArray[i][1::2] = 0

randArray

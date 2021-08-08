import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

HorsePower = pd.Series([130, 250, 190, 300, 210, 220, 170])
Weight = pd.Series([1900, 2600, 2200, 2900, 2400, 2300, 2100])
Efficiency = pd.Series([16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2])

PCC = pd.DataFrame({'horsePower' : HorsePower, 'weight' : Weight ,'efficiency' : Efficiency})

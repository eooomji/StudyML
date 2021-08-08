import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# from sklearn import linear_model
# from statsmodels.formula.api import ols
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# setting
Idx = pd.Series(['A', 'B', 'C', 'D', 'E', 'F', 'G'])
HorsePower = pd.Series([130, 250, 190, 300, 210, 220, 170])
Efficiency = pd.Series([16.3, 10.2, 11.1, 7.1, 12.1, 13.2, 14.2])

P_carCompany = pd.DataFrame({'idx' : Idx, 'horse power' : HorsePower, 'efficiency' : Efficiency})
P_carCompany1 = P_carCompany.transpose()
P_carCompany2 = P_carCompany1.rename(columns=P_carCompany1.iloc[0])
P_carCompany3 = P_carCompany2.drop(P_carCompany2.index[0])

P_carCompany3

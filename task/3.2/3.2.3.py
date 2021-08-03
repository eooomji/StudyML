######################## 미완성
#3.2.3 마력x연비 값이 가장 큰 차종을 찾아 출력
import pandas as pd

P_carCompany = pd.DataFrame ({'name' :  ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
                              'horse power' : ['130', '250', '190', '300', '210', '220', '170'],
                              'weight' : ['1.9', '2.6', '2.2', '2.9', '2.4', '2.3', '2.2'],
                              'efficiency' : ['16.3', '10.2', '11.1', '7.1', '12.1', '13.2', '14.2']})

P_horsePower = []
P_efficiency = []

for i in range(7):
  Ph = float(P_carCompany.loc[i]['horse power'])
  P_horsePower.append(Ph)
  Pe = float(P_carCompany.loc[i]['efficiency'])
  P_efficiency.append(Pe)

# print(P_horsePower)
# print(P_efficiency)

he_list = []

for i in range(7):
  he = P_horsePower[i] * P_efficiency[i]
  he_list.append(he)

he_list

P_carCompany['he 곱한 값'] = he_list

# P_carCompany

heMax = P_carCompany['he 곱한 값'].max()


heMaxCol = P_carCompany.loc[P_carCompany['he 곱한 값'] == heMax]
# heMaxCol = P_carCompany.loc[P_carCompany['he 곱한 값'] == heMax]['name']
heMaxCol['name']

print('마력과 연비를 곱한 값중 최대값을 가진 차종 : ', heMaxCol['name'])

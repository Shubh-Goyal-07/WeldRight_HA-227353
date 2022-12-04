import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

operation_num = int(input('Enter the operation number: '))

file = (f'{operation_num}.xlsx')
df = pd.read_excel(file)

param_dict = {'current': 0, 'humidity': 1, 'temperature': 2, 'flow': 3, 'job temp': 4, 'voltage': 5, 'defect': 6}
inp = input('Enter the parameter: ')

param_arr = df[param_dict[inp]].tolist()
defect_arr = df[param_dict['defect']].tolist()
for i in range(len(defect_arr)):
    if defect_arr[i] == 'No Defect':
        defect_arr[i] = 0
    else:
        defect_arr[i] = 1
d = {}

for i in range(len(param_arr)):
    d[param_arr[i]] = 0
    
for i in range(len(defect_arr)):
    if(defect_arr[i] == 0):
        d[param_arr[i]] += 1

Keys = list(d.keys())
Values = list(d.values())

plt.ylabel('number of defects')
plt.xlabel(f'{inp}')
plt.plot(Keys, Values, '.')
plt.show()

d = {k: v for k, v in sorted(d.items(), key=lambda item: item[1])}

lst = []

for key in d.keys():
    if d[key] == 0:
        lst.append(key)
    else:
        break
    
print("The point of zero defects are :", lst)
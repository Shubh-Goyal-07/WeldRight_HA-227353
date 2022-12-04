import pandas as pd
import numpy as np

data = pd.read_excel("/home/shubh07/Desktop/WeldRight/WeldRight Dataset.xlsx")

data = pd.DataFrame.to_numpy(data)
data = data[1:, 3:13]
data = np.delete(data, 1, 1)
data = np.delete(data, 1, 1)

for i in data:
    if (i[0] == '-'):
        i[0] = 1
    elif (i[0] == '180-'):
        i[0] = 180
    else:
        i[0] = abs(int(i[0]))
    
dict = {}
for i in data:
    if i[7][0:9] == "No Defect":
        i[7] = "No Defect"
        
        
    if i[0] in dict:
        dict[i[0]].append(i[1:])
    else:
        dict[i[0]] = []
        dict[i[0]].append(i[1:])

for key in dict:
    dict[key] = np.array(dict[key])
    
print(dict)

for key in dict:
    df = pd.DataFrame (dict[key])
    filepath = str(key) + '.xlsx'
    df.to_excel(filepath, index=False)
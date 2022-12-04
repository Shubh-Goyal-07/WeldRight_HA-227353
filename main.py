import pandas as pd
import numpy as np
import predictor
from sklearn.metrics import f1_score


path = input("Enter the file path:")

if path[-3::-1] == "csv":
    data = pd.read_csv(path)
else:
    data = pd.read_excel(path)
    
data = pd.DataFrame.to_numpy(data)
data = data[1:, 3:13]
data = np.delete(data, 1, 1)
data = np.delete(data, 1, 1)

predictions = []
for i in data:
    defect = predictor.predict(i)
    predictions.append(defect)

predictions = np.array(predictions)
print("Predictions :", predictions)

y_pred = data[:, -1]

print("f1_score :", f1_score(predictions,y_pred,average='micro'))
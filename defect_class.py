from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import numpy as np
import pandas as pd
import pickle
from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score
from sklearn.metrics import confusion_matrix, zero_one_loss
from sklearn.metrics import classification_report

for op_no in [1, 30, 40, 130, 180, 240]:
    data = pd.read_excel("/home/shubh07/Desktop/WeldRight/"+str(op_no)+".xlsx")
    
    data = pd.DataFrame.to_numpy(data)
    data = data[:, :]
    
    class_data = []
    for i in data:
        if i[-1] != "No Defect":
            if i[-1] == "Porosity":
                i[-1] = 1
                class_data.append(i)
            else:
                i[-1] = 2
                class_data.append(i)
        else:
            continue
    
    class_data = np.array(class_data)
    
    X = class_data[:, :6]
    y = class_data[:, 6]        
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    X_train = X_train.astype(np.float32)
    y_train = y_train.astype(np.int32)
    X_test = X_test.astype(np.float32)
    y_test = y_test.astype(np.int32)

    clf = RandomForestClassifier(max_depth=4, random_state=2)
    clf.fit(X_train, y_train)

    pkl_filename = "logreg_models/model_" + str(op_no) + ".pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump (clf, file)
    # Load from file
    pkl_filename = "logreg_models/model_" + str(180) + ".pkl"
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)
        
    y_pred = clf.predict(X_test)
    
    print(y_pred)

    sum=0
    for i in range(len(y_pred)):
        if y_pred[i] == y_test[i]:
            sum+=1
            
    print('accuracy:', sum/len(y_pred)*100)

    results_nm = confusion_matrix(y_test,y_pred)
    print(results_nm)
    print(classification_report(y_test,y_pred))
    print(accuracy_score(y_test,y_pred))
    print("Precision Score : ",precision_score(y_test,y_pred, 
                                            pos_label='positive',
                                            average='micro'))
    print("Recall Score : ",recall_score(y_test,y_pred, 
                                            pos_label='positive',
                                            average='micro'))
    print(f1_score(y_test,y_pred,average='micro'))



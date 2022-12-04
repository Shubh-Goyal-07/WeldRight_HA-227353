# from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np
from sklearn.mixture import GaussianMixture
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

    X = data[:, :6]
    print(X)

    y = data[:, 6]


    for i in range (0, len(y)):
        if y[i] == "No Defect":
            continue
        else:
            y[i] = 'Defect'

    print(y)

    lst = []
    for i in y:
        if i not in lst:
            lst.append(i)
        
    print(lst)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    gnb = GaussianNB()
    gnb.fit(X_train, y_train)

    lst1 = []
    for i in y_train:
        if i not in lst1:
            lst1.append(i)
    print(lst1)

    lst2 = []
    for i in y_test:
        if i not in lst2:
            lst2.append(i)
    print(lst2)

    # # # saved_model = pickle.dumps(gnb)

    # # # Load the pickled model
    # # gnb_from_pickle = pickle.loads(saved_model)

    # # # Use the loaded pickled model to make predictions
    # # y_pred = gnb_from_pickle.predict(X_test)

    # # print("Number of mislabeled points out of a total %d points : %d"%(X_test.shape[0], (y_test != y_pred).sum()))

    # # gm = GaussianMixture(n_components=2, random_state=0).fit(X_train, y_train)
    # # y_pred = gm.predict(X_test)
    # # print(y_pred)

    # # num = 0
    # # for i in y_pred:
    # #     if i == 1:
    # #         num+=1
    # # print(num)

    # # print("Number of mislabeled points out of a total %d points : %d"%(X_test.shape[0], (y_test != y_pred).sum()))

    # # Save the trained model as a pickle string.


    pkl_filename = "mulgauss_models/model_" + str(op_no) + ".pkl"
    with open(pkl_filename, 'wb') as file:
        pickle.dump (gnb, file)
    # Load from file
    with open(pkl_filename, 'rb') as file:
        pickle_model = pickle.load(file)
    # Calculate the accuracy score and predict target values
    score = pickle_model.score(X_test, y_test)
    print("Test score: {0:.2f}%".format(100 * score))
    y_pred = pickle_model.predict(X_test)
    print(y_pred)

    num = 0
    for i in y_pred:
        if i!='No Defect':
            num+=1

    num2 = 0
    for i in y_test:
        if i!='No Defect':
            num2+=1

    lst3 = []
    for i in y_pred:
        if i not in lst3:
            lst3.append(i)
    print(lst3)

    print(num2, num)
    print("Number of mislabeled points out of a total %d points : %d"%(X_test.shape[0], (y_test != y_pred).sum()))



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
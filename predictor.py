# import pandas as pd
import numpy as np
import pickle 

def isDefect(op_no, parameters):
    pkl_filename = "mulgauss_models/model_" + str(op_no) + ".pkl"
    
    with open(pkl_filename, 'rb') as file:
        model = pickle.load(file)

    # Calculate the accuracy score and predict target values
    y_pred = model.predict(parameters)
    
    if y_pred == "Defect":
        return True
    else:
        return False

def defecttype(op_no, parameters):
    pkl_filename = "logreg_models/model_" + str(op_no) + ".pkl"
    
    with open(pkl_filename, 'rb') as file:
        model = pickle.load(file)

    # Calculate the accuracy score and predict target values
    y_pred = model.predict(parameters)
    
    if y_pred == 1:
        return "Porosity"
    else:
        return "Tungsten Inclusion"

def predict(data):
    op_no = data[0]
    para = data[1:7]
    if isDefect(op_no, np.array([para])):
        return defecttype(op_no, np.array([para]))
    else:
        return "No Defect"
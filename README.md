# WeldRight
A ML model to predict welding defects.

## TEAM DESCRIPTION
Team Strength - 3:

Shubh Goyal: Sophomore year (B. Tech Computer Science and Engineering)
goyal.22@iitj.ac.in

Sukriti Goyal: Sophomore year (B. Tech Computer Science and Engineering)
goyal.23@iitj.ac.in

Tanish Pagaria: Sophomore year (B. Tech Artificial Intelligence and Data Science)
pagaria.2@iitj.ac.in

IIT Jodhpur Undergraduates

The Machine Learning model, used here, predicts the defects using the multiple parameters affecting the welding process and records the dataset from past activities. These parameters include ambient temperature, weld job temperature, humidity, voltage current, welding travel speed, shielding gas flow, and metal composition. It is a better approach as compared to the present methods of defect detection that are used after the completion of the manufacturing process.


## A DETAILED DESCRIPTION OF THE PROPOSED MACHINE LEARNING MODEL 

The Machine Learning model that we have used here predicts whether a particular combination of parameters lead to a defective weld or a non-defective weld.

Here is a detailed description of all the files included in the submitted “Weldright” folder.

### main.py

The file named main.py basically takes input of the parameters and returns the final array (list) of the predicted values (“No defect” or the type of defect), for the given set of parameters, as the output.
To give the input, the user has to simply give the file path as the input to the python program, after which the program will access the values from the csv/excel file on its own and return the predicted values as output along with the accuracy (provided that the true output values are provided).



### predictor.py

This file is acting as a bridge between the file that stores the model (i.e., the Gaussian Naive Bayes Machine Learning model) and the main.py file that took the input. This file imports the model and processes the data and returns a predicted value to the main.py which further returns the same predicted value to the user.


### model.py

This is the file that stores the code for the Gaussian Naive Bayes Machine Learning model, the model that we used for the prediction purpose. This file in itself takes no input and does not give an output to the user directly. This file is imported into predictor.py (which has access to the input data from main.py). The model uses a Gaussian Naive Bayes approach to predict whether the given welding parameters lead to a defect or not. It should be noted that the output here is binary, i.e., “Defect” or “No Defect”. For further classification of the defects, we pass on the data labeled as “Defect” to the file named defect_class.py.


### defect_class.py

This file is a Random Forest Classifier which classifies the data labeled as “Defect” into the various types of defects (for example: tungsten inclusion, porosity, etc.). This file too does not take an input or generate an output by itself but is imported into predictor.py (which generates an output for the model.py file). The code here makes use of the data classified as “Defect” by the Gaussian Naive Bayes algorithm in the model.py file.


### advancedanalytics.py

This file stores the code for plotting the graphs of the number of defects corresponding to a welding parameter versus the range of values for that parameter. The graphs plotted are useful in observing the variation in the number of defects with the change in a particular parameter and thus, play an important role in analyzing the impact of that welding parameter in the manufacturing process.


### oporder.py

This file contains the code that we used for the cleaning of the dataset that was provided as it contained some errors and unwanted redundancies. However, it should be noted that this code will not be accessed for any new test data that is fed into the model as we have written all the codes assuming the new test data to be clean and free of errors.

### Other xlsx files

We divided the original dataset on the basis of separate operation numbers and the name of each file signifies the particular operation number. 
Here is an explanation for why we went ahead with this division: As observed in the data, there are six different kinds of welding operations which are performed here. For each operation, the ambient welding conditions, i.e., the best-suited values of current, temperature, etc. (based on the provided data), would be different. Therefore, it would be a better option to apply the machine learning model separately to all the operations.


## STATISTICAL ANALYSIS OF THE MODEL BASED ON THE GIVEN DATASET

We divided the given dataset into 2 parts, i.e., the training data and the test data. After using the training data to train the model, we used the test data to check the accuracy using the F1 score of the model. 
The F1 score of the Gaussian Naive Bayes model turned out to be a staggering 0.983.
However, after the application of the Random Forest Classifier to determine the type of defect, the F1 score dropped to 0.94.
Thus, we can infer that the model predicts that a given set of parameters will lead to a defect or no defect with an accuracy of 98.3%.


## ROI ANALYSIS

Currently the detection methods for defects are put to use once the weld is completed. This incurs a very heavy loss to the company as the defective weld is of no use after being discarded, thus leading to a wastage of a whole lot of resources. Instead the model that we have presented herewith predicts the defect beforehand and thus prevents the company from having to discard a defective piece after once being manufactured. This saves a significant amount of the company’s money as they can now invest only in non-defective production. Thus, we can simply evaluate the final value of the proposed solution equivalent to all the money that is saved, thanks to the predictions done by the model. The point to be noted here is that the initial cost of the proposed solution is just the computational as well as the logistic (i.e., servers etc.) cost of running the proposed Machine Learning model effectively. 
Thus clearly, the initial cost is not even remotely comparable to the vast savings that add up to be the final value of this investment. 
Hence, we can safely say that the ROI on this investment is humongous and in fact highly profitable.


## TCO ANALYSIS

As mentioned above, in the ROI analysis, the initial investment is made in the computational and logistic side. TCO (Total Cost of Ownership) aims to analyze the actual cost of purchasing a product or service from a given supplier, beyond the basic purchase price. Hence, we can say that the TCO in this scenario is the cost spent in the deployment and the maintenance of the machine learning model. Additional costs may involve a mechanism by which this model can be accessed and included in the manufacturing and the business process.



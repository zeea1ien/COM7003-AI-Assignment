import numpy as np 
import pandas as pd
import pickle as p # p stands for pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

def init_knn_model(dt):
    #split the data into training and test sets 
    # starting with splitting it into features (x) and target (Y)

    #convert hours studied to numerical values 

    for col in dt.columns:
        if dt[col].dtype == 'object':
            dt[col] = LabelEncoder().fit_transform(dt[col])


    x = dt.drop(columns='Exam_Score', axis=1) 
    y = dt["Exam_Score"]

    # split the data into training and test sers 
    x_train,x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42) #30% of the data will be used for testing and 70% will be used for training
    x_train = np.array(list(x_train))
    y_train = np.array(list(y_train))
    x_test = np.array(list(x_test))
    y_test = np.array(list(y_test))
    #next im going to scale the features using standardscaler
    scaler = StandardScaler()
    x_train = scaler.fit_transform(x_train)
    x_test = scaler.transform(x_test)

#now the models ready to train for this use a fixed model of 3 for k

    knn = KNeighborsRegressor(n_neighbors=3)
    knn.fit(x_train, y_train)

    #Make predictions 

    y_pred = knn.predict(x_test)
# model evaluation
    r2 = r2_score(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test,y_pred)

    #print knn evaluation metrics 
    print(f"R² Score: {r2:.2%}") # Higher is better
    print(f"Mean Absolute Error (MAE): {mae:.2f}") # Lower is better 
    print(f"Mean Squared Error (MSE): {mse:.2f}") # Lower is better
    return knn

   # confusion = confusion_matrix(y_true=actual, y_pred=pred)
    #print(str(confusion))
   # report = classification_report(actual, pred)
    #print(str(report))

import numpy as np 
import pickle as p # p stands for pickle
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score

def init_knn_model(dt):
    #split the data into training and test sets 
    # starting with splitting it into features (x) and target (Y)

    y = dt["Exam_Score"]
    x = dt.drop(columns='Exam_Score', axis=1) 
    # split the data into training and test sers 
    x_train,x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=50) #30% of the data will be used for testing and 70% will be used for training
    x_train = np.array(list(x_train))
    y_train = np.array(list(y_train))
    x_test = np.array(list(x_test))
    y_test = np.array(list(y_test))
    #next im going to scale the features using standardscaler
    #scaler = StandardScaler()
    #x_train = scaler.fit_transform(x_train)
    #x_test = scaler.transform(x_test)

#now the models ready to train for this use a fixed model of 3 for k

    knn = KNeighborsClassifier()
    knn.fit(X=x_train, y=y_train)
    pred = knn.predict(X=x_test)
    actual = y_test
    score = knn.score(x_test, y_test)
    print(f"{score:.2%}")

    confusion = confusion_matrix(y_true=actual, y_pred=pred)
    print(str(confusion))
    report = classification_report(actual, pred)
    print(str(report))

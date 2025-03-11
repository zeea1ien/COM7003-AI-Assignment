import pandas as pd
from process_dataset import *
from KNN_Model import init_knn_model
from Linear_Model import init_Linear_Model
from RandomForest_Model import init_Random_Forest_Model

#Load the student data.
dt = pd.read_csv("StudentPerformanceFactors2.csv")
dt = clean_drop(dt)
dt = normalise_boolean(dt)
init_knn_model(dt)
print("---------------------------------------------------------------")
init_Linear_Model(dt)
print("---------------------------------------------------------------")
init_Random_Forest_Model(dt)
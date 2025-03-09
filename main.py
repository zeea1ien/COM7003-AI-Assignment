import pandas as pd
from process_dataset import *
from KNN_Model import init_knn_model
from Linear_Model import init_Linear_Model

#Load the student data.
dt = pd.read_csv("StudentPerformanceFactors2.csv")
dt = clean_drop(dt)
dt = normalise_boolean(dt)
init_knn_model(dt)
init_Linear_Model(dt)
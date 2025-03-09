import pandas as pd
from process_dataset import *

#Load the student data.
dt = pd.read_csv("StudentPerformanceFactors2.csv")
dt = clean_drop(dt)
dt = normalise_boolean(dt)
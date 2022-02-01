# Train Random Forest Regressor on dataframe trainingFirstCycle
import os
import psutil
import math
import time
import pandas
import sklearn
import fastai
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
from sklearn.metrics import mean_squared_error
from sklearn.tree import export_graphviz
import feather
import unittest

# Get the sum of the system and user CPU time of the current process in nanoseconds
# Nanoseconds since the epoch, which is 1 January 1601, 00:00:00 for Windows
# At the beginning of the process
start = time.process_time_ns()
# Read feather formatted trainingFirstCycle and define as array X_train. This is the training set
X_train = pandas.read_feather(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle/trainingFirstCycle.feather")
# Define X_train.rent_count as dependent variable Y_train. This is the dependent variable of the training set, the column to be predicted.
Y_train = X_train.rent_count
# TODO Visualize X_train and Y_train in a scatterplot
    # Pandas method dataframe.plot.scatter
X_train.plot.scatter()
    # TODO Set properties of scatterplot (colour, grading, etc.)
# Read csv formatted evalidateFirstCycle and define as array X_validate. This is the name of the validation set.
X_validate = pandas.read_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle/validateFirstCycle.csv")
# Read y_name_validation.csv and define as Y_validate. This is the dependent variable of the validation set, the column to be predicted.
Y_validate = pandas.read_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/FirstCycle/y_name_validation.csv")
# Create sklearn.ensemble.RandomForestRegressor() object
RF1 = sklearn.ensemble.RandomForestRegressor()
# Run fit method on training set
RF1.fit(X_train, Y_train)
# Predict y variable in validation set.
# TODO Visualize RF1.fit using export_graphviz
y_pred=RF1.predict(X_validate)
y_true=Y_validate
# TODO Fix value error
# TODO Fix parameter squared=False
score=sklearn.metrics.mean_squared_log_error(y_true, y_pred)
print(score)
# TODO Visualize score

# Return further parameters

# Nanoseconds since the epoch
# At the end of the process
end = time.process_time_ns()
runtime = end-start

# Get CPU usage
# How much cpu is used in total numbers
cpu_load = psutil.getloadavg()
# How many percent of the cpu are being used. Multiply by 100 in order to get a percent instead of a decimal.
cpu_usage = (cpu_load(os.cpu_count()) * 100

print("Time elapsed:", runtime, "nanoseconds")
print("CPU used:", cpu_usage, "%")
print("RAM memory used:", psutil.virtual_memory()[2]), "%")
# TODO Visualize parameters
# TODO Save all prints into a file

if __name__ == '__main__':
    unittest.main(verbosity=2)

import sys
import os
import pandas
import numpy
import torch
import fastai
from fastai.tabular.core import add_datepart

# Create a dataframe
trainingSetFirstCycle = pandas.read_csv(
    "C:/Users/henri/OneDrive/Dokumente/Berufseinstieg/Sprachtechnologie/Predicting_Bike_Rental_Demand/Datasets/train.csv",
    low_memory=False, parse_dates=["datetime"])
# Calculate the log for each value in dependent variable "count"
# Each value in "rent_count" is being replaced by its log natural logarithm by defining the column a a variable and performing numpy.log on it
trainingSetFirstCycle.rent_count = numpy.log(trainingSetFirstCycle.rent_count)
# Use fastai function "add_datepart"
trainingSetFirstCycle = add_datepart(trainingSetFirstCycle, "datetime", drop=True)
# TODO Check missing values
# TODO Add missing numeric values
# "proc_DF"
# TODO Move dependent variable into a separate variable
# TODO Save dataframe into feather format

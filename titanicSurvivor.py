import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from tensorflow import feature_column as fc
import tensorflow as tf

# Load dataset.
dftrain = pd.read_csv('Dataset/train.csv') # training data
dfeval = pd.read_csv('Dataset/eval.csv') # testing data

y_train = dftrain.pop('survived')
y_eval = dfeval.pop('survived')

# print(dftrain.describe())

dftrain.hist(column='age')
print(dftrain.age.hist(bins=20))
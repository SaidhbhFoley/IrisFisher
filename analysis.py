# Author: Saidhbh Foley
# Analysing the dataset

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import os

# Reading in the Iris file
iris_data = pd.read_csv("iris_csv.csv")
iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

# Size of the data set
iris_data['species'].unique()
print(iris_data.groupby('species').size())

# Just some general investigation of the data
# Find out the min, max, mean, median and std
iris_data.min()
iris_data.max()
iris_data.mean()
iris_data.median()
iris_data.std()

# Summary of data
summary = iris_data.describe()
summary = summary.transpose()
summary.head()
print(summary)
#print(summary)

# Summary by the attributes
print(iris_data.groupby(['species'])[['sepal_length']].describe())
print(iris_data.groupby(['species'])[['sepal_width']].describe())
print(iris_data.groupby(['species'])[['petal_length']].describe())
print(iris_data.groupby(['species'])[['petal_width']].describe())

# Outputs summary of variable to individual txt files
with open ('sepal_length.txt', 'wt') as f:
    print(iris_data.groupby(['species'])[['sepal_length']].describe(), file=f)

with open ('sepal_width.txt', 'wt') as f:
    print(iris_data.groupby(['species'])[['sepal_width']].describe(), file=f)

with open ('petal_length.txt', 'wt') as f:
    print(iris_data.groupby(['species'])[['petal_length']].describe(), file=f)

with open ('petal_width.txt', 'wt') as f:
    print(iris_data.groupby(['species'])[['petal_width']].describe(), file=f)

with open ('variable_summary.txt', 'wt') as f:
    print(iris_data.groupby(['species'])[['sepal_length']].describe(), file=f)
    print(iris_data.groupby(['species'])[['sepal_width']].describe(), file=f)
    print(iris_data.groupby(['species'])[['petal_length']].describe(), file=f)
    print(iris_data.groupby(['species'])[['petal_width']].describe(), file=f)

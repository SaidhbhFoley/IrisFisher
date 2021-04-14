# Author: Saidhbh Foley 
# Messing around with the data set


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

# Reading in the Iris file
iris_data = pd.read_csv("iris_csv.csv")
iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

# Specifies how much to show
iris_data.head(10)

# Finding out the species/how many of each species there are
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

# Playing with boxplots
# Sepal Distribution
sns.set(style="whitegrid", palette="mako", rc={'figure.figsize':(11.7,8.27)})
plt.title("Distribution of Sepal Length")
sns.boxplot(x='species', y='sepal_length', data=iris_data)
plt.show()
# Petal Width
sns.set(style="whitegrid", palette="crest", rc={'figure.figsize':(11.7,8.27)})
plt.title("Distribution of Petal Width")
sns.boxplot(x='species', y='petal_width', data=iris_data)
plt.show()
# Petal Length
sns.set(style="whitegrid", palette="crest", rc={'figure.figsize':(11.7,8.27)})
plt.title("Distribution of Petal Length")
sns.boxplot(x='species', y='petal_length',data=iris_data)
plt.show()

# Playing with scatterplots
sns.set(style="whitegrid", palette="mako", rc={'figure.figsize':(11.7,8.27)})
plt.title("Petal Width and Petal Length")
sns.scatterplot(x='petal_width', y='petal_length', data=iris_data, hue='species')
plt.show()

# Playing with pairplots
sns.set(style="whitegrid")
sns.pairplot(iris_data, hue='species', palette="crest")
plt.show()

# Histograms
sns.set(style="whitegrid", palette="mako", rc={'figure.figsize':(11.7,8.27)})
plt.title("Distribution of Sepal Length")
sns.histogram(x='species', y='sepal_length', data=iris_data)
plt.show()
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

# Exploring the dataset to obtain what species it contains and the number of data points for each species.
iris_data['species'].unique()
print(iris_data.groupby('species').size())
# Ensuring no blanks/missing data
print(iris_data.info())

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
# At first I misread this and interpretted this as an individual txt file for each variable
# Therefore changed the code to reflect what was asked for
#with open ('sepal_length.txt', 'wt') as f:
    #print(iris_data.groupby(['species'])[['sepal_length']].describe(), file=f)

#with open ('sepal_width.txt', 'wt') as f:
    #print(iris_data.groupby(['species'])[['sepal_width']].describe(), file=f)

#with open ('petal_length.txt', 'wt') as f:
    #print(iris_data.groupby(['species'])[['petal_length']].describe(), file=f)

#with open ('petal_width.txt', 'wt') as f:
    #print(iris_data.groupby(['species'])[['petal_width']].describe(), file=f)

# Outputs summary of variables to a single txt file
with open ('variable_summary.txt', 'wt') as f:
    print(iris_data.groupby(['species'])[['sepal_length']].describe(), file=f)
    print(iris_data.groupby(['species'])[['sepal_width']].describe(), file=f)
    print(iris_data.groupby(['species'])[['petal_length']].describe(), file=f)
    print(iris_data.groupby(['species'])[['petal_width']].describe(), file=f)

# Visualisation of the Dataset
# Visualisation of dataset broken into separate .py files
# Petal Length Hist (adding comments for this one, they apply to all the plots, where there was additional/differing code I added a comment explaining why I did that piece of code)
sns.set(style="white", rc={'figure.figsize':(11.7,8.27)})
# Setting the background style to be white with no gridlines, specifying figure size
sns.set_style("ticks")
# Addition of ticks to the y-axis
plt.title("Distribution of Petal Length")
# Setting the title of the plot
sns.histplot(data=iris_data, x="petal_length", hue="species", palette="viridis", element="step", multiple="dodge", shrink=.8, legend=False)
# Selecting the dataset and looking at petal length only, the hue means all species will be coloured differently, then some general formatting of the hist
plt.xlabel("Petal Length (cm)")
# Setting the x-label
plt.legend(title="Species",loc='upper left', labels=['Iris setosa', "Iris versicolor", 'Iris virginica'])
sns.despine()
# Removing the top and right lines to make the graph more visually appealing
plt.savefig('Distribution of Petal Length')
# Saving the file
plt.clf()
# Clearing the file (I was having issues with the files becoming overlapped and muddled this command stopped them getting messed up with the data from other plots)
# Petal Width Hist
sns.set(style="white", rc={'figure.figsize':(11.7,8.27)})
sns.set_style("ticks")
plt.title("Distribution of Petal Width")
sns.histplot(data=iris_data, x="petal_width", hue="species", palette="viridis", element="step", multiple="dodge", shrink=.8)
plt.xlabel("Petal Width (cm)")
sns.despine()
plt.savefig('Distribution of Petal Width')
plt.clf()
# Sepal Length Hist
sns.set(style="white", rc={'figure.figsize':(11.7,8.27)})
sns.set_style("ticks")
plt.title("Distribution of Sepal Length")
sns.histplot(data=iris_data, x="sepal_length", hue="species", palette="viridis", element="step", multiple="dodge", shrink=.8)
plt.xlabel("Sepal Length (cm)")
sns.despine()
plt.savefig('Distribution of Sepal Length')
plt.clf()
# Sepal Width Hist
sns.set(style="white", rc={'figure.figsize':(11.7,8.27)})
sns.set_style("ticks")
plt.title("Distribution of Sepal Width")
sns.histplot(data=iris_data, x="sepal_width", hue="species", palette="viridis", element="step", multiple="dodge", shrink=.8)
plt.xlabel("Sepal Width (cm)")
sns.despine()
plt.savefig('Distribution of Sepal Width')
plt.clf()

# Scatterplots
# Sepal L vs W
sns.set(style="white", palette="viridis", rc={'figure.figsize':(11.7,8.27)})
plt.title("Sepal Length Vs Sepal Width")
sns.scatterplot(data=iris_data, x="sepal_length", y="sepal_width", hue="species", style="species")
# Here I added species as hue and style for ease of distinguishing between species, style creates different shapes, combined with hue it makes species identification easier
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Sepal Width (cm)")
sns.despine()
plt.savefig('Sepal Length and Sepal Width')
plt.clf()
# Petal L vs W
sns.set(style="white", rc={'figure.figsize':(11.7,8.27)})
plt.title("Petal Length and Petal Width")
sns.scatterplot(data=iris_data, x="petal_length", y="petal_width", hue="species", style="species")
plt.xlabel("Petal Length (cm)")
plt.ylabel("Petal Width (cm)")
sns.despine()
plt.savefig('Petal Length Vs Petal Width')
plt.clf()

# Pairplots (just for fun)
sns.set(style="white", rc={'figure.figsize':(11.7,8.27)})
sns.pairplot(iris_data, hue='species', palette="crest")
plt.savefig("Pairplot Iris Dataset")
plt.clf()

# Boxplots (just for fun)
# Petal Length
sns.set(style="white", palette="crest", rc={'figure.figsize':(11.7,8.27)})
sns.boxplot(data=iris_data, x="species", y="petal_length")
plt.xlabel("Species")
plt.ylabel("Petal Length (cm)")
sns.despine()
plt.savefig('Boxplot Petal Length')
plt.clf()
# Petal Width
sns.set(style="white", palette="crest", rc={'figure.figsize':(11.7,8.27)})
sns.boxplot(data=iris_data, x="species", y="petal_width")
plt.xlabel("Species")
plt.ylabel("Petal Width (cm)")
sns.despine()
plt.savefig('Boxplot Petal Width')
plt.clf()
# Sepal Length
sns.set(style="white", palette="crest", rc={'figure.figsize':(11.7,8.27)})
sns.boxplot(data=iris_data, x="species", y="sepal_length")
plt.xlabel("Species")
plt.ylabel("Sepal Length (cm)")
sns.despine()
plt.savefig('Boxplot Sepal Length')
plt.clf()
# Sepal Width
sns.set(style="white", palette="crest", rc={'figure.figsize':(11.7,8.27)})
sns.boxplot(data=iris_data, x="species", y="sepal_width")
plt.xlabel("Species")
plt.ylabel("Sepal Width (cm)")
sns.despine()
plt.savefig('Boxplot Sepal Width')
plt.clf()
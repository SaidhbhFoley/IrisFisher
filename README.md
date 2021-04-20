# IrisFisher

## Iris Fisher Data Set Overview
The Iris flower data set or Fisher's Iris daa set is a multivariate data set. It was first introduced in 1936 in R. A. Fisher's paper *"The use of multiple measurements in taxonomic problems"*. R.A. Fisher was a British statistician and biologist. The dataset contains 50 records of the length and width of sepals and petals (in centimeters) for the three different iris species; *Iris setosa, Iris viginica, Iris versicolor*. Edgar Anderson collected the data on these three species in Quebec, Canada, and due to his collaboration this dataset is also referred to as Anderson's Iris dataset. Anderson collected 50 specimens each on the same day.
Based on the differences observed amongst the three species, Fisher established a linear discrimiinant model to distinguish the species from one another.</p>

The dataset contains 150 records under 5 characteristics:
+ Sepal length (cm)
+ Sepal width (cm)
+ Petal leghth (cm)
+ Petal width (cm)
+ Species: 
    + *Iris setosa* 
    + *Iris versicolor*
    + *Iris virginica*


<p>
   <img src="https://miro.medium.com/max/4800/0*QHogxF9l4hy0Xxub.png">
</p>

   *Iris flower species*
</p>

<p>Since it's publication it has been widely used in the field of data analytics, and is still used to this day. The Iris Dataset is the best known dataset in pattern recognition literature.</p>

## Libraries Utilised
Pandas, Matplotlib, Numpy and Seabron were all imported for analysing this dataset.

### Pandas
Pandas is a software library that offers easy-to-use data analysis and manipulation in Python.

### Matplotlib and Numpy
Matlib is a plotting library used in Python programming. Numpy is an extension of Matlib.

### Seaborn
Seaborn is a Python data visualisation library based on Matplotlib. Seaborn allows the user to create more attractive and informative statistical graphs.

These libraries were imported using the following code:

```
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
```

## Dataset
### Import
Fisher's dataset was imported using the following code:

```
iris_data = pd.read_csv("iris_csv.csv")
iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']
```

The above code also renamed the column headings for user ease.

The dataset was obtained from github and is included in the references.

### Researching the Dataset
#### Size of the Dataset and Investigating Blanks
The first step taken in researching this data set was to investigate the species and the size of the data set. This was using the code below:
```
# Exploring the dataset to obtain what species it contains and the number of data points for each species.
iris_data['species'].unique()
print(iris_data.groupby('species').size())
```

```
# Ensuring no blanks/missing data
print(iris_data.info())
```

The above code prints:
```
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
 #   Column        Non-Null Count  Dtype  
---  ------        --------------  -----  
 0   sepal_length  150 non-null    float64
 1   sepal_width   150 non-null    float64
 2   petal_length  150 non-null    float64
 3   petal_width   150 non-null    float64
 4   species       150 non-null    object 
dtypes: float64(4), object(1)
memory usage: 6.0+ KB
None
```
Showing that the dataset is complete and contains no blank entries or missing data.

#### General Investigation of the Dataset
Once this information had been obtained the next step was to generally investigate it by finding out the min, max, mean, median and the standard deviation of the dataset. This was done using the code below:

```
# Just some general investigation of the data
# Find out the min, max, mean, median and std
iris_data.min()
iris_data.max()
iris_data.mean()
iris_data.median()
iris_data.std()
```
#### Summary of the Dataset
In order to visualise an overview of the dataset, for sepal length, sepal width, petal length and petal width, the following code was used:

```
# Summary of data
summary = iris_data.describe()
summary = summary.transpose()
summary.head()
print(summary)
```
Which produces the following table, summarising the count, mean, standard deviation, min, interquartiles and max.

|            | Count  | Mean | Std   | Min | 25%  | 50%   | 75%  | Max  |
|---         |---     |---   |---    |---  |---   |---    |---   |---   |
 Sepal Length| 150.0  | 5.84 | 0.828 | 4.3 | 5.1  | 5.8   | 6.4  | 7.9  | 
 Sepal Width | 150.0  | 3.05 | 0.433 | 2.0 | 2.8  | 3.0   | 3.3  | 4.4  |
 Petal Length| 150.0  | 3.75 | 1.764 | 1.0 | 1.6  | 4.3   | 5.1  | 6.9  |  
 Petal Width | 150.0  | 1.19 | 0.763 | 0.1 | 0.3  | 1.3   | 1.8  | 2.5  |
  

## Analysing the Dataset
### Summary for Each Attribute
Outputs a summary of each variable to a single text file. The code for this is displayed below:
```
with open ('variable_summary.txt', 'wt') as f:
    print(iris_data.groupby(['species'])[['sepal_length']].describe(), file=f)
    print(iris_data.groupby(['species'])[['sepal_width']].describe(), file=f)
    print(iris_data.groupby(['species'])[['petal_length']].describe(), file=f)
    print(iris_data.groupby(['species'])[['petal_width']].describe(), file=f)
```
This creates a text file named variable_summary.txt where 4 tables summarise sepal length, sepal width, petal length and petal width respectively. These tables are shown below

#### Sepal Length  

|Species            |Count   |Mean   |Std       |Min    |25%    |50%    |75%    |Max    |
|---                |---     |---    |---       |---    |---    |---    |---    |---    |
 *Iris setosa*      |50.0    |5.006  |0.352490  |4.3    |4.8    |5.0    |5.2    |5.8    |
 *Iris versicolor*  |50.0    |5.936  |0.516171  |4.9    |5.6    |5.9    |6.3    |7.0    |
 *Iris virginica*   |50.0    |6.588  |0.635880  |4.9    |6.2    |6.5    |6.9    |7.9    |


#### Sepal Width  

|Species             |Count   |Mean   |Std       |Min    |25%    |50%    |75%    |Max    |
|---                 |---     |---    |---       |---    |---    |---    |---    |---    |
 *Iris setosa*       |50.0    |3.418  |0.381024  |2.3    |3.1    |3.4    |3.6    |4.4    |
 *Iris versicolor*   |50.0    |2.770  |0.313798  |2.0    |2.5    |2.8    |3.0    |3.4    |
 *Iris virginica*    |50.0    |2.974  |0.322497  |2.2    |2.8    |3.0    |3.1    |3.8    |

#### Petal Length

|Species             |Count   |Mean   |Std       |Min    |25%    |50%    |75%    |Max    |
|---                 |---     |---    |---       |---    |---    |---    |---    |---    |
 *Iris setosa*       |50.0    |1.464  |0.173511  |1.0    |1.4    |1.5    |1.5    |1.9    |
 *Iris versicolor*   |50.0    |4.260  |0.469911  |3.0    |4.0    |4.3    |4.6    |5.1    |
 *Iris virginica*    |50.0    |5.552  |0.551895  |4.5    |5.1    |5.5    |5.8    |6.9    |

#### Petal Width
|Species             |Count   |Mean   |Std       |Min    |25%    |50%    |75%    |Max    |
|---                 |---     |---    |---       |---    |---    |---    |---    |---    |
 *Iris setosa*       |50.0    |0.244  |0.107210  |0.1    |0.2    |0.2    |0.3    |0.6    |
 *Iris versicolor*   |50.0    |1.326  |0.197753  |1.0    |1.2    |1.3    |1.5    |1.8    |
 *Iris virginica*    |50.0    |2.026  |0.274650  |1.4    |1.8    |2.0    |2.3    |2.5    |

### Visualisation of the Dataset
#### Histograms
Histograms are the most commonly used graph to show frequency distributions. The following attributes are plotted on histograms:
+ Petal length
+ Petal width
+ Sepal length 
+ Sepal width
##### Distribution of Petal Length
![Alt text](https://github.com/SaidhbhFoley/IrisFisher/blob/main/Distribution%20of%20Petal%20Length.png?raw=true)
Plot 1. Attribute: Petal Length
##### Distribution of Petal Width
![Alt text](https://github.com/SaidhbhFoley/IrisFisher/blob/main/Distribution%20of%20Petal%20Width.png?raw=true)
Plot 2. Attribute: Petal Width
##### Distribution of Sepal Length
![Alt text](https://github.com/SaidhbhFoley/IrisFisher/blob/main/Distribution%20of%20Sepal%20Length.png?raw=true)
Plot 3. Attribute: Sepal Length
##### Distribution of Sepal Width
![Alt text](https://github.com/SaidhbhFoley/IrisFisher/blob/main/Distribution%20of%20Sepal%20Width.png?raw=true)
Plot 4. Attribute: Sepal Width

From the histograms it is clear that the petal length and petal width are defining features for each species particularly *Iris setosa* who's petals are signigificantly shorter and narrower than *Iris versicolor* and *Iris virginica*. There is some overlap between *Iris versicolor* and *Iris virginica*. The overall trend is *Iris setosa* has the smallest petals both in length and width, followed by *Iris versicolor* and *Iris virginica*. When it comes to sepal length it follows a similar trend however there is more overlap between the species and therefore they are harder to differentiate on sepal length alone. With regards to sepal width this feature cannot be used to distinguish between the species using a histogram.

#### Scatterplots
Scatterplots are used to display relationships between two variables. The below scatterplots compare petal length with petal width and sepal length with sepal width.
##### Petal Length Vs. Petal Width
![Alt text](https://github.com/SaidhbhFoley/IrisFisher/blob/main/Petal%20Length%20Vs%20Petal%20Width.png?raw=true)
Plot 5. Attribute: Petal Length and Petal Width

##### Sepal Length Vs. Sepal Width
![Alt text](https://github.com/SaidhbhFoley/IrisFisher/blob/main/Sepal%20Length%20and%20Sepal%20Width.png?raw=true)
Plot 6. Attribute: Sepal Length and Sepal Width

The scatterplots further illustrate that petal length and width are the distinguishing features for identifying the species of Iris. Particularly for *Iris versicolor* and *Irish virginica* which cannot be distinguished using sepal length and sepal width.

### Some Extra Visualisation of the Dataset (for fun)
#### Pairplots
Pairplots are a simple way to visualise relationships between each variable and produce a matrix of relationships between each attribute in the dataset.
![Alt text](https://github.com/SaidhbhFoley/IrisFisher/blob/main/Pairplot%20Iris%20Dataset.png?raw=true)
Plot 7. Pairplot showing all four attributes for the three species of Iris.

#### Boxplots
Boxplots are a great way to quickly visualise one attribute at a time and it's quartiles.
##### Comparison of Petal Length
![Alt text](https://github.com/SaidhbhFoley/IrisFisher/blob/main/Boxplot%20Petal%20Length.png?raw=true)
Plot 8. Attribute: Petal Length
##### Comparison of Petal Width
![Alt text](https://github.com/SaidhbhFoley/IrisFisher/blob/main/Boxplot%20Petal%20Width.png?raw=true)
Plot 9. Attribute: Petal Width
##### Comparison of Sepal Length
![Alt text](https://github.com/SaidhbhFoley/IrisFisher/blob/main/Boxplot%20Sepal%20Length.png?raw=true)
Plot 10. Attribute: Sepal Length
##### Comparison of Sepal Width
![Alt text](https://github.com/SaidhbhFoley/IrisFisher/blob/main/Boxplot%20Sepal%20Width.png?raw=true)
Plot 11. Attribute: Sepal Width

The boxplots further signify the best attributes for discriminating between these three species of Iris. Highlighting yet again that petal length and width, and to a lesser degree sepal length, are the attributes to distinguish amongst these three species.

## Conclusion
The most useful attributes for distinguishing between *Iris setosa*, *Iris versicolor* and *Iris virginica* is petal length and petal width. *I. setosa* is the most easily distinguishable of the three using petal length and petal width, as there is some overlap between *I. versicolor* and *I. virginica*. Sepal length can be used to identify *I. setosa* and to a lesser extent *I. versicolor* and *I. virginica*. Sepal width is not a good attribute for distinguishing these species from one another.

## References:
[Background on Iris Dataset](https://en.wikipedia.org/wiki/Iris_flower_data_set)  
[Further reading on Iris Dataset](https://www.learnbay.co/data-science-course/blog-post/exploratory-data-analysis-on-iris-dataset/)  
[Data set obtained from](https://gist.github.com/netj/8836201#file-iris-csv)  
[Image of Iris species](https://miro.medium.com/max/2550/1*7bnLKsChXq94QjtAiRn40w.png)  
[Python – Basics of Pandas using Iris Dataset](https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/)  
[Boxplots and Histograms](https://www.geeksforgeeks.org/box-plot-and-histogram-exploration-on-iris-data/)  
[Iris Data Visualisation](https://www.kaggle.com/crbelhekar619/iris-dataset-eda-visualization)  
[Exploratory analysis on Iris Dataset](https://medium.com/@sulavojha11/exploratory-data-analysis-on-iris-dataset-84832e519040)  
[Introduction to Seaborn](https://seaborn.pydata.org/introduction.html)  
[Seaborn Scatterplots](https://seaborn.pydata.org/generated/seaborn.scatterplot.html#seaborn.scatterplot)  
[Improving Scatterplots in Seaborn](https://towardsdatascience.com/7-points-to-create-better-scatter-plots-with-seaborn-9f0202fb2ba4)  
[Visualising Statistical Relationships Seaborn](https://seaborn.pydata.org/tutorial/relational.html)  
[Seaborn Histplot](https://seaborn.pydata.org/generated/seaborn.histplot.html)  
[Seaborn Boxplots](https://pythonbasics.org/seaborn-boxplot/)  
[Seaborn Pairplots](https://seaborn.pydata.org/generated/seaborn.pairplot.html)  
[Controlling figure aesthetics Seaborn](http://seaborn.pydata.org/tutorial/aesthetics.html)  
[Editing figure size in Seaborn plot](https://stackoverflow.com/questions/31594549/how-do-i-change-the-figure-size-for-a-seaborn-plot)  
[Seaborn Colour Palettes](https://seaborn.pydata.org/tutorial/color_palettes.html)  
[Customising ticks in Seaborn](https://jakevdp.github.io/PythonDataScienceHandbook/04.10-customizing-ticks.html)  
[Issues with Seaborn graphs overlapping](https://stackoverflow.com/questions/36018681/stop-seaborn-plotting-multiple-figures-on-top-of-one-another)  
[Pandas overview](https://www.earthdatascience.org/courses/intro-to-earth-data-science/scientific-data-structures-python/pandas-dataframes/run-calculations-summary-statistics-pandas-dataframes/)  
[Pandas dataframe](https://www.ritchieng.com/pandas-selecting-multiple-rows-and-columns/)  
[Github Markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)  
[Further Github Markdown Formatting](https://docs.github.com/en/github/writing-on-github/organizing-information-with-tables)  
[How to add images to Github](https://stackoverflow.com/questions/14494747/how-to-add-images-to-readme-md-on-github)  
[Github italics issue](https://github.com/madskristensen/MarkdownEditor/issues/68)  


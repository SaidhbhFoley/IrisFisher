# IrisFisher

Iris Fisher Data Set Overview
---
<p> The Iris flower data set or Fisher's Iris daa set is a multivariate data set. It was first introduced in 1936 in R. A. Fisher's paper <e/m>"The use of multiple measurements in taxonomic problems"<e/m>. R.A. Fisher was a British statistician and biologist. The dataset contains 50 records of the length and width of sepals and petals (in centimeters) for the three different iris species; <e/m> Iris setosa, Iris viginica, Iris versicolor<e/m>. Based on the differences observed amongst the three species, Fisher established a linear discrimiinant model to distinguish the species from one another.<p>

<p> The dataset contains 150 records under 5 characteristics:
1.  Sepal length (cm)
2.  Sepal width (cm)
3.  Petal leghth (cm)
4.  Petal width (cm)
5.  Species: <e/m> Iris setosa, Iris versicolor, Iris virginica<e/m>

![alt text](https://i.ebayimg.com/images/g/PxUAAMXQwwlSAaCr/s-l300.jpg) iris setosa
![alt text](https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg) iris virginica
![alt text](hhttps://upload.wikimedia.org/wikipedia/commons/2/27/Blue_Flag%2C_Ottawa.jpg) iris versicolor


<p>Since it's publication it has been widely used in the field of data analytics, and is still used to this day. The Iris Dataset is the best known dataset in pattern recognition literature.<p>

Libraries Utilised
---
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
#### Size of the Dataset
The first step taken in researching this data set was to investigate the species and the size of the data set. This was using the code below:
```
# Finding out the species/how many of each species there are
iris_data['species'].unique()
print(iris_data.groupby('species').size())
```
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
This gave the following table

|            | Count  | Mean | Std   | Min | 25%  | 50%   | 75%  | Max  |
|---         |---     |---   |---    |---  |---   |---    |---   |---   |
 Sepal Length| 150.0  | 5.84 | 0.828 | 4.3 | 5.1  | 5.8   | 6.4  | 7.9  | 
 Sepal Width | 150.0  | 3.05 | 0.433 | 2.0 | 2.8  | 3.0   | 3.3  | 4.4  |
 Petal Length| 150.0  | 3.75 | 1.764 | 1.0 | 1.6  | 4.3   | 5.1  | 6.9  |  
 Petal Width | 150.0  | 1.19 | 0.763 | 0.1 | 0.3  | 1.3   | 1.8  | 2.5  |
  

Analysing the Dataset
---
Outputs a summary of each variable to a single text file. The code for this is displayed below:
```
with open ('variable_summary.txt', 'wt') as f:
    print(iris_data.groupby(['species'])[['sepal_length']].describe(), file=f)
    print(iris_data.groupby(['species'])[['sepal_width']].describe(), file=f)
    print(iris_data.groupby(['species'])[['petal_length']].describe(), file=f)
    print(iris_data.groupby(['species'])[['petal_width']].describe(), file=f)
```
This creates a text file named variable_summary.txt where 4 tables summarise sepal length, sepal width, petal length and petal width respectively. These tables are shown below

### Sepal Length                                            
|Species            |Count   |Mean   |Std       |Min    |25%    |50%    |75%    |Max    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-setosa        |50.0    |5.006  |0.352490  |4.3    |4.8    |5.0    |5.2    |5.8    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-versicolor    |50.0    |5.936  |0.516171  |4.9    |5.6    |5.9    |6.3    |7.0    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-virginica     |50.0    |6.588  |0.635880  |4.9    |6.2    |6.5    |6.9    |7.9    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- -------- 

### Sepal Width                                              
|Species            |Count   |Mean   |Std       |Min    |25%    |50%    |75%    |Max    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-setosa        |50.0    |3.418  |0.381024  |2.3    |3.1    |3.4    |3.6    |4.4    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-versicolor    |50.0    |2.770  |0.313798  |2.0    |2.5    |2.8    |3.0    |3.4    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-virginica     |50.0    |2.974  |0.322497  |2.2    |2.8    |3.0    |3.1    |3.8    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- -------- 

### Petal Length
|Species            |Count   |Mean   |Std       |Min    |25%    |50%    |75%    |Max    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-setosa        |50.0    |1.464  |0.173511  |1.0    |1.4    |1.5    |1.5    |1.9    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-versicolor    |50.0    |4.260  |0.469911  |3.0    |4.0    |4.3    |4.6    |5.1    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-virginica     |50.0    |5.552  |0.551895  |4.5    |5.1    |5.5    |5.8    |6.9    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- -------- 

### Petal Width
|Species            |Count   |Mean   |Std       |Min    |25%    |50%    |75%    |Max    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-setosa        |50.0    |0.244  |0.107210  |0.1    |0.2    |0.2    |0.3    |0.6    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-versicolor    |50.0    |1.326  |0.197753  |1.0    |1.2    |1.3    |1.5    |1.8    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- --------                                                     
|Iris-virginica     |50.0    |2.026  |0.274650  |1.4    |1.8    |2.0    |2.3    |2.5    |
-------------------- -------- ------- ---------- ------- ------- ------- ------- -------- 



References:
data set obtained from: https://gist.github.com/netj/8836201#file-iris-csv
https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/
https://pythonbasics.org/seaborn-boxplot/
https://stackoverflow.com/questions/31594549/how-do-i-change-the-figure-size-for-a-seaborn-plot
https://seaborn.pydata.org/tutorial/color_palettes.html
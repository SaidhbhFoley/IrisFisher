import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

iris_data = pd.read_csv("iris_csv.csv")
iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']

#Sepal Length Histogram
plt.figure(figsize = (10, 7))

  
plt.hist("sepal_length", bins = 20, color = "green")
plt.title("Sepal Length in cm")
plt.xlabel("Sepal_Length_cm")
plt.ylabel("Count")
plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

iris_data = pd.read_csv("iris_csv.csv")
iris_data.columns = ['sepal_length', 'sepal_width' , 'petal_length', 'petal_width', 'species']



sns.set(style="whitegrid", palette="mako", rc={'figure.figsize':(11.7,8.27)})
plt.title("Distribution of Sepal Length")
sns.histplot(x='species', y='sepal_length', data=iris_data)
plt.show()
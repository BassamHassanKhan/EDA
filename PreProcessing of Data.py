# -*- coding: utf-8 -*-
"""Untitled5.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Oi0vWBoo7kfvvW2WEpySripT13xPApvg
"""

#computing libraries
import numpy as np
import pandas as pd

#potting libraries
import matplotlib.pyplot as plt
import seaborn as sns

#preprocessiong modules
from sklearn.preprocessing import LabelEncoder

data=pd.read_csv("/content/drive/MyDrive/Data Science/train_qWM28Yl.csv")

data

#grouping the data wrt target column
gp=data.groupby('is_claim').count()

data.describe()

#countplot
sns.countplot(x='is_claim',data=data)
plt.xlabel('is claim')
plt.ylabel('count')
plt.title('Distribution of is claim')
plt.show()

data1=data.drop('policy_id',axis=1)

#boxplot
sns.boxplot(x='is_claim',y='age_of_car',data=data)
plt.xlabel('is_claim')
plt.ylabel('age of car')
plt.title('Box plot')
plt.show()



# List to store the non-categorical column names
non_categorical_columns = []

# Iterate over each column in the DataFrame
for column in data1.columns:
    # Check if the column is non-categorical (numeric)
    if data1[column].dtype != 'object' and column != 'is_claim':
        non_categorical_columns.append(column)

# Create the box plots
for column in non_categorical_columns:
    plt.figure()
    sns.boxplot(x='is_claim', y=column, data=data1)
    plt.title(f'Box Plot: {column}')
    plt.show()

data1.info()

#finding correlation
data1.corr()

#correlation heat Map
correlation_matrix = data.corr()
plt.figure(figsize=(17,17))
sns.heatmap(correlation_matrix,annot=True,cmap='Pastel1')
plt.title('Correlation matrix')
plt.show()

#extractinmg categhorical co,umn:
catFeature = [col for col in data1.columns if col in data1.select_dtypes(include=object).columns]
catFeature

#Extracting all features
features=[col for col in data1.columns  ]

#splitting features and target  variable:
x,y=data1.loc[:,features],data1.loc[:,'is_claim']

#checkingb dataset shape
print(x.shape)

catFeatures=[col for col in data1.columns if col in data1.select_dtypes(include=object).columns]
features=[col for col in data1.columns if col not in ['policy_id','is_claim']]

labelEncode = LabelEncoder()
for col in catFeatures:
  x[col]= labelEncode.fit_transform(data[col])

x

data1


# -*- coding: utf-8 -*-
"""LVADSUSR105_Lab1R.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LIHZVVoKTkFXkdsCDVmnhE6AN9DAsTjx
"""

#Regression
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

#1
data = pd.read_csv("/content/drive/MyDrive/expenses.csv")
df = pd.DataFrame(data)

missingvalues  = df.isnull().sum()
df.dropna()
print(missingvalues)
print("There are no null values in the dataset")

q1 = df.quantile(0.25)
q3 = df.quantile(0.75)
iqr = q3-q1

outlier  = ((df<(q1 - iqr*1.5)) | (df>(q3 + iqr*1.5))).any(axis=1)

df[~outlier]

#2
from sklearn.preprocessing import LabelEncoder
encode  = LabelEncoder()
df["sex"] = encode.fit_transform(df["sex"])
df["smoker"] = encode.fit_transform(df["smoker"])
df["region"] = encode.fit_transform(df["region"])

#3
#removing duplicates
df.drop_duplicates

#4
from sklearn.model_selection import train_test_split
x=df.drop("charges",axis=1)
y=df["charges"]

x_train,x_test,y_train,y_test  = train_test_split(x,y,test_size=0.3,random_state=42)

#5
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train)
predicted_op = model.predict(x_test)

#6
from sklearn.metrics import r2_score , mean_squared_error, mean_absolute_error
r_squared  = r2_score(y_test,predicted_op)
mean_Squared_Err = mean_squared_error(y_test,predicted_op)
meanabserr = mean_absolute_error(y_test,predicted_op)
print(r_squared)
print(mean_Squared_Err)
print(meanabserr)

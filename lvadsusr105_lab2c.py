# -*- coding: utf-8 -*-
"""LVADSUSR105_Lab2C.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cyrb2EceVHZUls8JisOo_Z4CxJ_6NUFE
"""

#Classification
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

#1
data = pd.read_csv("/content/drive/MyDrive/booking.csv")
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
df["room type"] = encode.fit_transform(df["room type"])
df["type of meal"] = encode.fit_transform(df["type of meal"])
df["booking status"] = encode.fit_transform(df["booking status"])
df["market segment type"] = encode.fit_transform(df["market segment type"])

#3
#removing duplicates
df.drop_duplicates

#4
from sklearn.model_selection import train_test_split
x=df.drop(["booking status","Booking_ID","date of reservation"],axis=1)
y=df["booking status"]

x_train,x_test,y_train,y_test  = train_test_split(x,y,test_size=0.3,random_state=42)

#5
from sklearn.tree import DecisionTreeClassifier
model = DecisionTreeClassifier()
model.fit(x_train,y_train)
predicted_op = model.predict(x_test)

#6
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score , confusion_matrix
accuracyscore  = accuracy_score(y_test,predicted_op)
precisionscore  = precision_score(y_test,predicted_op)
recallscore  = recall_score(y_test,predicted_op)
f1score = f1_score(y_test,predicted_op)
confusionmatrix  = confusion_matrix(y_test,predicted_op)
print(accuracyscore)
print(precisionscore)
print(recallscore)
print(f1score)
print(confusionmatrix)

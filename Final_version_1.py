import pandas as pd
import numpy as np
import xlrd
import csv
from sklearn import linear_model
import statsmodels.api as sm
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import seaborn as sns

xls_file = pd.ExcelFile('/Users/cansuyuksel/Desktop/Son model/DataSet.xls')
df_0 = xls_file.parse('DataSet.csv')
df_0.drop_duplicates(subset="Game_ID", inplace=True)
df_0[["Is_Free","Windows","Mac","Linux"]] = df_0[["Is_Free","Windows","Mac","Linux"]].astype(int)
df_0 = df_0.drop(df_0[(df_0["Sum_Meta_Total"] == 0.0)].index)
df_0 = df_0.drop(df_0[(df_0["Metacritic"] == 0.0)].index)
df_0 = df_0.drop(df_0[(df_0["Total_Recommendation_Number"] == 0.0)].index)
df_0 = df_0.drop("Ukranian", axis=1)
df_0 = df_0.reset_index(drop=True)
df_0["Price"] = df_0["Price"]/df_0["Price"].max()
df_0['Total_Recommendation_Number'] = df_0['Total_Recommendation_Number'].replace(0,1)
df_0['Recent_Recommendation_Number'] = df_0['Recent_Recommendation_Number'].replace(0,1)
df_0['Total_Recommendation_Number'] = np.log(df_0['Total_Recommendation_Number'])
df_0['Recent_Recommendation_Number'] = np.log(df_0['Recent_Recommendation_Number'])

X = df_0.drop(['Game_Name','Game_ID','Is_Free','Developers','Publishers',"Metacritic",'Recent_Recommendation_Number',
                    'Total_Recommendation_Number',"Total_Percentage", "Recent_Percentage",'Total_Positive_Review_Number',
                    'Recent_Positive_Review_Number','Sum_Meta_Total'],axis=1)

y = df_0["Metacritic"]


model = linear_model.LinearRegression()
model.fit(X, y)
X = sm.add_constant(X)
model = sm.OLS(y, X).fit()
predictions = model.predict(X)

y_true = y
y_pred = predictions

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error

print("First five values of the prediction array : ")

print(predictions[0:5])

print("Mean absolute error of Metacritic predictions = ", mean_absolute_error(y_true, y_pred))

print("Mean squared error of Metacritic predictions = ", mean_squared_error(y_true, y_pred))

print("Maximum value of the prediction array = ",predictions.max())

print("Minimum value of the prediction array = ",predictions.min())

print(model.summary())
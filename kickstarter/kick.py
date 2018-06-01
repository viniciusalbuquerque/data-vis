#!/usr/bin/python

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# df = pd.read_csv('ks-projects-201612.csv')
df2018 = pd.read_csv('ks-projects-201801.csv')
# print(df.shape)
# print(df2018.shape)
# print list(df)
# print list(df2018)
df2018.drop(['ID', 'name', 'usd_pledged_real', 'usd_goal_real', 'backers'], axis=1, inplace=True)
print df2018.shape
# print list(df2018)

# print df2018.corr()

label_column = 'state'
time_column = 'time_elapsed'

df2018['launched'] = pd.to_datetime(df2018['launched'])
df2018['deadline'] = pd.to_datetime(df2018['deadline'])
df2018[time_column] = (df2018.deadline - df2018.launched).astype('timedelta64[h]')
# print df2018['launched'].head(10)
# print(df2018[time_column].head(15))

df2018.drop(['launched', 'deadline'], axis=1, inplace=True)

df2018 = df2018.apply(lambda x: pd.factorize(x)[0])

X = np.array(df2018.drop([label_column], axis=1))
# y = df2018[label_column].shift(-shift_param)
y = df2018[label_column]

# X = preprocessing.scale(X)

# X = [X:~shift_param+1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=89, shuffle=True)

# clf = LinearRegression()
clf = svm.SVC()
clf.fit(X_train, y_train)

print clf.score(X_test, y_test)

corr = df2018.corr()
plt.figure(figsize=(10, 6))
# sns.heatmap(corr, cbar=None, annot=True, cmap='Blues')
sns.pairplot(df2018, hue=label_column)
plt.show()
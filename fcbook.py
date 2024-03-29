# -*- coding: utf-8 -*-
"""FCBOOK.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1b355atUOd8xm6QbwfP6jkVQAmJoewIhZ
"""

import pandas as pd # for data manipulation and analysis, e.g. it offers data structures and operations for manipulating numerical tables and time series.
import matplotlib.pyplot as plt  # for creating static, animated, and interactive visualizations
import seaborn as sns  #  data visualization library based on matplotlib, it provides a high-level interface for drawing attractive and informative statistical graphics
import numpy as np # is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays

# read the json file into a dataframe
df = pd.read_json('your_posts_1.json')
#event = pd.read_json('event_invitations.json')

df.head(3)
#df.tail(3)

# rename the timestamp column
df.rename(columns={'timestamp': 'date'}, inplace=True)

#drop some unnecessary columns
df = df.drop(['attachments', 'title', 'tags'], axis=1)

print(df)
#validate(df['date'])

# making sure it's datetime format
df['date'] = pd.to_datetime(df['date'])

df.head(3)

print(df.shape)
df.tail(3)

df.set_index('date',inplace=True)

post_counts=df.resample('MS').size()  #For 'MS' the dates of the groups are always the first of the month, for 'M' the last day.
#post_means=post_counts.resample('YS').mean(numeric_only=True)

print(post_counts)
#print(post_means)

start_date = '2021-11-15'
end_date   = '2022-11-18'
df2 = df.query('date >= @start_date and date <= @end_date')
print(df2)

sns.set(rc={'figure.figsize':(30,20)})
sns.set(font_scale=3)

x_labels = post_counts.index  #The index() method returns the position at the first occurrence of the specified value.

#plt.bar(x_labels, post_counts,color='orange')
fig, ax = plt.subplots()
ax.bar(x_labels,post_counts,color = "black",edgecolor = "black", linewidth = 2)

plt.plot(post_counts, marker='o')

#ax = post_counts.plot(x='Date', y='Number of posts', figsize=(8,6))
ax = post_counts.plot(x='Date', y='Number of posts')

xcoords = ['2008-01-01', '2009-01-01', '2010-01-01', '2011-01-01', '2012-01-01', '2013-01-01', '2014-01-01', '2015-01-01', '2016-01-01','2017-01-01', '2018-01-01', '2019-01-01', '2020-01-01', '2021-01-01', '2022-01-01', '2023-01-01']
for xc in xcoords:
    plt.axvline(x=xc, color='black', linestyle='--')

#plt.scatter(x_labels, post_counts)

#post_freq=post_counts/np.sum(post_counts)  #frekvencie
#plt.plot(post_freq, marker='o')

post_counts.hist()
#plt.hist(post_counts, bins=20, linewidth=0.5, edgecolor="white")
#post_counts.plot(kind='kde')

pd.plotting.lag_plot(post_counts, lag=1)
#More points tighter in to the diagonal line suggests a stronger relationship and more spread from the line suggests a weaker relationship.
#A ball in the middle or a spread across the plot suggests a weak or no relationship.

from statsmodels.graphics.tsaplots import plot_acf
plot_acf(post_counts)

split = round(len(post_counts) / 2)
X1, X2 = post_counts[0:split], post_counts[split:]
mean1, mean2 = X1.mean(), X2.mean()
var1, var2 = X1.var(), X2.var()
print('mean1=%f, mean2=%f' % (mean1, mean2))
print('variance1=%f, variance2=%f' % (var1, var2))

#plt.plot(np.log(post_counts), marker='o')

"""![An image](https://av-eks-blogoptimized.s3.amazonaws.com/0*Ja-FJ47hkBT-Azib80953.png)

The Augmented Dickey-Fuller test is a type of statistical test called a unit root test.

The intuition behind a unit root test is that it determines how strongly a time series is defined by a trend.



*   **Null Hypothesis (H0)**: If failed to be rejected, it suggests the time series has a unit root, meaning it is non-stationary. It has some time dependent structure.
*   **Alternate Hypothesis (H1)**: The null hypothesis is rejected; it suggests the time series does not have a unit root, meaning it is stationary. It does not have time-dependent structure.



*  $p$-value $> 0.05$: Fail to reject the null hypothesis (H0), the data has a unit root and is non-stationary.
*  $p$-value $\leq  0.05$: Reject the null hypothesis (H0), the data does not have a unit root and is stationary.

"""

from statsmodels.tsa.stattools import adfuller

result = adfuller(post_counts)
print('ADF Statistic: %f' % result[0])
print('p-value: %f' % result[1])
print('used lag: %f' % result[2])
print('num. of obs.: %f' % result[3])
print('Critical Values:')
for key, value in result[4].items():
 print('\t%s: %.3f' % (key, value))

print('The maximized information criterion if autolag is not None: %f' % result[5])

import pandas as pd # for data manipulation and analysis, e.g. it offers data structures and operations for manipulating numerical tables and time series.
import matplotlib.pyplot as plt  # for creating static, animated, and interactive visualizations
import seaborn as sns  #  data visualization library based on matplotlib, it provides a high-level interface for drawing attractive and informative statistical graphics
import numpy as np # is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays

# read the json file into a dataframe
df = pd.read_json('your_posts_1.json')
#event = pd.read_json('event_invitations.json')

df.head(3)
event.tail(3)

# rename the timestamp column
df.rename(columns={'timestamp': 'date'}, inplace=True)

#drop some unnecessary columns
df = df.drop(['attachments', 'title', 'tags'], axis=1)

#print(df)

# making sure it's datetime format
df['date'] = pd.to_datetime(df['date'])

df.head(3)
print(df.shape)
df.tail(3)

#Set the date column as the index of our DataFrame
#Select the column we want to resample by — in this case, is the data column.
#Use the .resample() function with the argument 'MS' (for “Month Start”) to resample our data by month.
#Use .size() to specify what we want to measure each month — in this case, the number of rows (i.e., posts) with a post date that fall within that month.

#df = df[df['date'] > '2022-1-1'] #  case need time interval 
#df['date'] = pd.to_datetime(df['date'])
df.set_index('date',inplace=True)

post_counts=df.resample('MS').size()
#post_counts = post_counts[(post_counts['date'] > '2022-6-1') & (post_counts['date'] <= '2023-1-10')]

#type(post_counts)

print(post_counts)

# set figure size and font size
sns.set(rc={'figure.figsize':(40,20)})
sns.set(font_scale=3)
# set x labels
x_labels = post_counts.index

#create bar plot
sns.barplot(x_labels, post_counts, color="blue")





sns.barplot(x_labels, post_counts, color="blue")

# only show x-axis labels for Jan 1 of every other year
tick_positions = np.arange(10, len(x_labels), step=24)

#reformat date to display year onlyplt.ylabel("post counts")
plt.xticks(tick_positions, x_labels[tick_positions].strftime("%Y"))

# display the plot
plt.show()

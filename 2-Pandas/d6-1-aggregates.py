"""column aggregates

df.column_name.command()
built in commands that are included in Pandas
mean, std, median, min, max, count, nunique, unique

Command	Description 
mean	Average of all values in column
std	Standard deviation
median	Median
max	Maximum value in column
min	Minimum value in column
count	Number of values in column
nunique	Number of unique values in column
unique	List of unique values in column
"""

# import codecademylib
import numpy as np
import pandas as pd

orders = pd.read_csv('myfiles/d6-orders.csv')
# print(orders.head(10))

#find the most expensive shoe price
most_expensive = orders.price.max()
print "highest price", most_expensive

#count the number of colors
num_colors = orders.shoe_color.nunique()
print "color count", num_colors

# group by syntax
# df.groupby('column1').column2.measurement()
# where column1 is the column to aggregate and column2 is the value to measure/calculate on

#show the max price for each shoe type
pricey_shoes = orders.groupby('shoe_type').price.max()
# print(pricey_shoes)

#use reset_index() with groupby to make a new dataframe of the dimensions and metrics: 
# df.groupby('column1').column2.measurement().reset_index()

#also use rename to reset the column name to be more description
pricey_shoes = orders.groupby('shoe_type').price.max().reset_index().rename(columns={'price': 'hi_price'})
print(pricey_shoes)

#use a lambda function to apply other functions, like from numpy
#find cheap shoes - what's the 25th %-tile price for each color?
cheap_shoes = orders.groupby('shoe_color').price.apply(lambda x: np.percentile(x,25)).reset_index()
print 'cheap shoes (pecentile)'
print(cheap_shoes)

# group by 2 columns - very different syntax - using list notation [] (both work for the metric column)
#shoe_counts = orders.groupby(['shoe_type', 'shoe_color'])['id'].count().reset_index().rename(columns={'id':'order_count'})
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index().rename(columns={'id':'order_count'})
print 'shoe count'
print(shoe_counts)

""" pivot tables
df.pivot(columns='ColumnToPivot',
         index='ColumnToBeRows',
         values='ColumnToBeValues')
"""
#start with a group by that groups on the values to make row and column
shoe_counts = orders.groupby(['shoe_type', 'shoe_color']).id.count().reset_index()

shoe_counts_pivot = shoe_counts.pivot(
	columns='shoe_color',
	index='shoe_type',
	values='id').reset_index()

print(shoe_counts)
print(shoe_counts_pivot)
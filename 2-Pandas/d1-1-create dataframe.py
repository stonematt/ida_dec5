# import codecademylib
import pandas as pd

# create a data frame by passing in a library
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  # add Product Name and Color here
  'Product Name': ['t-shirt', 't-shirt', 'skirt','skirt'],
  'Color': ['blue', 'green', 'red','black'],
})

print df1
# list columns in the dataframe
print 'list of columns', list(df1)

# create data frame by passing in an array
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
	[3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=[
    'Store ID', 'Location', 'Number of Employees'
  ])

print df2

# more data to play with
df3 = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)

print df3

# select from a data frame
# select a column of values
employee_count = df2['Number of Employees']
print employee_count
print sum(employee_count)

# simple select a column when column name has no spaces
product_colors = df1.Color
print product_colors

# multiple columns
clinic_nw = df3[['clinic_north','clinic_west']]
print clinic_nw

# select rows from data frame
LAStore = df2.loc[1] #DF are zero-indexed arrays - this is the 2nd row
print LAStore
# print LAStore['Number of Employees']

# select multiple rows with list slicing
april_may_june = df3[3:]
print april_may_june

# select mulipble rows with query search
jan_clinics = df3[df3.month == 'January']
print jan_clinics

# query a data frame with AND (&) and OR (|)
march_april = df3[(df3.month == 'March') | (df3.month == 'April')]
print march_april

# using .isin method is simpler to query for items in a list
january_february_march = df3[df3.month.isin(['January', 'February','March'])]
print january_february_march
# combine isin with other criteria
q1_north_over75 = df3[df3.month.isin(['January', 'February','March']) & (df3.clinic_north > 75)]
print q1_north_over75

# reset the indexs of a data frame that was generated as a selction of a larger
# datafram so keep zero-indexed array correct. 
# reset_index() moves the old index to column "index" as a foriegn key to original
# drop=True drops the foreign key as "index" -- it is optional
df_three_rows = df.loc[[1, 3, 5]]
df_three_rows.reset_index(inplace=True, drop=True) #inplace modifies "this" dataframe without making a new one
print df_three_rows
# import codecademylib
import pandas as pd

orders = pd.read_csv('myfiles/d9-orders.csv')
print orders
products = pd.read_csv('myfiles/d9-products.csv')
print products

# merge 2 dataframes when the ID column of the join isn't explicit.
orders_products = pd.merge(orders, products.rename(columns={'id':'product_id'}))
print orders_products

# insted of remaming columns on the fly, name the columns to use for the join in the
# left (first) and right(second) tabels.  Use suffixes to make ther esulting column names clear

orders_products2 = pd.merge(
	orders,
	products,
	left_on='product_id',
	right_on='id',
	suffixes=['_orders','_products'])

print orders_products2

#######
# outer merge

store_a = pd.read_csv('myfiles/d9-store_a.csv')
print store_a
store_b = pd.read_csv('myfiles/d9-store_b.csv')
print store_b

# outer merge on the 2 data frames to keep rows from both.
store_a_b_outer= pd.merge(store_a, store_b, how='outer')
print store_a_b_outer


######
# left join to find iems in the second frame that are also in the first (left)

store_a_b_left = pd.merge(store_a, store_b, how='left')
print store_a_b_left

store_b_a_left = pd.merge(store_b, store_a, how='left')
print store_b_a_left

######
# combine (or concatenate) data frames if the columsn are the same

# dfc = pd.concat([df1, df2, df3])

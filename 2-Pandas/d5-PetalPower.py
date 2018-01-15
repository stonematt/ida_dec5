# import codecademylib
import pandas as pd

# load inventory from CSV file
inventory = pd.read_csv('myfiles/d5-inventory.csv')

#check out top 10 rows
#print inventory.head(10)

# top 10 rows are for the staten island location, put them in their own frame
staten_island = inventory.head(10)
#print staten_island

# customer makes a seed request for "seeds" sold in "booklyn"
seed_request = inventory[(inventory.location == 'Brooklyn') & (inventory.product_type == 'seeds')]
#print seed_request

# add a column to indicate whether item is in stock
inventory['in_stock'] = inventory.apply(lambda row:
                                       True
                                       if row.quantity > 0
                                       else False, axis=1)

# lambda function to combine row elements for a string description.
combine_lambda = lambda row: \
    '{} - {}'.format(row.product_type,
                     row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)  
  
print inventory.head(10)

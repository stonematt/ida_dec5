# import codecademylib
import pandas as pd

orders = pd.read_csv('myfiles/d1-15shoefly.csv')

print orders.head(5)

emails = orders.email

frances_palmer = orders[(orders.first_name == 'Frances') & (orders.last_name == 'Palmer')]

print frances_palmer

comfy_shoes = orders[orders.shoe_type.isin(['clogs','boots','ballet flats'])]
print comfy_shoes
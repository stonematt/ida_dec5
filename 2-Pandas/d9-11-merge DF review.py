# import codecademylib
import pandas as pd

visits = pd.read_csv('myfiles/d9-11-visits.csv',
                        parse_dates=[1])
checkouts = pd.read_csv('myfiles/d9-11-checkouts.csv',
                        parse_dates=[1])

print visits.head(2)
print checkouts.head(2)

v_to_c = visits.merge(checkouts)#.reset_index()

# make a column to hold the difference in time between vistiing the landing page and starting the checkout
v_to_c['time'] = v_to_c.checkout_time - v_to_c.visit_time

print v_to_c.head(2)
#show the average time on site before checkout:
print(v_to_c.time.mean())
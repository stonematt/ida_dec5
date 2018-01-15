"""
this won't run w/out the sales csv data but the hist call are correct
"""
# import codecademylib
from matplotlib import pyplot as plt
from lesson11script import sales_times1
from lesson11script import sales_times2

plt.hist(sales_times1, bins=30, alpha=0.4, normed=True, label="sales1")
#plot your other histogram here
plt.hist(sales_times2, bins=30, alpha=0.4, normed=True, label="sales2")

plt.legend(loc=2)

plt.show()
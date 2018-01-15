

"""
plt.fill_between(x_values, y_lower, y_upper, alpha=0.2) #this is the shaded error
plt.plot(x_values, y_values) #this is the line itself
"""

# import codecademylib
from matplotlib import pyplot as plt

months = range(12)
month_names = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
revenue = [16000, 14000, 17500, 19500, 21500, 21500, 22000, 23000, 20000, 19500, 18000, 16500]

y_lower = [ye * 0.9 for ye in revenue]
y_upper = [ye * 1.1 for ye in revenue]

#your work heree
 
plt.fill_between(months, y_lower, y_upper, alpha=0.2 )
plt.plot(months, revenue, label='Revenue Forecast')

plt.title('revenue and uncertainty')
plt.xlabel('Months')
plt.ylabel('Revenue ($)')
plt.legend()

ax = plt.subplot()
ax.set_xticks(range(len(months)))
ax.set_xticklabels(month_names)
 
plt.show()
# import codecademylib
import pandas as pd
from matplotlib import pyplot as plt

user_visits = pd.read_csv('myfiles/d6-8-page_visits.csv')

# print(user_visits.head(3))

click_source =  user_visits.groupby('utm_source').id.count().reset_index()
# print(click_source)

click_source_by_month = user_visits.groupby(['utm_source','month']).id.count().reset_index()

click_source_by_month_pivot = click_source_by_month.pivot(
	columns='month',
	index='utm_source',
	values='id').reset_index()

print(click_source_by_month_pivot)

click_source_by_month_chart = click_source_by_month.pivot(
	index='month',
	columns='utm_source',
	values='id').reset_index()

# print(click_source_by_month_chart)
print(list(click_source_by_month_chart)[1:])

month = range(len(click_source_by_month_chart['month']))
# plt.plot(month,click_source_by_month_chart['email'], label='email')

#use a loop to plot them all...
for dataset in list(click_source_by_month_chart)[1:]:
  plt.plot(month,click_source_by_month_chart[dataset], label=dataset)

# labels and legends
plt.xlabel('Month')
plt.ylabel('clicks')
plt.title('Click by source')
plt.legend() #uses labels on the plot, or specify in list [] also loc=1-10 for placement

# axis stuff
ax = plt.subplot()
ax.set_xticks(month)
ax.set_xticklabels(click_source_by_month_chart['month'])


plt.show()
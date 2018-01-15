# import codecademylib
import pandas as pd

ad_clicks = pd.read_csv('myfiles/d8-ad_clicks.csv')

#print(ad_clicks).head(5)

#quick count of clicks by source
clicks_by_utm_source = ad_clicks.groupby('utm_source').user_id.count().reset_index()
#print(clicks_by_utm_source)

#if the timestamp is not null, then it was an actual click, make a column to filter on clicks
ad_clicks['is_click'] = ~ad_clicks.ad_click_timestamp.isnull()                                     
#print(ad_clicks).head(5)

#group by the source and boolean
clicks_by_source = ad_clicks.groupby(['utm_source', 'is_click']).user_id.count().reset_index()
#print(clicks_by_source)

# make a pivot table to count and compare views clicks & source 
clicks_pivot = clicks_by_source.pivot(columns='is_click', index='utm_source', values='user_id').reset_index()
#print(clicks_pivot)

# calculate the percent who clicked the add by source
clicks_pivot['percent_clicked'] = clicks_pivot[True] / (clicks_pivot[False] + clicks_pivot[True])
print clicks_pivot

#show add volume by group
clicks_by_group = ad_clicks.groupby(['experimental_group','is_click']).user_id.count().reset_index()
#print(clicks_by_group)

group_pivot = clicks_by_group.pivot(columns='is_click',index='experimental_group',values='user_id').reset_index()
#print(group_pivot)

#calcuate percent of users who clicked each ad
group_pivot['percent_clicked'] = group_pivot[True] / (group_pivot[True] + group_pivot[False])
print(group_pivot)

print "Starting the A/B analysis by Day..."
#separate A and B clicks into 2 data frames
a_clicks = ad_clicks[ad_clicks.experimental_group == "A"]
b_clicks = ad_clicks[ad_clicks.experimental_group == "B"]

#for each data frame, calculate percent clicked by day
# use a function (DRY)...
def make_day_click_pivot(clicks):
  df_groupby = clicks.groupby(['day', 'is_click']).user_id.count().reset_index()
  df_pivot = df_groupby.pivot(columns='is_click', index='day', values='user_id').reset_index()
  df_pivot['percent_clicked'] = df_pivot[True] / (df_pivot[True] + df_pivot[False])
  return df_pivot
  

a_pivot = make_day_click_pivot(a_clicks)
print(a_pivot)

b_pivot = make_day_click_pivot(b_clicks)
print(b_pivot)


 
#I think there's a better way to do that....
# aggregate: group by (day, evalgrp, isclick) and count
ms_groupby = ad_clicks.groupby(['day', 'experimental_group', 'is_click']).user_id.count().reset_index()
# make pivot on is_click first
ms_pivot1 = ms_groupby.pivot_table(columns='is_click',index=['day','experimental_group'], values='user_id').reset_index()
# make % clicked
ms_pivot1['percent_clicked'] = ms_pivot1[True] / (ms_pivot1[True] + ms_pivot1[False])
# pivot on col=evalgrp, ind=day, val=%clicked...
ab_pivot = ms_pivot1.pivot(columns='experimental_group', values='percent_clicked', index='day').reset_index()
# add some interetsing columns
# daily winner
ab_pivot['advantage'] = ab_pivot.apply(lambda row:
                                      "A"
                                      if row['A'] - row['B'] > 0
                                      else "B", axis=1)
#total variance
ab_pivot['a_variance'] = ab_pivot['A'] - ab_pivot['B']
a_Advantage = ab_pivot.a_variance.mean() * 100

#show your work
print(ab_pivot)
# print "Advantage for A is ", a_Advantage
print "Average of advantage for A is %0.2f%%" % (a_Advantage)




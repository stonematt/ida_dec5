# import codecademylib
from string import lower
import pandas as pd

df = pd.DataFrame([
  ['JOHN SMITH', 'john.smith@gmail.com'],
  ['Jane Doe', 'jdoe@yahoo.com'],
  ['joe schmo', 'joeschmo@hotmail.com']
],
columns=['Name', 'Email'])

# Add columns and apply a function to determine value.  
# in this case apply lower() to the column Name and put it in a new column
df['Lowercase Name'] = df.Name.apply(lower)

print df

# Add columns using a lambda function
dfe = pd.read_csv('myfiles/2.d3.5.employees.csv')
# two options - 
# 1 lambda defined outside of this event (would be reusable elsewhere)
#get_last_name = lambda x: x.split()[-1]
#df['last_name'] = df.name.apply(get_last_name)

# 2 lambda defined on the fly for this transaction
dfe['last_name'] = dfe.name.apply(lambda x: x.split()[-1])
print 'lambda function'
print dfe[['name','last_name']].head(2)

# Add a column w/ a lambda function using more than one value on each row.
# in this case, total earned = wage * hours worked with overtime added
# don't forget axis=1
dfe['total_earned'] = dfe.apply(lambda row:
	row['hours_worked'] * row['hourly_wage']
	if row['hours_worked'] <= 40
	else (row['hourly_wage'] * 40) + (((row['hours_worked']) -40) * (row['hourly_wage'] * 1.5)), axis=1)
  
print dfe[['last_name', 'hours_worked','hourly_wage', 'total_earned']]

# rename columns 
# sets the columns to be this list (must do all of them)
#df.columns=['ID','Title','Category','Year Released','Rating']

# rename columns inplace
df.rename(inplace=True, columns={
  'name': 'movie_title'
})
import numpy as np

class_year = np.array([1967, 1949, 2004, 1997, 1953, 1950, 1958, 1974, 1987, 2006, 2013, 1978, 1951, 1998, 1996, 1952, 2005, 2007, 2003, 1955, 1963, 1978, 2001, 2012, 2014, 1948, 1970, 2011, 1962, 1966, 1978, 1988, 2006, 1971, 1994, 1978, 1977, 1960, 2008, 1965, 1990, 2011, 1962, 1995, 2004, 1991, 1952, 2013, 1983, 1955, 1957, 1947, 1994, 1978, 1957, 2016, 1969, 1996, 1958, 1994, 1958, 2008, 1988, 1977, 1991, 1997, 2009, 1976, 1999, 1975, 1949, 1985, 2001, 1952, 1953, 1949, 2015, 2006, 1996, 2015, 2009, 1949, 2004, 2010, 2011, 2001, 1998, 1967, 1994, 1966, 1994, 1986, 1963, 1954, 1963, 1987, 1992, 2008, 1979, 1987])


#calculating "mean" on a logical statement returns the percent that mean the statement
millennials = np.mean(class_year >= 2005)
print "millennials = np.mean(class_year >= 2005)"
print millennials

print "count"
print len(class_year)
print len(class_year[class_year >= 2005])

### Calculating means in a 2 Dimensional Array (2D array)
# five participants made daily responses for 3 days
# response is 1-10 for drowsiness
allergy_trials = np.array([[6, 1, 3, 8, 2], 
                           [2, 6, 3, 9, 8], 
                           [5, 2, 6, 9, 9]])

# average drowsiness overall
# mean of a 2 dimensional array (2D array)
total_mean = np.mean(allergy_trials)
print "total mean: ", total_mean

# average daily mean, is average of each row
# row is axis=1
trial_mean = np.mean(allergy_trials, axis=1)
print "trial mean:", trial_mean

# average for each patient (column)
# columns are axis=0
patient_mean = np.mean(allergy_trials, axis=0)
print "patient mean:", patient_mean

#sort an array to visually inspect for outliers:
temps = np.array([86, 88, 94, 85, 97, 90, 87, 85, 94, 93, 92, 95, 98, 85, 94, 91, 97, 88, 87, 86, 99, 89, 89, 99, 88, 96, 93, 96, 85, 88, 191, 95, 96, 87, 99, 93, 90, 86, 87, 100, 187, 98, 101, 101, 96, 94, 96, 87, 86, 92, 98,94, 98, 90, 99, 96, 99, 86, 97, 98, 86, 90, 86, 94, 91, 88, 196, 195,93, 97, 199, 87, 87, 90, 90, 98, 88, 92, 97, 88, 85, 94, 88, 93, 198, 90, 91, 90, 92, 92])

sorted_temps=np.sort(temps)
print sorted_temps

### also median:
print "median temp: ",  np.median(temps)
print "standard deviation: ", np.std(temps)
print "avg temp: ", np.mean(temps)
### also percentiles (quartile in this example..)
first_quarter = np.percentile(temps, 25)
third_quarter = np.percentile(temps, 75)

interquartile_range = third_quarter - first_quarter

print "1st Q: ", first_quarter
print "2nd Q: ", third_quarter
print "interQ: ", interquartile_range

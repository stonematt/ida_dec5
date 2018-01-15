import numpy as np

# make an array by hand from a list
test_1 = np.array([92, 94, 88, 91, 87])
# import and make an array from a CSV file
#test_2 = np.genfromtxt('test_2.csv', delimiter=',')

test_3 = np.array([87, 85, 72, 90, 92])

#perfom math on elements of the array rather than a loop
test_3_fixed = test_3 + 2
print test_3_fixed

test_1 = np.array([92, 94, 88, 91, 87])
test_2 = np.array([79, 100, 86, 93, 91])
test_3 = np.array([87, 85, 72, 90, 92])
test_3_fixed = test_3 + 2

## use range notation to select individual itesm or collection of items from an array
# arrays are zero indexed
jeremy_test_2 = test_2[3] # picks the 4th item in test 2
manual_adwoa_test_1 = test_1[1:3] #picks the 2nd and 3rd item in test 1

#find the averate of elements in the 3 arrays
# !! This REQUIRES that all arrays have the same number of elements
total_grade = test_1 + test_2 + test_3_fixed
final_grade = total_grade / 3
print final_grade

####
# two dimensional arrays are lists of arrays of equal lenght like this:
# pattern np.array([[list1],[list2],...])
tests = np.array([[92, 94, 88, 91, 87], 
                  [79, 100, 86, 93, 91],
                  [87, 85, 72, 90, 92]])
                  
####
# selectin from a 2D array, uses row/column notation, 
# wehere rows are "axis =1" and columns are "axis = 0"
# like a[row,column] where a is the array

# select an entire row or colum with a colun like:
# a[:,0] selects the entire first column (at posistion "0") and
# a[1,:] selects the entire send row

student_scores = np.array([[92, 94, 88, 91, 87],
                           [79, 100, 86, 93, 91],
                           [87, 85, 72, 90, 92]])

# students are Tanya, Manual, Adwoa, Jeremy, Cody
tanya_test_3 = student_scores[2,0]
# pull all of cody scores by pulling all of scores in the last column
cody_test_scores = student_scores[:,-1]

porridge = np.array([79, 65, 50, 63, 56, 90, 85, 98, 79, 51])

# select samples that are "cold", i.e. under 60
cold = porridge[porridge < 60]
print cold

# select the hot ones
hot = porridge[porridge > 80]
print len(hot)

#and the ones that are "just right..." using a logical condition
just_right = porridge[(porridge > 60) & (porridge < 80) ]
print just_right

temperatures = np.genfromtxt('myfiles/3/d1-temperature_data.csv', delimiter=',')
#daily times @ 0:00, 6:00, 12:00, 18:00
print temperatures

# sensor was miscalibrated, adjust by +3 degrees
temperatures_fixed = temperatures + 3
print temperatures_fixed

# print monday
monday_temperatures = temperatures_fixed[0,:]
print monday_temperatures

# print Th/Fr @ 6:00
thursday_friday_morning = temperatures_fixed[-2:,1]
print thursday_friday_morning

#save extremes
temperature_extremes = temperatures_fixed[(temperatures_fixed < 50) | (temperatures_fixed > 60)]
print temperature_extremes
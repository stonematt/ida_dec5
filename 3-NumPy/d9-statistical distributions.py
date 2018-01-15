# import codecademylib
import numpy as np
from matplotlib import pyplot as plt

# generate random dataset with normal distribution
# np.random.normal(loc, scale, size=#)
# loc = mean (location of center)
# scale = standard deviation
# Brachiosaurus
b_data = np.random.normal(6.7, 0.7, size=1000)


# generate sample set the shows probability of an 
# outcome
# np.random.binomial(n, p, size=#)
# n = number of samples or attempts
# p = probablity of sucess
emails = np.random.binomial(500, 0.05, size=10000)

#plt.hist(emails)
plt.hist(emails, normed=True)

plt.xlabel('Number of email responses')
plt.ylabel('Frequency')

plt.show()

"""
Remember that taking the mean of a logical statement 
will give us the percent of values that satisfy our logical statement"""

# if 5% are expected to open an email (25 of 500),
# what is the probability that no one will?
no_emails = np.mean(emails == 0)
print no_emails

#target response rate is 8%
target = 0.08
#target of 500 recipeints
respondents = 500 * target
#probability that this would have 
#happened anyway
b_test_emails = np.mean(emails >= respondents)
print b_test_emails

print "likelihood that %s or more would have responded previously is %0.2f%%" % (str(respondents), b_test_emails * 100)



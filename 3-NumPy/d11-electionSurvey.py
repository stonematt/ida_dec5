# import codecademylib
import numpy as np
from matplotlib import pyplot as plt

survey_responses = ['Ceballos', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos','Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos',
                    'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Ceballos', 'Ceballos', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Kerrigan', 'Ceballos']

# make survey responses in to a numpy array.
responses = np.array(survey_responses)
# how many said "ceballos"?
total_ceballos=len(responses[responses == 'Ceballos'])
print 'total ceballos: ', total_ceballos

# percent of responses who said Cebellos
percentage_ceballos = np.mean(responses == "Ceballos")
print '% ceb from array: ', percentage_ceballos


# in real election, 54% voted cebellos, is the survey
# prediction of 47% reasonable?

total_responses = float(len(responses))
print 'total survey responses: ', total_responses
# survey results: 47% of 70 resondents picked Ceballos
# reality: 54% of 10,000 voters voted for Ceballos
# make a binomial distribution to see if that fits our survey set
# divide by N to convert to percentage
possible_surveys = np.random.binomial(total_responses, \
                                      percentage_ceballos, \
                                      size=10000) / total_responses
# print 'possible surveys out: ', possible_surveys[0:5]

## 
# plt.hist(possible_surveys, bins=20, range=(0,1), label='possible ceb', normed=True)
# plt.xlabel('% for Ceballos')
# plt.ylabel('Frequency')
# plt.legend()
# plt.show()

# how likely did the survey predict that
# Ceballos would loose, (i.e. get < 50%)
ceballos_loss_surveys = np.mean(possible_surveys < 0.5)
print "survey suggests Ceballos had %0.2f%% chance of losing" % (ceballos_loss_surveys * 100)


# 33 (or 70) responses aren't very many
# what if the survey had suveyed 7000 instead?
large_survey = np.random.binomial(7000.0, percentage_ceballos, size=10000) / 7000.0
print large_survey[0:5]

# compare Ceballos loss probability from the large survey
ceballos_loss_new = np.mean(large_survey < 0.5)
print "large survey suggests Ceballos had %0.2f%% chance of losing" % (ceballos_loss_new * 100)

# another test: we know taht 54% voted Ceballos in the true election.
# assume we used that as P, and surveyed a large popualtion, liek 7,000
# how how often would the survey precit Ceballows to lose?
large_survey2 = np.random.binomial(7000.0, 0.54, size=10000) / 7000.0
print "large_survey2", large_survey2[0:5]

# compare Ceballos loss probability from the large survey
ceballos_loss_2 = np.mean(large_survey2 < 0.5)
print "large survey suggests Ceballos had %0.2f%% chance of losing" % (ceballos_loss_2 * 100)

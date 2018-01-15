import random
import numpy as np
from matplotlib import pyplot as plt

roll1 = np.array([])
roll2 = np.array([])

def plot2d6(dice):
  # print dice
  plt.hist(dice, label='2d6')
  plt.legend()
  
  # ax = plt.subplot()
  # ax.set_xticks(range(1,13))
  # ax.set_xticklabels(range(1,13))
  
  plt.show()

for i in range(10000):
  fistdice = random.randint(1,6)
  roll1=np.append(roll1,fistdice)
  seconddice = random.randint(1,6)
  roll2=np.append(roll2,seconddice)
  # print i, fistdice, seconddice
  two_d_six = roll1 + roll2
  # print two_d_six
  # if i == 5:
  #  plot2d6(two_d_six)
  # elif i % 50 == 0:
  #   plot2d6(two_d_six)

plot2d6(two_d_six)
  

# import codecademylib
import numpy as np
from matplotlib import pyplot as plt

sunflowers = np.genfromtxt('myfiles/3/d9-sunflower_heights.csv',
                           delimiter=',')

# Calculate mean and std of sunflowers here:
sunflowers_mean = np.mean(sunflowers)
sunflowers_std = np.std(sunflowers)

# Calculate sunflowers_normal here:
# generate dataset of normal distribution for 
# comparison to observed.
sunflowers_normal = np.random.normal(\
                         sunflowers_mean, \
                         sunflowers_std, \
                         size=50000)

plt.hist(sunflowers,
         range=(11, 15), linewidth=2,
        label='observed', normed=True, alpha=0.3)
plt.hist(sunflowers_normal,
         range=(11, 15), histtype='step', linewidth=2,
        label='normal', normed=True)
plt.legend()
plt.show()

# Calculate probabilities here:

# 10% of sunflowers fail to bloom.  make a dataset
# to use for calcualting probablilities...
experiments = np.random.binomial(200, 0.1, size=5000)

# what percent of experements has <20 that fail to bloom
prob = np.mean(experiments < 20)
print prob


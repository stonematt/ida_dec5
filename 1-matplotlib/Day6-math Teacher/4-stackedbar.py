# import codecademylib
from matplotlib import pyplot as plt
import numpy as np

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
As = [6, 3, 4, 3, 5]
Bs = [8, 12, 8, 9, 10]
Cs = [13, 12, 15, 13, 14]
Ds = [2, 3, 3, 2, 1]
Fs = [1, 0, 0, 3, 0]

x = range(5)

c_bottom = np.add(As, Bs) #numpy addes arrays to make the stacked bar base.
d_bottom = np.add(c_bottom, Cs)
f_bottom = np.add(d_bottom, Ds)

#create your plot here
plt.figure(figsize=(10,8))

plt.bar(range(len(unit_topics)), As, label='A')
plt.bar(range(len(unit_topics)), Bs, bottom=As, label='B')
plt.bar(range(len(unit_topics)), Cs, bottom=c_bottom, label='C')
plt.bar(range(len(unit_topics)), Ds, bottom=d_bottom, label='D')
plt.bar(range(len(unit_topics)), Fs, bottom=f_bottom, label='F')

ax = plt.subplot()
ax.set_xticks(range(len(unit_topics)))
ax.set_xticklabels(unit_topics)

# Standard Plot Elements
plt.title('Grade distribution')
plt.xlabel('Unit')
plt.ylabel('Number of Students')
plt.legend()

plt.savefig('my_stacked_bar.png')

plt.show()
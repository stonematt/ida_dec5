# import codecademylib
from matplotlib import pyplot as plt

unit_topics = ['Limits', 'Derivatives', 'Integrals', 'Diff Eq', 'Applications']
middle_school_a = [80, 85, 84, 83, 86]
middle_school_b = [73, 78, 77, 82, 86]

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

#school_a_x = [0.8, 2.8, 4.8, 6.8, 8.8]
#school_b_x = [1.6, 3.6, 5.6, 7.6, 9.6]

# Make your chart here

school_a_x = create_x(2, 0.8, 1, len(middle_school_a))
school_b_x = create_x(2, 0.8, 2, len(middle_school_b))

plt.figure(figsize=(10,8))
ax = plt.subplot()

plt.bar(school_a_x, middle_school_a, label='Middle School A')
plt.bar(school_b_x, middle_school_b, label='Middle School B')

plt.axis([0,12,70,90])
#plt.set_ylim([70,90])

middle_x = [ (a + b) / 2.0 for a, b in zip(school_a_x, school_b_x)]
ax.set_xticks(middle_x)
ax.set_xticklabels(unit_topics)

# Standard Plot Elements
plt.title('Test Averages on Different Units')
plt.xlabel('Unit')
plt.ylabel('Test Average')
plt.legend()

plt.savefig('my_side_by_side.png')

plt.show()
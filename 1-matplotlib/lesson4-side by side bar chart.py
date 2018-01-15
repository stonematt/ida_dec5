# import codecademylib
from matplotlib import pyplot as plt

def create_x(t, w, n, d):
    return [t*x + w*n for x in range(d)]

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
sales1 =  [91, 76, 56, 66, 52, 27]
sales2 = [65, 82, 36, 68, 38, 40]
  
# Use create_x to make store1_x
store1_x = create_x(2, 0.8, 1, len(sales1))
plt.bar(store1_x, sales1)


# Use create_x to make store2_x
store2_x = create_x(2, 0.8, 2, len(sales2))
plt.bar(store2_x, sales2)

ax = plt.subplot()
# ax.set_xticks([i  for i in range(len(sales1)*2) if i % 2 == 1])
# x-axis labels for side by side 2 series bar chart (hard coded for 2 series)
ax.set_xticks([i + 0.5  for i in range(len(sales1)*2) if i % 2 == 1])
# ax.set_xticks([i   for i in range(len(sales1)*2)])
# ax.set_xticklabels(drinks)

plt.show()



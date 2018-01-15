# import codecademylib
from matplotlib import pyplot as plt

drinks = ["cappuccino", "latte", "chai", "americano", "mocha", "espresso"]
ounces_of_milk = [6, 9, 4, 0, 9, 0]
error = [0.1*e for e in ounces_of_milk]

# Plot the bar graph here

#includes error bars w/ yerr and capsize
plt.bar(range(len(ounces_of_milk)), ounces_of_milk, 
        label="ounces of milk", yerr=error, capsize=5) 

plt.title('Milk in drinks')
plt.xlabel('Drinks')
plt.ylabel('Milk (oz)')
plt.legend()

ax = plt.subplot()
ax.set_xticks(range(len(drinks)))
ax.set_xticklabels(drinks)



plt.show()
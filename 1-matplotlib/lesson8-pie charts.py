# import codecademylib
from matplotlib import pyplot as plt
import numpy as np

payment_method_names = ["Card Swipe", "Cash", "Apple Pay", "Other"]
payment_method_freqs = [270, 77, 32, 11]

#make your pie chart here

plt.pie(payment_method_freqs, 
        labels=payment_method_names,
        autopct='%d%%') #'%d%%' is rounded to int or %0.2f%% for 2 decimal places
plt.axis('equal') # makes a pie chart round...



# Standard Plot Elements
plt.title('Payment Methods')
#plt.xlabel('Drinks')
#plt.ylabel('Milk (oz)')
# plt.legend(payment_method_names)




plt.show()
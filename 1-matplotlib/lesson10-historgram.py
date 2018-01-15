# import codecademylib
from matplotlib import pyplot as plt
from lesson10script import sales_times

#create the histogram here

plt.hist(sales_times, bins=20) #bins= count of bins, also range=(min,max)
#plt.hist(dataset, bins=20, alpha=0.5) #plot histograms of mulitple populations, alpha for transparency

# Standard Plot Elements
plt.title('sales busy time')
plt.xlabel('Time')
plt.ylabel('Count of Sales')
#plt.legend()


plt.show()
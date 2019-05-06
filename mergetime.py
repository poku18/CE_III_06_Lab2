import random
from time import time
import matplotlib.pyplot as plt
from lab2 import mergeSort

n = 1000
i = 0
time_merge_sort=[]
sizeArray = []

for i in range(n, n * 20, n):
        sizeArray.append(i)
        randomvalues = random.sample(range(i), i)
        startTime = time()
        mergeSort(randomvalues)
        endTime = time()
        totalTime = endTime - startTime
        time_merge_sort.append(totalTime)
        print(totalTime, "for size", i)

# draw graph for time vs size for the algorithm
plt.plot(sizeArray, time_merge_sort, label = 'Merge Sort')
plt.legend(loc = 'upper center', shadow = True, fontsize = 'large')
plt.show()

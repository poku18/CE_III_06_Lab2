from lab2 import insertionSort
import random
from time import time
import matplotlib.pyplot as plt

n = 1000
i = 0
time_insertion_sort = []
sizeArray = []

#timing insertion sort
for i in range(n, n * 11, n):
	sizeArray.append(i)
	randomvalues = random.sample(range(i), i)
	startTime = time()
	insertionSort(randomvalues)
	endTime = time()
	totalTime = endTime - startTime
	time_insertion_sort.append(totalTime)
	print(totalTime, "for size", i)

# draw graph for time vs size for the algorithm
plt.plot(sizeArray, time_insertion_sort, label = 'Insertion Sort')
plt.legend(loc = 'upper center', shadow = True, fontsize = 'large')
plt.show()


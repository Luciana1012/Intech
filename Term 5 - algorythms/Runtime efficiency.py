#Runtime efficiency for insertion, merge, selection, quicksort, bubblesort for arrays with 10, 100,  1000, 100000 and 1 million numbers.

#Insertiont sort

import time
import numpy as np

# def insertionSort(unsortedList):

#     sortedList = []
#     while len(unsortedList) != 0:
#         sortedList.append(min(unsortedList)) # change this to min or max depending on descending or ascending
#         unsortedList.remove(min(unsortedList))


# start_time = time.time()
# arr = list(np.random.randint(1,100,10))
# insertionSort(arr)
# print("it took (seconds):", time.time() - start_time)

#print(arr)
#1,100,1000 = 0.07579684
#1,100,10000 = 7.03081345
#1,100,10 = 0.000996828

#Merge
# mergeSortedArray = []
# def mergeSort(array):
#     if len(array) > 1:
#         mid = len(array) // 2 # do double divide to round to nearest integer

#          # Diving  the array into 2
#         leftSide = array[:mid]
#         rightSide = array[mid:]

#          # we call the method again "recursively" until there's 1 element left in each array
#         mergeSort(leftSide)
#         mergeSort(rightSide)

#         indexLeftSide = 0
#         indexRightSide = 0
#         indexSortedArray = 0

#         while indexLeftSide < len(leftSide) and indexRightSide < len(rightSide):
#             if leftSide[indexLeftSide] < rightSide[indexRightSide]:
#                 array[indexSortedArray] = leftSide[indexLeftSide]
#                 indexLeftSide += 1
#             else:
#                 array[indexSortedArray] = rightSide[indexRightSide]
#                 indexRightSide += 1
#             indexSortedArray += 1
#         while indexLeftSide < len(leftSide) :
#                 array[indexSortedArray] = leftSide[indexLeftSide]
#                 indexLeftSide += 1
#                 indexSortedArray += 1

#         while indexRightSide < len(rightSide):
#             array[indexSortedArray] = rightSide[indexRightSide]
#             indexRightSide += 1
#             indexSortedArray += 1

# start_time = time.time()
# arr = list(np.random.randint(1,100,10000))
# mergeSort(arr)
#print("it took (seconds):", time.time() - start_time)

#1,100,1000 = 0.0059831
#1,100,10000 = 0.0907561
#1,100,10 = 0.0

# SELECTION SORT
# Traverse through all array elements
# def selectionSort(array):
#     for i in range(len(array)):

#         currentPosition = i 
#         for j in range(i + 1, len(array)):
#             if array[currentPosition] > array[j]:
#                 currentPosition = j

#         array[i] = array[currentPosition]
#         array[currentPosition] = array[i]

# start_time = time.time()
# arr = list(np.random.randint(1,100,10000))
# selectionSort(arr)
# print("it took (seconds):", time.time() - start_time)

#1,100,1000 = 0.0937488079
#1,100,10000 = 10.444239616
#1,100,10 = 0.0009980201

#BubbleSort
# def bubbleSort(unsortedArray):
#     for i in range(0, len(unsortedArray)):
#         for j in range(0, len(unsortedArray) - 1):
#           if unsortedArray[j] > unsortedArray[j+1]:
#             tempStorage = unsortedArray[j]
#             unsortedArray[j] = unsortedArray[j+1]
#             unsortedArray[j+1] = tempStorage
# start_time = time.time()
# arr = list(np.random.randint(1,100,10))
# bubbleSort(arr)
# print("it took (seconds):", time.time() - start_time)

#1,100,1000 = 0.344135284
#1,100,10000 = 32.387605
#1,100,10 = 0.0009970664

#quickSort
def quickSort(unsortedArray):
    less = [] 
    equal = []
    greater = []
    if len(unsortedArray) > 1:
        pivot = unsortedArray[0]
        for element in unsortedArray:
            if element < pivot:
                less.append(element) 
            elif element == pivot:
                equal.append(element)
            elif element > pivot:
                greater.append(element)
        return quickSort(less)+equal+quickSort(greater)
    else:
        return unsortedArray
start_time = time.time()
arr = list(np.random.randint(1,100,1000))
quickSort(arr)
print("it took (seconds):", time.time() - start_time)
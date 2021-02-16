# Function to do insertion sort
def insertionSort():

    sortedList = []
    unsortedList = [5,3,1,4,6]
    while len(unsortedList) != 0:
        sortedList.append(min(unsortedList)) # change this to min or max depending on descending or ascending
        unsortedList.remove(min(unsortedList))
        print("unsorted is", unsortedList)
        print("sorted is", sortedList)

# insertionSort()

mergeSortedArray = []
def mergeSort():
    if len(array) > 1:
         mid = len(array) // 2 # do double divide to round to nearest integer

         # Diving  the array into 2
         leftSide = array[:mid]
         rightSide = array[mid:]

         # we call the method again "recursively" until there's 1 element left in each array
         mergeSort(leftSide)
         mergeSort(rightSide)

         indexLeftSide = 0
         indexRightSide = 0
         indexSortedArray = 0

        while indexLeftSide < len(leftSide) and indexRightSide < len(rightSide)
            if leftSide[indexLeftSide] < rightSide[indexRightSide]:
                mergeSortedArray.append(leftSide[indexLeftSide])
                indexLeftSide += 1
            else:
                mergeSortedArray.append(rightSide[indexRightSide])
                indexRightSide += 1

        while indexLeftSide < len(rightSide) :
                array[indexSortedArray] = leftSide[indexLeftSide]
                indexLeftSide += 1
                indexSortedArray += 1

        while indexRightSide < len(righSide):
            array[indexSortedArray] = rightSide[indexRightSide]
            indexRightSide += 1
            indexSortedArray += 1

arr = [12, 11, 13, 5, 6, 7]
print("Given array is")
print(arr)
mergeSort(arr)
print("Sorted array is: ")
print(arr)


         # Copy data to temp arrays L[] and R []
        #while i < len(leftSide) and j < len(rightSide)
        #    if leftSide[indexLeftSide] < rightSide[indexRightSide]:
        #       array[sortedListIndex] = leftSide[indexLeftSide]
        #       indexLeftSide += 1
        #  else:
        #     arr[k] = R[i] 

# SELECTION SORT

array = [64, 25, 12, 22, 11]

# Traverse through all array elements
for i in range(len(array)):

    currentPosition = i 
    for j in range(i + 1, len(array)):
        if array[currentPosition] > array[j]:
            currentPosition = j

    array[i] = array[currentPoisiton]
    array[currentPosition] = array[i]

print(array, "sorted")


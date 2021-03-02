def binarySearch(array, startingIndex, endingIndex, x):
        if startingIndex == endingIndex: #we didn't found the element x
            return -1
        midPointIndex = (startingIndex + endingIndex) // 2
        midPointValue = array[midPointIndex]
        if x == midPointValue:
            return midPointIndex
        elif x < midPointValue:
            return binarySearch(array, 0, midPointIndex, 0) 
        elif x > midPointValue:
            return binarySearch(array, midPointIndex, len(array) - 1, x)

a = [1,2,3,4,5,6,7,8,9,10]
print (binarySearch(a,0, len(a)-1, 8))
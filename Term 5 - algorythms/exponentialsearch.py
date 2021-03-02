from binary import binarySearch 

def exponentialSearch(array, x):
    startingIndex = 0 
    endingIndex = 0
    if array[startingIndex] == x:
        return startingIndex
    else:
        endingIndex +=1
    while endingIndex < len(array) and array[endingIndex] <= x:
        endingIndex *= 2
    return binarySearch(array, startingIndex, endingIndex, x)


a = [1,2,3,4,5,6,7,8,9,10]
print (exponentialSearch(a, 6))
#def bubbleSort(9,6,8,4):
#    for i from 0 to size of array:
#        for j from 0 to size of array -1: #why do we do -1 here?
#            If unsortedArray at j  is more than unsortedArray at j+1
#            unsortedArray at j = unsortedArray at j+1
#            unsortedArray at j+1 = unsortedArray at j



#def bubbleSort(9,6,8,4):
def bubbleSort(unsortedArray):
    for i in range(0, len(unsortedArray)):
        for j in range(0, len(unsortedArray) - 1):
          if unsortedArray[j] > unsortedArray[j+1]:
            tempStorage = unsortedArray[j]
            unsortedArray[j] = unsortedArray[j+1]
            unsortedArray[j+1] = tempStorage
unsortedArray = [9,6,8,5,4]
bubbleSort(unsortedArray)        
print(unsortedArray)

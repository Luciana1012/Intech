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

unsortedArray = ['r', '#','*','z','a','m','l','j']
sortedArray = quickSort(unsortedArray)        
print(sortedArray)

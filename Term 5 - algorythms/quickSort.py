#Declare 3 empty arrays (one called less, one called equal, another called more)
#If size of unsortedArray is more than 1:
#	set pivot variableas first element
#	for each element in unsortedArray:
#		If element less than pivot:
#			Add element to less array
#		Else if element equal to pivot
#			Add element to equal array
#		Else if element more than pivot:
#			Add element to more array
#	Return quickSort(less array).extend(equal array).extend(sort(greater array))

#Else:
#	Return unsortedArray

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

unsortedArray = [3,10,1,9,6,8,5,4]
sortedArray = quickSort(unsortedArray)        
print(sortedArray)




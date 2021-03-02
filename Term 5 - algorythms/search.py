def linearSearch(array, x):
    index = 0
    for element in array:
        if element == x:
            return index
        index +=1
    return -1

a = [1,2,3,4,5,6,7,8,9,10]
print(linearSearch(a, 4))


#x = 0
#    while loop
#    if x < 100:
#        x++
#        print(x)
#    else print(x)
#return 0

#x = 0
#while(x < 100):
#	x+= 1
#	print(x)

#return 0

#x = 0
#while(True):
#	if(x < 100)
#		x+= 1
#		print(x)
#	else
#	print(x)
#	return 0


#no ; para python
#: dsps de 1) if else, 2)  loops y 3) funciones declaradas :

#Task implement the following flowchat
import math

array = [1,2,3,4,5,6,7,8,9,10]
target = 8
def linearSearch(array, x, currentPosition):
    index = currentPosition
    while index < len(array):
        if array[index] == x:
            return index
        index +=1
    return -1

def jumpSearch(array, target):
	x = int (math.sqrt(len(array)))
	currentPosition = 0
	while(array[currentPosition] < target):
		if currentPosition < len(array):
			currentPosition = currentPosition + x
		elif currentPosition > len(array):
			return -1
	currentPosition = currentPosition - x 
	return linearSearch(array, target, currentPosition)
print(jumpSearch(array,target))
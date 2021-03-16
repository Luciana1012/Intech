import unittest

def sum(array):
    """
    This function will display the sum of all elements added together.
    Input: array (list) array of numbers
    Output: return the sum of all numbers in array.
    """

    sumValue = 0
    for element in range(1,len(array)+1):
        sumValue += element
    return sumValue


class Test1 (unittest.TestCase): #This can be any name!!
    def testcasefirst(self): #This can be any name!!
        #a = 80
        #self.assertTrue(a, 80)
        #b = "testing" 
        #self.assertFalse(a, b)
        #using self.assertXXXX() write:
        #assign the value 80 to variable called "a", test that a  is equal to 80
        #assign the value "testing" to variable called "b", test that b is not equal to a
        # assign tha array [1,2,3,4] to variable "c" and [2,3,4] to variable "d"
        #           test that c is not equal to d 
        # test that second element of C is equal to first element of d
        # test that last element of c is equal to last element of d
        # assign the array [1,2,3,4] to a variable "e", test that c is equal to e
        #pass
        #self.assertEquals(3, 4)
        #EXAMPLE ONLY!!
        #self.assertTrue(item1 == item2) or (item1 != item2)
        #self.assertFalse(item1 == item2) or (item1 != item2)
        #self.assertEquals(item1, item2) <----- (item1 == item2)
    
#unittest.main()

        a = 80
        self.assertTrue(a == 80)
        b = "testing" 
        self.assertFalse(a == b)
        c = [1,2,3,4]
        d = [2,3,4]
        self.assertFalse(c == d)
    
        self.assertEquals(c[1], d[0])
        self.assertEquals(c[-1], d[-1])
        e = [1,2,3,4]
        self.assertEquals(c, e)

    def testSumFunction(self):
        array = [1,3,5,7]
        sum(array)
        self.assertEquals(sum([1,3,5,7]), 16)
        self.assertEquals(sum([2,4,6,8]), 20)
        self.assertEquals(sum([10,50,30,10]), 100)
unittest.main()

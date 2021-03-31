import unittest

def sum(array):
    """
    This function will display the sum of all elements added together.
    Input: array (list) array of numbers
    Output: return the sum of all numbers in array.
    """

    sumValue = 0
    for element in range(0,len(array)):
        sumValue += array[element]
    return sumValue

#The range() function returns a sequence of numbers, starting from 0 by default, 
# and increments by 1 (by default), and stops before a specified number.
#range(start -OPTIONAL, stop BEFORE -REQUIRED, stepINCREMENTATION PARAMETER -OPTIONAL)

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
        
        
        #self.assertTrue(sum([1,3,5,7]), 16)
        #self.assertEquals(sum([1,3,5,7]) == 16) 
        #self.assertFalse(sum([1,3,5,7]) != 16)

        #self.assertEquals(sum([2,4,6,8]), 20)

        #self.assertTrue(sum([10,50,30,10]) == 100)

    
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
        self.assertEquals(sum(array), 16)
        self.assertEquals(sum([2,4,6,8]), 20)
        self.assertEquals(sum([10,50,30,10]), 100)
    
unittest.main()

def calculateTax(income):
    """
    This function calculate tax value based on income bracket.
    Those income between 0 and 10,000 will pay 0%
    10,001 - 40,000 will pay 5%
    40,001 - 50,000 will pay 10%
    50,001 - 70,000 will pay 15%
    above 70,000 will pay 20%
    Input: income (int) 
    Output: return the amount of tax needs to be paid
    """

    if (income > 0 and income <= 10000) or (income <= 0):
        return 0
    elif income > 10000 and income <= 40000:
        return 0.05 * income
    elif income > 40000 and income <= 70000:
        return 0.1 * income
    elif income > 70000 and income <= 100000:
        return 0.15 * income
    else:
        return 0.2 * income

class Test1 (unittest.TestCase): 
    def testcasefirst(self):
        self.assertTrue(calculateTax(5000) == 0)
        self.assertEquals(calculateTax(10000), 0)
        self.assertTrue(calculateTax(17000) == 850)
        self.assertTrue(calculateTax(40000) == 2000)
        self.assertEquals(calculateTax(-1000), 0)
        self.assertTrue(calculateTax(0) == 0)
        self.assertTrue(calculateTax(-40000) == 0)

unittest.main()
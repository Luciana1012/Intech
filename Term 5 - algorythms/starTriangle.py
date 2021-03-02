#    def starTriangle(numberOfLine)
#    numberOfLine = 9
#    numberOfLine = 1("*")
#    numberOfLine = 2("*+**")

#    print ()

def starTriangle(numberOfLine):
    currentLine = 1
    for x in range(0, numberOfLine):
        numberOfStars = currentLine + (x * 2)
        print (" " * (numberOfLine-x), "x" * numberOfStars)

starTriangle(10)
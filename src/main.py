n = 5

def alphabet(n, line):
    alphabetArray = []
    for i in range(n, n - line, -1): 
        #print("i = ", i)
        char = chr(96 + i)
        #print("char = ", char)
        alphabetArray.append(char)
    return alphabetArray

def lineDraw(n, line, width):
    halfList = alphabet(n, line)
    firstHalfList = halfList[:-1]
    #print("firstHalfList = ", firstHalfList)
    secondHalfList = halfList[::-1]
    #print("secondHalfList = ", secondHalfList)
    fullList = firstHalfList + secondHalfList
    #print("fullList = ", fullList)
    addFullList = '-'.join(fullList)
    #print("addFullList = ", addFullList)
    return addFullList.center(width, '-')

def printRangoli(n):
    width = 4 * n - 3
    # Top Part
    for line in range(1, n + 1):
        print(lineDraw(n, line, width))
    # Bottom Part
    for line in range(n - 1, 0, -1):
        print(lineDraw(n, line, width))

printRangoli(n)

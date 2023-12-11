def checkUpDown(matrix, i, j):
    up = ''
    down = ''
    if i > 0:
        up = matrix[i-1][j]

    if i < len(matrix)-1:
        down = matrix[i+1][j]

    if up != '' and up != '.' and not up.isdigit():
        return True
    if down != '' and down != '.' and not down.isdigit():
        return True

    return False

def getCellMult(matrix, i, j, asterisks):
    key = ""
    foundAsterisks = set()
    if matrix[i][j] == "*":
        key = str(i) + "," + str(j)
        foundAsterisks.add(key)

    if i > 0 and matrix[i-1][j] == "*":
        key = str(i-1) + "," + str(j)
        foundAsterisks.add(key)

    if i < len(matrix)-1 and matrix[i+1][j] == "*":
        key = str(i+1) + "," + str(j)
        foundAsterisks.add(key)

    if key != "" and key not in asterisks:
        asterisks[key] = []

    return foundAsterisks

def getPartNumbersMulti(matrix):
    sum = 0
    asterisks = {}
    numCols = len(matrix[0])-1
    for row in range(len(matrix)):
        foundAsterisks = set()
        strNum = ""
        # iterate through columns
        for column in range(len(matrix[0])):
            val = matrix[row][column]
            # print("val:", val)
            asterisksCurrent = getCellMult(matrix, row, column, asterisks)
            foundAsterisks.update(asterisksCurrent)
            # print("row:", row, "column:", column, "asterisksCurrent:", asterisksCurrent, " foundAsterisks:", foundAsterisks, "asterisks:", asterisks)

            if val.isdigit():
                strNum += val
            if not val.isdigit() or column == numCols:
                newNum = getValue(strNum)
                strNum = "" # Reset string
                if newNum > 0:
                    for key in foundAsterisks:
                        if key in asterisks:
                            for num in asterisks[key]:
                                # print('num:{0} * newNum:{1}'.format(num, newNum))
                                sum += num * newNum
                            asterisks[key].append(newNum)
                        else:
                            asterisks[key] = [newNum]

                foundAsterisks = asterisksCurrent
    return sum


def getPartNumbersSum(matrix):
    sum = 0
    # iterate through rows
    for row in range(len(matrix)):
        strNum = ''
        flagSpecialChar = False
        # iterate through columns
        for column in range(len(matrix[0])):
            val = matrix[row][column]
            # print("row:", row, "column:", column, " val:", val, " flagSpecialChar:", flagSpecialChar)
            if val.isdigit():
                strNum += val
                flagSpecialChar = flagSpecialChar or checkUpDown(matrix, row, column)
            else:
                if val != '.':
                    sum += getValue(strNum)
                    # print("  GetNum(SpecialChar):", strNum)
                    strNum = "" # Reset string
                    flagSpecialChar = True
                else:
                    flagSpecialCharUpDown = checkUpDown(matrix, row, column)
                    if flagSpecialChar or flagSpecialCharUpDown:
                        sum += getValue(strNum)
                        # print("  GetNum(.):", strNum)
                    strNum = "" # Reset string                    
                    flagSpecialChar = flagSpecialCharUpDown

    return sum

def getValue(stringNum):
    if stringNum == "":
        return 0
    else:
        return int(stringNum)

def getRow(matrix, line):
    row = []
    for c in line:
        row.append(c)

    return row

def getSum(file):
    Lines = file.readlines()

    # Create Matrix
    matrix = []
    i = 0
    for line in Lines:
        matrix.append(getRow(matrix, line.strip()))

    # print('matrix: {0}'.format(matrix))

    print('1: {0}'.format(getPartNumbersSum(matrix)))
    print('2: {0}'.format(getPartNumbersMulti(matrix)))

input = open("inputDay3.txt", "r") 
getSum(input)
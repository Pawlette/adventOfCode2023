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
    #return sum

input = open("inputDay3.txt", "r") 
getSum(input)
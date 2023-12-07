# Read line by line
# Use i: start, j: end
# Walk from start and end to find num or reach contrary index, find num, extract.
# If i == j, then same num... ab7cd >> 77
### Walkthrough: aaaa7b
'''
 i = 0 a
 j = 5 b
 No number, add i, dec j

 i = 1 a
 j = 4 7

 Num j, stop moving j

 i = 2 a
 j = 4 7
 No num, move i

 i = 3 a
 j = 4 7
 No num, move i

 i = 4
 >> i == j
 Same num

 return 77
'''
# Add nums
numbers = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def getNumber(char, word, reverse):
    if isNumber(char):
        return char
    
    for key in numbers:
        if key in word:
            return numbers[key]
        if key in reverse:
            return numbers[key]
    
    return ''

def isNumber(char):
    try: 
        int(char)
    except ValueError:
        return False
    else:
        return True

def extractNumChars(line):
    i = 0
    j = len(line.strip()) - 1
    num1 = ''
    num2 = ''

    ss = '' # string start
    se = '' # string end
    ssrev = ''
    serev = ''

    while i <= len(line.strip()) - 1 and j >= 0:
        ss += line[i]
        ssrev = line[i] + ssrev #reverse
        se = line[j] + se
        serev += line[j]   #reverse

        ## print('    ss:{0} se:{1} ssrev:{2} serev:{3}'.format(ss, se, ssrev, serev))
        if num1 == '':
            num1 = getNumber(line[i], ss, ssrev)
        if num2 == '':
            num2 = getNumber(line[j], se, serev)
        
        if num1 != '' and num2 != '':
            break

        i += 1
        j -= 1

    # print('    n1:{0} n2:{1}'.format(num1, num2))

    num = int(num1 + num2)
    return num

def extractNum(line):
    i = 0
    j = len(line.strip()) - 1

    idxStart = -1
    idxEnd = -1

    while i <= j:
        if idxStart < 0 and isNumber(line[i]):
            idxStart = i
        if idxEnd < 0 and isNumber(line[j]):
            idxEnd = j

        if idxStart >= 0 and idxEnd >= 0:
            break

        if idxStart < 0:
            i += 1
        if idxEnd < 0:
            j -= 1

    num = int(line[idxStart] + line[idxEnd])
    ## print('start:{0} end:{1} {2} {3} >> {4}\n'.format(idxStart, idxEnd, line[idxStart], line[idxEnd], num))
    return num

def getSum(file):
    Lines = file.readlines()
    sum = 0
    sum2 = 0

    for line in Lines:
        sum += extractNum(line)
        sum2 += extractNumChars(line)

    print('sum1: {0}'.format(sum))
    print('sum2: {0}'.format(sum2))
    return sum

input = open("inputDay1.txt", "r") 
getSum(input)
'''
Determine which games would have been possible if the bag had been loaded with
only 12 red cubes, 13 green cubes, and 14 blue cubes. What is the sum of the IDs of those games?
'''

'''
- Create map with current values using color as key
- Walkthrough games, divide in sets, per set, make sure that nums are less or equal that num of available cubes
- Add ids for valid Games
'''

colorMap = {'red': 12, 'green': 13, 'blue': 14}

def walkGames(game):
    gameId = game[:len(game)-1].split(':')[0].split(' ')[1]
    sets = game.split(':')[1].split(';')
    valid = True
    for set in sets:
        cubes = set.split(',')
        for cube in cubes:
            kv = cube.strip().split(' ')
            if colorMap[kv[1]] < int(kv[0]):
                valid = False

    if valid:
        # print('valid game {0}', gameId)
        return int(gameId)
    else:
        return 0

def walkGamesMin(game):
    minColorMap = {'red': 0, 'green': 0, 'blue': 0}

    sets = game.split(':')[1].split(';')
    for set in sets:
        cubes = set.split(',')
        for cube in cubes:
            kv = cube.strip().split(' ')
            if minColorMap[kv[1]] < int(kv[0]):
                minColorMap[kv[1]]  = int(kv[0])
    # print(game[:len(game)-1])
    # print(minColorMap)
    return minColorMap['red'] * minColorMap['green'] * minColorMap['blue']


def getSum(file):
    Lines = file.readlines()
    sum = 0
    sumMin = 0
    for line in Lines:
        sum += walkGames(line)
        sumMin += walkGamesMin(line)

    print('1: {0}'.format(sum))
    print('2: {0}'.format(sumMin))
    return sum

input = open("inputDay2.txt", "r") 
getSum(input)
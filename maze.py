import os

mapData = []
startPos = ()
finishPos = ()
playerPos = []
maxRow, maxCol = -1, -1

def prepare():
    loadMap()
    parsingMap()
    displayMap()

# o x o x x x x o F 
# o o o x x o o o x 
# o x o x o o x o x 
# o o o o o x x o o 
# x x x x o o x x x 
# o o o o x o o o o 
# x o x o o o x o x 
# o o o o x o o o x 
# S x x o o x x o x

def loadMap(): #맵 가지고오기
    with open('level1.map', 'r') as f:
        while f.readable():
            line = f.readline()
            if not line:
                break
            line = line.replace('\n', '').replace(' ', '') # \n 기준으로, 공백 없이
            mapData.append(line)
    # print(mapData)

def parsingMap(): # 플레이어 위치
    global startPos, finishPos, maxRow, maxCol
    maxRow = len(mapData) - 1
    for y, line in enumerate(mapData):
        maxCol = len(line) - 1
        for x, tile in enumerate(line):
            if tile == 'S':
                startPos = (y, x)
            if tile == 'F':
                finishPos = (y, x)
    playerPos[:] = startPos[:]
    # print('playerPos:', playerPos)

def displayMap():
    py, px = playerPos
    for y, line in enumerate(mapData):
        li = list(line)
        if y == py:
            # y축이 플레이어의 위치와 같다
            # x축의 인덱스 값을 P로
            li[px] = 'P'
        print(''.join(li))

def play():
    while True:
        os.system('clear')
        py, px = playerPos
        if finishPos[0] == py and finishPos[1] == px:
            print('COOOOOL')
            break
        displayMap()
        print('1.북')
        print('2.동')
        print('3.남')
        print('4.서')
        inputV = input('>>> ')
        # inputV.isdigit()   #숫자의 표현식도 포함
        # inputV.isdecimal() #int형으로 변환이 가능한것만!
        # inputV.isnumeric() #숫자의 표현식도 포함
        if inputV.isnumeric():
            selection = int(inputV)
            if selection == 1:
                dy, dx = py - 1, px
                if checkMovable(dy, dx):
                    playerPos[:] = (dy, dx)
            if selection == 2:
                dy, dx = py, px + 1
                if checkMovable(dy, dx):
                    playerPos[:] = (dy, dx)
            if selection == 3:
                dy, dx = py + 1, px
                if checkMovable(dy, dx):
                    playerPos[:] = (dy, dx)
            if selection == 4:
                dy, dx = py, px - 1
                if checkMovable(dy, dx):
                    playerPos[:] = (dy, dx)

def checkMovable(dy, dx) -> bool: # 조건.. 밖으로 안 나가게, X로 못가게ㅔ
    inBoundary = (0 <= dy and dy <= maxRow) and (0 <= dx and dx <= maxCol)
    validTile = (mapData[dy][dx] != 'x')
    return inBoundary and validTile

if __name__ == '__main__':
    prepare()
    play()

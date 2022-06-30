board = [ 
    ['.','.','.'],
    ['.','.','.'],
    ['.','.','.']
]

def draw_board():
    print()
    for i in range(3):
        s=""
        for j in range(3):
            s+=board[i][j]
        print(s)

def check3(c):
    if board[0][0]==c and board[1][1]==c and board[2][2] == c:
        return True
    if board[0][2]==c and board[1][1]==c and board[2][0] == c:
        return True

    for i in range(3):
        if board[i][0]==c and board[i][1]==c and board[i][2] == c:
            return True
        if board[0][i]==c and board[1][i]==c and board[2][i] == c:
            return True
    return False

def checkEnd():
    for x in range(3):
        for y in range(3):
            if board[x][y] == '.':
                return False
    return True

def check():
    if check3('o'):
        print('you win')
        return True
    if check3('x'):
        print('computer wins')
        return True
    if checkEnd():
        print('draw')
        return True
    return False

def play():
    px = 0
    py = 0
    ps = 0
    for x in range(3):
        for y in range(3):
            if board[x][y] == '.':
                board[x][y] = 'x'
                canWin = check3('x')
                board[x][y] = 'o'
                canLoose = check3('o')
                board[x][y] = '.'
                isCenter = x==1 and y==1
                isCorner = (x==0 and y==0) or (x==0 and y==2) or (x==2 and y==0) or (x==2 and y==2)

                s = 1
                if canWin:
                    s += 5
                if canLoose:
                    s += 4
                if isCenter:
                    s += 3
                if isCorner:
                    s += 2
                if s > ps:
                    ps = s
                    px = x
                    py = y

    board[px][py] = 'x'
         
while True:
    play()
    draw_board()
    if check(): break

    x,y = [int(i) for i in input().split()]
    if x not in range(3) or y not in range(3):
        print("move outside board")
        continue
            
    if board[x][y] == 'x' or board[x][y] == 'o':    
        print("position taken already")
        continue

    board[x][y] = 'o'
    draw_board()

    if check(): break
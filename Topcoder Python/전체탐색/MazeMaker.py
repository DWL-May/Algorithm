def longestPath(maze, startRow, startCol, moveRow, moveCol):
    maxResult = 0
    width = len(maze)
    height = len(maze)

    board = []
    for i in range(height):
        temp = []
        for j in range(width):
            temp.append(-1)
        board.append(temp)

    board[startRow][startCol] = 0

    qX = []
    qY = []

    qX.append(startCol)
    qY.append(startRow)

    while len(qX) != 0:
        x = qX.pop(0)
        y = qY.pop(0)

        for i in range(len(moveRow)):
            print("index" + str(i))
            nextX = x + moveCol[i]
            nextY = y + moveRow[i]
            print(nextX)
            print(nextY)
            if nextX >= 0 and nextX < width and nextY >= 0 and nextY < height and board[nextY][nextX] == -1 and maze[nextY][nextX] == '.':
                board[nextY][nextX] = board[y][x] + 1
                qX.append(nextX)
                qY.append(nextY)
                print(qX)
                print(qY)


    for i in range(height):
        for j in range(width):
            if maze[i][j] == '.' and board[i][j] == -1:
                return -1
            maxResult = max(maxResult,board[i][j])

    return maxResult

maze = [[".",".","."],
        [".",".","."],
        [".",".","."]]

startRow = 0
startCol = 1
moveRow = [1, 0, -1, 0]
moveCol = [0, 1, 0, -1]

print(longestPath(maze,startRow,startCol,moveRow,moveCol))
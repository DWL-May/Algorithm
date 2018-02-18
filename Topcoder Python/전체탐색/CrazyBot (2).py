grid = []

for i in range(100):
    temp = []
    for j in range(100):
       temp.append(False)
    grid.append(temp)
vx = [1, -1, 0, 0]
vy = [0, 0, 1, -1]

prob = [0,0,0,0]

def getProbability(n, east, west, south, north):
    prob[0] = east / 100.0
    prob[1] = west / 100.0
    prob[2] = south / 100.0
    prob[3] = north / 100.0

    return dfs(50,50,n)

def dfs(x,y,n):
    if grid[x][y]:
        return 0

    if n == 0:
        return 1

    grid[x][y] = True
    ret = 0
    for i in range(4):
        ret += dfs(x + vx[i], y + vy[i], n-1) * prob[i]

    grid[x][y] = False

    return ret


print(getProbability(2,25,25,25,25))

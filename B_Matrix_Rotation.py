t = int(input())

def beautifulArr(grid):
    if (grid[0][0] < grid[0][1]) and (grid[0][0] < grid[1][0]) and grid[0][1] < grid[1][1] and grid[1][0] < grid[1][1]:
        pass
    else:
        return 0
    return 1

def rotate(grid):
    grid[0][0], grid[0][1], grid[1][1], grid[1][0] = grid[1][0], grid[0][0], grid[0][1], grid[1][1]
    return grid

def canBeBeautiful(grid):
    if beautifulArr(grid) == 1:
        print("YES")
    else:
        count = 0
        while count < 4:
            grid = rotate(grid)
            if beautifulArr(grid) == 1:
                print("YES")
                return
            else:
                count += 1
        print("NO")
        return

for _ in range(t):
    grid = []
    for row in range(2):
        grid.append(list(map(int, input().split())))

    canBeBeautiful(grid)

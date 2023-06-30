def spiralOrder(matrix: list[list[int]]) -> list[int]:
    a = []
    while matrix:
        a.extend(matrix.pop(0))
        matrix = [*zip(*matrix)][::-1]
    return a

print(spiralOrder([[1,2,3],[4,5,6],[7,8,9]]))

def spiralOrder1(matrix: list[list[int]]) -> list[int]:
    a = []
    if len(matrix) == 0:
        return a

    rows, cols = len(matrix), len(matrix[0])
    top = 0
    bottom = rows - 1
    left = 0
    right = cols - 1
    direction = 0

    while top<=bottom and left <= right:
        if direction == 0:
            for i in range(left, right + 1):
                a.append(matrix[top][i])
            top += 1
        elif direction == 1:
            for i in range(top, bottom + 1):
                a.append(matrix[i][right])
            right -= 1
        elif direction == 2:
            for i in range(right, left -1, -1):
                a.append(matrix[bottom][i])
            bottom -=1
        elif direction == 3:
            for i in range(bottom, top - 1, -1):
                a.append(matrix[i][left])
            left += 1
        direction = (direction + 1) % 4
    
    return a

print(spiralOrder1([[1,2,3],[4,5,6],[7,8,9]]))
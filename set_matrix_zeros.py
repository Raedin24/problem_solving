def setZeros(matrix: list[list[int]]) -> None:
    rows = len(matrix)
    cols = len(matrix[0])
    zeroRows = set()
    zeroCols = set()

    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == 0:
                zeroRows.add(i)
                zeroCols.add(j)

    for i in range(rows):
        for j in range(cols):
            if i in zeroRows or j in zeroCols:
                matrix[i][j] = 0
    
    return matrix

print(setZeros([[1,1,1],[1,0,1],[1,1,1]]))        
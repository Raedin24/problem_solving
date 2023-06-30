def matrixReshape(mat, r, c) -> list[list[int]]:
    if len(mat) * len(mat[0]) != r * c:
        return mat
    else:
        col = []
        row = []
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                col.append(mat[i][j])
                if len(col) == c:
                    row.append(col)
                    col = []
    return row
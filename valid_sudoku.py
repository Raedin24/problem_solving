def isValidSudoku(board: list[list[str]]) -> bool:
    rows = len(board)
    cols = len(board[0])
    rowSet = [set() for i in range(rows)]
    colSet = [set() for i in range(cols)]
    boxSet = [[set() for i in range(cols//3)] for j in range(rows//3)]

    for i in range(rows):
        for j in range(cols):
            if board[i][j] != '.':
                if board[i][j] in rowSet[i]:
                    return False
                else:
                    rowSet[i].add(board[i][j])
                if board[i][j] in colSet[j]:
                    return False
                else:
                    colSet[j].add(board[i][j])
                if board[i][j] in boxSet[i//3][j//3]:
                    return False
                else:
                    boxSet[i//3][j//3].add(board[i][j])
    return True


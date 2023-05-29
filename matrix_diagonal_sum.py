class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        diagonal_sum = 0
        n = len(mat)

        for i in range(n):
            diagonal_sum += mat[i][i]

        for i in range(n):
            if i == n - 1 - i:
                continue
            diagonal_sum += mat[i][n-1 - i]
        
        return diagonal_sum
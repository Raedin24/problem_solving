def rotate(matrix: list[list[int]]) -> None:
   matrix = [*zip(*matrix)][::1]
   for i in range(len(matrix)):
      matrix[i] = list(matrix[i][::-1])      

   return matrix


def rotate2(matrix: list[list[int]]) -> None: # Like 1, but in one line
   matrix = [*zip(*matrix[::-1])]
   return matrix

def rotate3(matrix: list[list[int]]) -> None: # Modify in-place
   matrix.reverse()
   for i in range(len(matrix)):
      for j in range(i):
         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
   
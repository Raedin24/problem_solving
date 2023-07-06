def numMagicSquaresInside(grid: list[list[int]]) -> int:
    def isMagicSquare(subgrid):
        nums = set()
        for row in subgrid:
            nums.update(row)

        if len(nums) != 9 or any(num < 1 or num > 9 for num in nums):
            return False

        target_sum = subgrid[0][0] + subgrid[0][1] + subgrid[0][2]  # sum of the first row

        for i in range(3):
            if sum(subgrid[i]) != target_sum:  # check rows
                return False
            if sum(row[i] for row in subgrid) != target_sum:  # check columns
                return False

        if (subgrid[0][0] + subgrid[1][1] + subgrid[2][2] != target_sum or
                subgrid[0][2] + subgrid[1][1] + subgrid[2][0] != target_sum):  # check diagonals
            return False

        return True

    count = 0

    for i in range(len(grid) - 2):
        for j in range(len(grid[0]) - 2):
            subgrid = [row[j:j + 3] for row in grid[i:i + 3]]
            if isMagicSquare(subgrid):
                count += 1

    return count

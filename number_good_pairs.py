def numIdenticalPairs(nums: list[int]) -> int:
    count = 0
    for i, num1 in enumerate(nums):
        for j, num2 in enumerate(nums):
            if i < j and num1 == num2:
                count += 1
    return count
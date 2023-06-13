def missingNumber(nums: list[int]) -> int:
    for i in range(len(nums)+1):
        if i not in nums:
            return i
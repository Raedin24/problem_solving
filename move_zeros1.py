def moveZeros(nums: list[int]) -> None:
    left = 0
    right = 0

    while right < len(nums):
        if nums[right] != 0:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
        right += 1

    return nums

print(moveZeros([13, 0, 1, 0, 3]))
def sortColors(nums: list[int]):
    r = len(nums) - 1
    for i in range(len(nums)-1):
        for j in range(len(nums)-1):
            if nums[j] > nums[r] and j < r:
                nums[j], nums[r] = nums[r], nums[j]
        r -= 1
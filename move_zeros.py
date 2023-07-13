# def moveZeros(nums: list[int]) -> None:
#     i = nums.count(0)
#     for j in range(i):
#         nums.remove(0)
#     c = 0
#     while c < i:
#         nums.append(0)
#         c += 1

#     return nums

def moveZeroes(nums: list[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    r = 1
    while r < len(nums) and l < len(nums):
        if nums[l] == 0 and nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r += 1
        elif nums[r] == 0:
            r += 1
        else:
            l += 1
    return nums

# print(moveZeroes([1,0,4,0,0]))
# print(moveZeroes([1,0,1]))
print(moveZeroes([2,1]))
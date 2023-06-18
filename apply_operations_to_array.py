def rearrangeArray(nums):
    n = len(nums)
    
    for i in range(n - 1):
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i+1] = 0
    
    zero_idx = 0
    for i in range(n):
        if nums[i] != 0:
            nums[zero_idx] = nums[i]
            zero_idx += 1
    
    while zero_idx < n:
        nums[zero_idx] = 0
        zero_idx += 1

    return nums
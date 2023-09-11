def maximumSubarraySum(nums: list[int], k: int) -> int:
    if len(nums) < k:
        return 0
    
    elements = set()
    for i in range(k):
        elements.add(nums[i])
        if len(elements) == k:
            # start = i
            break

    max_sum = sum(list(elements)[:k])

    for i in range(len(nums) - k):
        window_sum = max_sum - nums[i] + nums[i+k]
        max_sum = max(max_sum, window_sum)
    return max_sum

    max_sum = 0
    for i in range(len(nums) - k):
        if nums[i] in elements:
            while nums[i] in elements:
                elements.remove(nums[i])
                i += 1
        elements.add(nums[i])
        
        if len(elements) == k:
            max_sum = max(max_sum, sum(elements))

maximumSubarraySum([1, 5, 4, 2, 9, 9, 9], 3)
def findMaxAverage(nums: list[int], k: int) -> float:
    max_average = 0
    for i in range(len(nums)):
        average = sum(nums[i:i+k]) / k
        max_average = max(max_average, average)
    return max_average

findMaxAverage([1,12,-5,-6,50,3], 4)
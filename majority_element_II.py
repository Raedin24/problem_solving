from collections import Counter

def majorityElement(nums: list[int]) -> list[int]:
    counter = Counter(nums)
    threshold = len(nums) / 3
    output = []
    for num, count in counter.items():
        if count > threshold:
            output.append(num)

    return output
# Submitted successfully. 2 tries, 11 min.

def majorityElement2(nums: list[int]) -> list[int]:
    output = []
    i = 0
    while i < len(nums):
        if nums.count(i) > (len(nums) /3) and i not in output:
            output.append(i)
    return output
# Time limit exceeded
from collections import Counter
def countDistinctIntegers(nums: list[int]) -> int:
    # rev = []
    for i in range(len(nums)):
        a = int(str(nums[i])[::-1])
        nums.append(a)
    # nums.append(rev)
    c = Counter(nums)
    
    return len(c)


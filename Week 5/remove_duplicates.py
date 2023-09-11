def removeDuplicates(nums: list[int]) -> int:
    nums_set = set()
    output = []
    count = 0
    for i in range(len(nums)):
        if nums[i] not in nums_set:
            nums_set.add(nums[i])
    return list(nums_set)

def removeDuplicates1(nums: list[int]) -> int:
    for i in range(len(nums) - 1):
        j = i+1
        while i < len(nums) - 1:
            j = i+1
            if nums[i] == nums[j]:
                nums.remove(nums[j])
            else:
                break
            j += 1
        


n = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates1(n))
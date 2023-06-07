def removeElement(nums: list[int], val:int) -> int:
    i = 0
    while i <  nums.count(val):
        nums.remove(val)

    return nums, len(nums)

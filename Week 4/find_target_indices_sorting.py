def targetIndices(nums: list[int], target: int) -> list[int]:
    nums.sort()
    target_index = []
    for i, num in enumerate(nums):
        if num == target:
            target_index.append(i)
    return target_index

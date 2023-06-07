def moveZeros(nums: list[int]) -> None:
    i = nums.count(0)
    for j in range(i):
        nums.remove(0)
    c = 0
    while c < i:
        nums.append(0)
        c += 1

    return nums
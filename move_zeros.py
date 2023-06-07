def moveZeros(nums: list[int]) -> None:
    i = nums.count(0)
    for j in range(i):
        nums.remove(0)
    c = 0
    while c < i:
        nums.append(0)
        c += 1
    
        # if i == 0:
        #     nums.pop(i)
        #     # nums.append(i)
        # else:
        #     continue

    return nums

print(moveZeros([0, 1, 0, 3, 12])) # 1, 3, 12, 0, 0
print(moveZeros([0])) # 0
print(moveZeros([0, 0, 1])) # 1, 0, 0
print(moveZeros([0, 1, 0, 3, 12, 0, 0, 0, 0, 0, 0, 0])) # 1, 3, 12, 0, 0
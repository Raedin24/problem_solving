def merge(nums1: list[int], nums2: list[int], n:int):

    for i in nums2:
        nums1.append(i)
    j = 0
    while j < n:
        nums1.remove(0)
        j += 1
    nums1.sort()

    return nums1
# Not efficient
def merge1(nums1: list[int], m: int, nums2: list[int], n:int) -> None:
    p1 = m - 1
    p2 = n - 1
    p = m + n -1

    while p1 >= 0 and p2 >=0:
        if nums1[p1] < nums2[p2]:
            nums1[p] = nums2[p2]
            p2 -= 1
        else:
            nums1[p] = nums1[p1]
            p1 -= 1
        p -= 1

    if p1 < 0:
        nums1[p] = nums2[p2]

    
    return nums1

print(merge1([0], 0, [1], 1))

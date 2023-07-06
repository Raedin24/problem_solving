import time

# def validMountainArray(arr: list[int]) -> bool:
#     if len(arr) < 3:
#         return False
#     k = max(arr[:])
#     i = l = r = 0
#     while i < arr.index(k):
#         if arr[i] < arr[i+1]:
#             i += 1
#         else:
#             l = 1
        
#     j = len(arr) - 1
#     while j > arr.index(k):
#         if arr[j] < arr[j-1]:
#             j -= 1
#         else:
#             r = 1

#     if not (l or r):
#         return True
#     return False

# t1 = time.time()
# print(validMountainArray([0,2,3,4,5,2,1,0]))
# print(validMountainArray([2,1]))
# print(validMountainArray([9,8,7,6,5,4,3,2,1,0]))
# t2 = time.time()
# print(t2-t1)

# def validMountainArray2(arr: list[int]) -> bool:
#     k = max(arr[:])
#     if len(arr) < 3 or arr.index(k) == 0 or arr.index(k) == -1:
#         return False
#     i = 0
#     while i < len(arr) - 1 and arr[i] < arr[i+1]:
#         i += 1
#     if i == len(arr) - 1:
#         return False
#     while i < len(arr) - 1 and arr[i] > arr[i+1]:
#         i += 1
#     if i == len(arr) - 1:
#         return True
#     return False

# t1 = time.time()
# print(validMountainArray2([0,2,3,4,5,2,1,0]))
# print(validMountainArray2([2,1]))
# print(validMountainArray2([9,8,7,6,5,4,3,2,1,0]))
# t2 = time.time()
# print(t2-t1)

def validMountainArray3(arr: list[int]) -> bool:
    k = max(arr[:])
    if len(arr) < 3 or arr[0] == k or arr[-1] == k:
        return False
    for i in range(0, arr.index(k)):
        if arr[i] < arr[i+1]:
            continue
        else:
            return False
    for j in range(arr.index(k), len(arr) - 1):
        if arr[j] > arr[j+1]:
            continue
        else:
            return False
    return True

t1 = time.time()
print(validMountainArray3([9,8,7,6,5,4,3,2,1,0])) # False
print(validMountainArray3([2,1])) # False
print(validMountainArray3([0,2,3,4,5,2,1,0])) # True
print(validMountainArray3([0,1,2,3,4,5,6,7,8,9])) # False
print(validMountainArray3([3,5,5])) # False
print(validMountainArray3([0,3,2,1])) # True
t2 = time.time()
print(t2 - t1)
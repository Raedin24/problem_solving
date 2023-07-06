# def replaceElements(arr: list[int]) -> list[int]: # O(n^2). Time limit exceeded.
#     for i in range(len(arr) - 1):
#         k = max(arr[i+1:])
#         arr[i] = k
#     arr[-1] = -1

#     return arr
import time

def replaceElements(arr: list[int]) -> list[int]: # O(n). Time limit exceeded.
    max_num = -1
    for i in range(len(arr) - 1, -1, -1):
        temp = arr[i]
        arr[i] = max_num
        max_num = max(max_num, temp)

    return arr

def replaceElements2(arr: list[int]) -> list[int]: # O(n). Time limit exceeded.
    max_num = -1
    for i in range(len(arr) - 1, -1, -1):
        arr[i], max_num = max_num, max(max_num, arr[i])
        # max_num = max(max_num, temp)

    return arr

t1 = time.time()
print(replaceElements([17,18,5,4,6,1]))
t2 = time.time()
print(t2-t1)

t1 = time.time()
print(replaceElements2([17,18,5,4,6,1]))
t2 = time.time()
print(t2-t1)
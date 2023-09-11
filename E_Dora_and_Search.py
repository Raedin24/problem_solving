"""
Given a permutation
Find a subsegment where the minimum and maximum elements are not the ends of the subsegment
ie. l, r where 1 <= l <= r <= n
for an array of len(n), if must only contain elements in range(n)
ie. n = 3, arr = [1, 2, 3] not [1, 3, 4]

If such a subsegment exits, output l and r
Else output -1
"""

t = int(input())
for _ in range(t):
    n = int(input()) # Length of permutation
    a = list(map(int, input().split())) # Elements of the permutation
    l, r = 0 , n - 1
    min_val, max_val = 1, n

    while l <= r:
        if a[l] == min_val:
            l += 1
            min_val += 1
        elif a[r] == min_val:
            r -= 1
            min_val += 1
        elif a[r] == max_val:
            r -= 1
            max_val -= 1
        elif a[l] == max_val:
            l += 1
            max_val -= 1

        else:
            break
    if l <= r:
        print(l+1, r+1)
    else:
        print(-1)

# t = int(input())
# for _ in range(t):
#     n = int(input()) # Length of permutation
#     a = list(map(int, input().split())) # Elements of the permutation
#     l, r = 0 , n - 1
#     # min_val, max_val = 1, n

#     while l < r:
#         min_val = min(a[l:r+1])
#         max_val = max(a[l:r+1])

#         if a[l] == min_val:
#             l + 1
#         elif a[r] == min_val:
#             r -= 1
#         elif a[l] == max_val:
#             l += 1
#         elif a[r] == max_val:
#             r -= 1
#         else: 
#             break


    """
    4
    3
    1 2 3
    4
    2 1 4 3

      l   r

    7
    1 3 2 4 6 5 7
    6
    2 3 6 5 4 1

    """

    # if len(a) == len(set(a)):
    #     l, r = 0, 3
    #     while r < n-1:
    #         window_max, window_min = max(a[l:r+1]), min(a[l:r+1])
    #         if window_min == 1 and a.index(window_min) == l or a.index(window_min) == r:
    #             l += 1
    #             r += 1
    #             window_max, window_min = max(a[l:r+1]), min(a[l:r+1])
                
    #         elif window_max == n-1 and a.index(window_max) == l or a.index(window_max) == r:
    #             r += 1
    #             window_max, window_min = max(a[l:r+1]), min(a[l:r+1])
    #         else:
    #             print(l+1, r+1)
    #             r += 1
                

        # """
        # check if all elements are in range(1, n)
        # for each subsegment, check if [0] and [-1] are either the max or the min of the entire permutation
        # find max and min of a subsegment of len(3)
        # if it satisfies the conditions, print indices.
        # else increase window by 1.
        # if new element > max or < min, store in respective variable
        # """
    # else:
    #     print(-1)

# def greater_than(a, b):
#     if b > a:
#         a = b
#     return a
    
# def less_than(a, b):
#     if b < a:
#         a = b
#     return a
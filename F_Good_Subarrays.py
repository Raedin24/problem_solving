t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input()))
    # print(a)
    a.sort()
    count = l = 0
    prefix_arr = []
    prefix_arr.append(0)
    for i in range(n):
        prefix_arr.append(prefix_arr[i-1] + a[i])
    while l < n:
        count += 1
        if count == prefix_arr[l]:
            l += 1
"""
a = [0, 1, 2]
prefix_a = [0, 1, 3]


"""
def swap(a):
    # max_swaps = n * (n - 1) // 2 - 1
    swaps = 0
    for i in range(1, len(a)):
        if a[i - 1] > a[i]:
            swaps += 1
    if swaps != len(a) - 1:
        return "YES"
    return "NO"


t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    result = swap(a)
    print(result)

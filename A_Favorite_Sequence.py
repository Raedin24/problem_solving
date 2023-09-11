t = int(input())

for _ in range(t):
    n = int(input())
    b = list(map(int, input().split()))

    l = 0
    r = n - 1
    original = []
    if n % 2 == 0:
        while l < n // 2:
            original.append(b[l])
            original.append(b[r])
            l += 1
            r -= 1
    else:
        while l != r:
            original.append(b[l])
            original.append(b[r])
            l += 1
            r -= 1
        if l == r:
            original.append(b[l])

    print(*original)
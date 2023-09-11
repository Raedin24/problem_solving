t = int(input())

for _ in range(t):
    n = int(input())
    # for __ in range(n):
    first = list(map(int, input().split()))
    m = int(input())
    second = list(map(int, input().split()))

    prefix_sum = [0]
    l = r = i = 0
    while l != n and r != m:
        prefix_sum.append(prefix_sum[i] + first[l])
        i+= 1
        l += 1

        prefix_sum.append(prefix_sum[i] + second[r])
        i += 1
        r += 1

    if l == n:
        for k in range(r, m):
            prefix_sum.append(prefix_sum[i] + second[k])

    if r == m:
        for k in range(l, n):
            prefix_sum.append(prefix_sum[i] + first[k])

    print(max(0, prefix_sum))




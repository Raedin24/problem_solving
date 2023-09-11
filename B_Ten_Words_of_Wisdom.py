t = int(input())

for _ in range(t):
    n = int(input())
    s = []
    for i in range(n):
        res = list(map(int, input().split()))
        if res[0] <= 10:
            s.append([res[1], i])
    s.sort(reverse=True)
    print(s[0][1] + 1)





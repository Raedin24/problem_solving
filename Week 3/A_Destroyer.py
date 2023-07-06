from collections import Counter
t = int(input())



def isFaulty(n, a):
    a.sort()

    b = [0 for i in range(max(a)+1)]
    m = Counter(a)
    for i in range(len(b)):
        b[i] = m[i]
    for i in range(len(b)-1):
        if m[i] >= m[i+1]:
            continue
        else:
            print("NO")
            return
    print("YES")


for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    isFaulty(n, a)


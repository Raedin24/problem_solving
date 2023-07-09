t = int(input())

def canTransform(n, a, b): # Time limit exceeded
    if a == b:
        print("YES")
        return

    for i in range(n):
        c = a.copy()
        d = b.copy()
        for j in range(len(a[:i+1])):
            c[j] = c[j]+ 1
        d.sort()
        c.sort()
        if c == d:
            print("YES")
            return
            
    print("NO")
    return

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    canTransform(n, a, b)
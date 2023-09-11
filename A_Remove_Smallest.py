def isConsecutive(n, a):
    a.sort()
    for i in range(n-1):
        if a[i+1] == a[i] + 1 or a[i] == a[i+1]:
                continue
        else:
                print("NO")
                return
    print("YES")
    return
      
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    isConsecutive(n, a)
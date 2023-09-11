t = int(input())

def check_num(a):
    a.sort(reverse=True)
    l = r = count = 0
    while r < len(a):
        if a[l] == a[r]:
            count += 1
            r += 1
        else:
            l = r
            count = 0
        if count >= 3:
            print(a[l])
            return

    print(-1)
    return

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    check_num(a)
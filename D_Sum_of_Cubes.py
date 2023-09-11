def check_num(t):
    limit = int(t**(1/3))
    combos = set()
    if t <= 1:
        print("No")
        return
    else:
        for i in range(1, limit+1):
            combos.add(i**3)

        for j in combos:
            if t - j in combos:
                print("Yes")
                return
    print("No")
    return

n = int(input())
for _ in range(n):
    t = int(input())
    check_num(t)
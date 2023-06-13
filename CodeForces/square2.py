t = int(input())
sizes = []

for i in range(t):
    a1, b1 = map(int, input().split())
    a2, b2 = map(int, input().split())
    sizes.append([a1, b1, a2, b2])

for i in range(t):
    a1, b1, a2, b2 = sizes[i]
    if a1 > b1:
        a1, b1 = b1, a1
    if a2 > b2:
        a2, b2 = b2, a2
    if a1 + a2 == b1 and b1 == b2:
        print("Yes")
    else:
        print("No")
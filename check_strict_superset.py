superset = set(map(int, input().split()))
num_sets = int(input())
isSuperSet = 1
for i in range(num_sets):
    otherSet = set(map(int, input().split()))
    if otherSet.issubset(superset):
        continue
    else:
        isSuperSet = 0
        break

print(bool(isSuperSet))
from collections import Counter

n = int(input())
s = []
for _ in range(n):
    s.append(input())

print(len(Counter(s)))
for j in Counter(s).values():
    print(j, end=" ")
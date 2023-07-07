n = int(input())
a = list(map(int, input().split()))

sum_a = sum(a)
indices = []
for i in range(len(a)):
    if a[i] ==  (sum_a - a[i])/(n-1):
        indices.append(i+1)    

if indices:
    print(len(indices))
    print(*indices)

else:
    print(0)
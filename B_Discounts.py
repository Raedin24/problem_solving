n = int(input())
a = list(map(int, input().split()))
m = int(input())
q = list(map(int, input().split()))

a.sort(reverse=True)
acc = sum(a)
for i in q:
    print(acc - a[i-1])
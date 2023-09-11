# t = int(input())

# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))

#     a.sort(reverse=True)

#     if n <= 1:
#         print("YES")
#         break
#     max_diff = a[0] - a[1]
    
#     for i in range(n - 1):
#         diff = a[i] - a[i+1]
#         max_diff = max(diff, max_diff)
#     if max_diff > 1:
#         print("NO")
#     else:
#         print("YES")

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    min_val = min(a)
    max_val = max(a)

    if max_val - min_val <= 1:
        print("YES")
    else:
        print("NO")

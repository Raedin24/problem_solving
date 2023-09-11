# t = int(input())

# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))

#     for i in range(n):
#         if a[i] % 2 == 0:
#             for j in range(i+1, n):
#                 if a[j] % 2 == 0 and a[j] < a[i]:
#                     a[i], a[j] = a[j], a[i]
#                     continue
#         else:
#             for j in range(i+1, n):
#                 if a[j] % 2 != 0 and a[j] < a[i]:
#                     a[i], a[j] = a[j], a[i]
#                     continue

#     if a == sorted(a):
#         print("YES")
#     else:
#         print("NO")

t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    even = []
    odd = []
    for num in a:
        if num % 2 == 0:
            even.append(num)
        else:
            odd.append(num)

    even.sort()
    odd.sort()

    sorted_arr = []
    even_idx = 0
    odd_idx = 0

    for num in a:
        if num % 2 == 0:
            sorted_arr.append(even[even_idx])
            even_idx += 1
        else:
            sorted_arr.append(odd[odd_idx])
            odd_idx += 1

    if sorted_arr == sorted(a):
        print("YES")
    else:
        print("NO")

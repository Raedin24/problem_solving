# q = int(input())

# for _ in range(q):
#     n = list(map(int, input().split()))
#     s = n.copy()
#     distance_list = []
#     distance_list.append(n)
#     # One moves forward
#     for i in range(len(n)):
#         n[i] += 1
#         distance_list.append(n)
#         n = s.copy()
#     # One moves backward
#     for i in range(len(n)):
#         n[i] -= 1
#         distance_list.append(n)
#         n = s.copy()
#     # Two move forward
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             n[i] += 1
#             n[j] += 1
#             distance_list.append(n)
#             n = s.copy()
#     # Two move backward
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             n[i] -= 1
#             n[j] -= 1
#             distance_list.append(n)
#             n = s.copy()
#     # One moves forward, one moves backward
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             n[i] += 1
#             n[j] -= 1
#             distance_list.append(n)
#             n = s.copy()
#     # One moves backward, one moves forward
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             n[i] -= 1
#             n[j] += 1
#             distance_list.append(n)
#             n = s.copy()
#     # Three move forward
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             for k in range(j + 1, len(n)):
#                 n[i] += 1
#                 n[j] += 1
#                 n[k] += 1
#                 distance_list.append(n)
#                 n = s.copy()
#     # Three move backward
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             for k in range(j + 1, len(n)):
#                 n[i] -= 1
#                 n[j] -= 1
#                 n[k] -= 1
#                 distance_list.append(n)
#                 n = s.copy()
#     # Two move forward, one move backward
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             for k in range(j + 1, len(n)):
#                 n[i] += 1
#                 n[j] += 1
#                 n[k] -= 1
#                 distance_list.append(n)
#                 n = s.copy()
#     # Two move backward, one move forward
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             for k in range(j + 1, len(n)):
#                 n[i] -= 1
#                 n[j] -= 1
#                 n[k] += 1
#                 distance_list.append(n)
#                 n = s.copy()
#     # One move forward, two move backward
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             for k in range(j + 1, len(n)):
#                 n[i] += 1
#                 n[j] -= 1
#                 n[k] -= 1
#                 distance_list.append(n)
#                 n = s.copy()
#     # One move backward, two move forward
#     for i in range(len(n)):
#         for j in range(i + 1, len(n)):
#             for k in range(j + 1, len(n)):
#                 n[i] -= 1
#                 n[j] += 1
#                 n[k] += 1
#                 distance_list.append(n)
#                 n = s.copy()
    
#     print(distance_list)


# t = int(input())

# for i in range(t):
#     a = list(map(int, input().split()))
#     a.sort()

#     if a[0] == a[1] and a[1] == a[2]:
#         ans = 0
#     elif a[0] == a[1]:
#         a[0] += 1
#         a[1] += 1
#         if a[2] != a[1]:
#             a[2] -= 1
#         ans = abs(a[0] - a[1]) + abs(a[1] - a[2]) + abs(a[0] - a[2])
#     elif a[1] == a[2]:
#         a[1] -= 1
#         a[2] -= 1
#         if a[0] != a[1]:
#             a[0] += 1
#         ans = abs(a[0] - a[1]) + abs(a[1] - a[2]) + abs(a[0] - a[2])
#     else:
#         a[0] += 1
#         a[2] -= 1
#         ans = abs(a[0] - a[1]) + abs(a[1] - a[2]) + abs(a[0] - a[2])

#     print(ans)

q = int(input())
m = list(map(int, input().split()))

for _ in range(q):
    m.sort()
    if m[0] == m[1] == m[2]:
        print(0)
    
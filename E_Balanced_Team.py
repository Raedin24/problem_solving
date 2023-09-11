# n = int(input())
# a = list(map(int, input().split()))

# a.sort()

# # for i in range(n-1, -1, -1):
# #     for j in range(n):
# #         max_team = max(a[j:i+1]) - min(a[j:i+1])
# #         if max_team <= 5:
# #             print(max_team)
# #             break
# #         else:
# #             continue

# max_team = None
# for i in range(n-1):
#     count = 0
#     for j in range(n-1, i, -1):
#         if abs(a[i] - a[j]) <= 5:
#             count += 1
#     count += 1
#     if max_team == None or count > max_team:
#         max_team = count
# print(max_team)

n = int(input())
a = list(map(int, input().split()))

a.sort()
max_team = 0

i, j = 0, 0
while i < n and j < n:
    while j < n and a[j] - a[i] <= 5:
        j += 1
    max_team = max(max_team, j - i)
    i += 1

print(max_team)

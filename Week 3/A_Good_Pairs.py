

# def isGoodPair(n, a):

#         # if len(a) == 1:
#         #     print(1, 1)

#         # else:
#         good_pairs = []
#         count = 0
#         for i in range(len(a)):
#             for j in range(len(a)):
#                 abs_diff  = abs(a[i] - a[j])
#                 for k in range(n+1):
#                     diff_i = abs(a[i] - a[k])
#                     diff_j = abs(a[k] - a[j])
#                     if diff_i + diff_j == abs_diff:
#                         good_pairs.append([i+1, j+1])
#                         count += 1
#                         # return
#                     # else:
#                     #     continue
#         if count == 1:
#              print(good_pairs[0][0], good_pairs[0][1])
#         else:
#              print(good_pairs[-1][0], good_pairs[-1][1])

# t = int(input())
# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
# isGoodPair(n, a)

def isGoodPair(n, a):
    min_val = min(a)
    max_val = max(a)

    if min_val == max_val:
        print(1, 1)

    else:
        min_idx = a.index(min_val) + 1
        max_idx = a.index(max_val) + 1
        print(min_idx, max_idx)

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    isGoodPair(n, a)

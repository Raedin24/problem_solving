s = input()
m = int(input())
sum_arr = [0, 0]
d = 0
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        d += 1
        sum_arr.append(d)
    else:
        # h += 1
        sum_arr.append(d)
# print(sum_arr)

for _ in range(m):
    query = list(map(int, input().split()))

    print(sum_arr[query[1]] - sum_arr[query[0]])



"""
number of i such that li < i < ri
si = si+1
"""
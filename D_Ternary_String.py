from collections import Counter
t = int(input())


for _ in range(t):
    s = list(map(int, input()))
    if len(Counter(s)) < 3:
        print(0)
    else:
        sub = []
        min_sub = None
        for i in range(len(s)-1):
            sub_i = []
            while len(Counter(sub_i)) < 3 and i < len(s):
                sub_i.append(s[i])
                i += 1
            if len(Counter(sub_i)) == 3:
                sub.append(sub_i)
        for sub_i in sub:
            if min_sub == None or len(sub_i) <len(min_sub):
                min_sub = sub_i

        print(len(min_sub))


# n = int(input())

# for _ in range(n):
#     a = list(map(int, input()))

#     max_string = set()

#     i, j = 0, 0
#     min_len = None
#     while i < len(a) and j < len(a):
#         while j < n and (1 not in max_string or 2 not in max_string or 3 not in max_string):
#             j += 1
#             max_string.add(a[j])
#         max_string.add(a[i])
#     if min_len == None:
#         min_len= j - i
#     else:
#         min_len= min(min_len, j - i)
#         i += 1

#     print(min_len+1)
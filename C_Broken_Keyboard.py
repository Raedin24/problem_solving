# from collections import Counter
# t = int(input())
# for _ in range(t):
#     s = input()
#     correct_keys = []
#     for key in Counter(s):
#         if Counter(s)[key] % 2 == 0:
#             continue
#         else:
#             correct_keys.append(key)
#     correct_keys = sorted(correct_keys)
#     print(*correct_keys, sep="")

    
# t = int(input())

# def isFaulty(s):
#     if len(s) < 2:
#         print(*s)
#         return
    
#     correctKeys = []
#     i = 0
#     # for i in range(len(s)):
#     while i < len(s):
#         j = i+1
#         if j == len(s):
#             correctKeys.append(s[i])
#             break
#         if s[i] == s[j]:
#             i += 2
#             continue
#         else:
#             if s[i] not in correctKeys:
#                 correctKeys.append(s[i])
#                 i += 1
#     res = sorted(correctKeys)
#     print(*res, sep="")
#     return

# for _ in range(t):
#     s = input()
#     isFaulty(s)

t = int(input())

def isFaulty(s):
    if len(s) < 2:
        print(*s)
        return
    
    correctKeys = set()
 
    i = 0
    while i < len(s):
        if i == len(s) - 1:
            correctKeys.add(s[i])
            break
        elif s[i] != s[i + 1] and i+1 < len(s):
            correctKeys.add(s[i])
            i += 1
        else:
            i += 2

    print(*sorted(correctKeys), sep="")

for _ in range(t):
    s = input()
    isFaulty(s)

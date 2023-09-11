"""
indices = []

while l != r:
    if '(' and ')' are both in wrong positions:
        shift both
        flag = Fasle
    elif '(' and ')' are both in correct positions:
        shift both, 
        if not flag: k += 1
        pairs += 1
        flag = True
        indices.extend([l, r])
    elif l is correct, shift right or vice versa
        flag = False

indices.sort()
print(k)
if k:
    print(pairs * 2)
    print(*indices, sep = " ")


"""

s = input()

l, r = 0, len(s)-1
k , pairs = 0, 0
indices = []

while l < r:
    if s[l] == ")" and s[r] == "(":
        l += 1
        r -= 1
    elif s[l] == "(" and s[r] ==")":
        pairs += 1
        indices.extend([l+1, r+1])
        l += 1
        r -= 1
    elif s[l] == "(":
        r -= 1
    elif s[r] == ")":
        l += 1

if pairs:
    print(1)
    indices.sort()
    print(pairs * 2)
    print(*indices, sep=" ")
else:
    print(0)
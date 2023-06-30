from collections import Counter

s = input()
t = Counter(s)
if len(t) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")

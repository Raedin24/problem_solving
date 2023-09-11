# from collections import Counter
n, k = map(int, input().split())
s = input()

max_beauty = 0
count_a = 0
count_b = 0
left = 0

for right in range(n):
    if s[right] == 'a':
        count_a += 1
    else:
        count_b += 1

    changes_needed = min(count_a, count_b)

    while changes_needed > k:
        if s[left] == 'a':
            count_a -= 1
        else:
            count_b -= 1
        left += 1
        changes_needed = min(count_a, count_b)

    current_beauty = right - left + 1

    max_beauty = max(max_beauty, current_beauty)

print(max_beauty)

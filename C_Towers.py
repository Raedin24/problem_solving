from collections import Counter

n = int(input())

bar_lengths = list(map(int, input().split()))
bar_counts = Counter(bar_lengths)

max_frequency = max(bar_counts.values())
distinct_len = len(bar_counts)

print(max_frequency, distinct_len)

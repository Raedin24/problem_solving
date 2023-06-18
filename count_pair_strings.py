from collections import Counter
def similarPairs(nums) -> int:
    counter = Counter(nums)
    pair_count = 0
    for count in counter.values():
        pair_count += count * (count - 1) // 2
    return pair_count
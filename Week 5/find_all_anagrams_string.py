from collections import Counter
def findAnagrams(s: str, p: str) -> list[int]:
    anagram_index = []
    n, m = len(s), len(p)
    target = Counter(p)
    window = Counter(s[:m])
    ans = 0
    if target == window:
        anagram_index.append(0)

    for i in range(m, n):
        if Counter(s[l:r]) == target:
            anagram_index.append(i)
        l += 1
        r += 1
    return anagram_index

findAnagrams("abab", "ab")
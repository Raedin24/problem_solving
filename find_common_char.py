from collections import Counter

def commonChars(words):
    counts = Counter(words[0])

    for word in words[1:]:
        counts &= Counter(word)

    common = []

    for char, freq in counts.items():
        common.extend([char] * freq)

    return common

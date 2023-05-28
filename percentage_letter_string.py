from collections import Counter
import math

def percentageLetter(s, letter):
    s_num = len(s)
    l_num = Counter(s)[letter]
    l_perc = math.floor((l_num / s_num) * 100)

    return l_perc

percentageLetter("foobar", "o")
from collections import Counter
t = int(input())

for _ in range(t):
    s = input()

    # Find the number of distinct characters in the string 
    freq = Counter(s)
    rearranged = []

    for keyl in freq:
        if freq[keyl] != 2:
            rearranged.append(keyl)
    for keyl in freq:
        if freq[keyl] == 2:
            rearranged.append(keyl*2)
    
    print(*rearranged, sep="")
    
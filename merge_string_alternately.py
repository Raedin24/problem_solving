def mergeAlternately(word1, word2): #Submitted
    c = 0
    output = ""
    max1 = max(len(word1), len(word2))
    while c < max1:
        if c < len(word1):
            output += word1[c]
        if c < len(word2):
            output += word2[c]
        c += 1

    return output

def mergeAlternatelyFor(word1, word2):
    output = ""
    for char1, char2 in zip(word1, word2):
        output += char1 + char2
    output += word1[len(word2):] + word2[len(word1):]
    return output
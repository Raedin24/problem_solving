def stammer(n: int, speech: list[str]):
    for word in speech:
        stam = word[0] + word[1]
        print(stam + '... ' + word + '?')

n = int(input())
speech = [''] * n
i = 0
while i < n:
    speech[i] = input()
    i += 1
stammer(n, speech)

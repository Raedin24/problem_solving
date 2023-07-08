import math

n = int(input())
a = list(map(int, input().split()))

negatives = []
positives = []
zeros = []

for num in a:
    if num < 0:
        negatives.append(num)
    elif num > 0:
        positives.append(num)
    else:
        zeros.append(num)

# Ensure each set is correct
if not positives:
    positives.extend([negatives.pop(), negatives.pop()])
if math.prod(negatives) > 0:
    zeros.append(negatives.pop())
if math.prod(positives) < 0:
    zeros.append(positives.pop())

print(len(negatives), *negatives)
print(len(positives), *positives)
print(len(zeros), *zeros)

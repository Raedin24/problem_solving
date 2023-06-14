t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    operations = []
    max_values = [a[0]]
    min_values = [a[0]]

    for i, ai in enumerate(a):
        if ai > max_values[-1]:
            if max_values:
                operations.append((i+1, ai - max_values[-1]))
            max_values.append(ai)
        elif ai < min_values[-1]:
            operations.append((i+1, min_values[-1] - ai))
            min_values.append(ai)

    p = len(operations)
    print(p)
    for i, x in operations:
        print(i, x)

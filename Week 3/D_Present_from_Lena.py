n = int(input())
output = []

if 2 <= n <= 9:
    # Upper portion
    for i in range(n + 1):
        spaces = (n - i) * 2
        spaces = spaces * " "
        # print(' ' * spaces, end='')
        output.append(spaces)
        for j in range(0, i + 1):
            # print(j, end=' ')
            output.append(str(j))
        for j in range(i - 1, -1, -1):
            # print(j, end=' ')
            output.append(str(j))
        for v in range(len(output)):
            if v > 0 and v != (len(output)-1):
                print(output[v], end = " ")
            else:
                print(output[v], end = "")
        output = []
        print()

    # Lower portion
    for k in range(n-1, -1, -1):
        spaces = (n  - k) * 2
        spaces = spaces * " "
        # print(' ' * spaces, end='')
        output.append(spaces)
        for j in range(0, k + 1):
            # print(j, end=' ')
            output.append(str(j))
        for j in range(k - 1, -1, -1):
            # print(j, end=' ')
            output.append(str(j))
        for v in range(len(output)):
            if v > 0 and v != (len(output)-1):
                print(output[v], end = " ")
            else:
                print(output[v], end = "")
        output = []
        print()
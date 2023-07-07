t = int(input())

for _ in range(t):
    a = []
    n, m = map(int, input().split())
    for _ in range(n):
        a.append(list(input()))
    index = 0
    for col in range(m):
        for row in range(n):
            if a[row][col] == '*':
                index += 1
                a[row][col] = '.'
            elif a[row][col] == 'o':
                for _ in range(index):
                    row -= 1
                    a[row][col] = '*'                    
                index = 0
        if row == n - 1 and index != 0:
            for _ in range(index):
                a[row][col] = '*'
                row -= 1
            index = 0

    for new_row in a:
        print(''.join(new_row))
    print()
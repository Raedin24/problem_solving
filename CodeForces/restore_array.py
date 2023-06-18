t = int(input())
test_cases = []
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))
 
for n, a in test_cases:
    good_array = [0] * n
    good_array[0] = a[0]
    for i in range(n - 2):
        good_array[i+1] = min(a[i], a[i + 1])
    good_array[-1] = a[-1]
    print(*good_array)
import math

def nearest_power_2(n):
    return 2 ** math.ceil(math.log(n, 2))


t = int(input())
test_cases = []

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    test_cases.append((n, a))
    
for n, a in test_cases:
    operations = []
    for i in range(n):
        x = nearest_power_2(a[i]) 
        if x > 0:
            operations.append((i+1, x - a[i]))
            
    print(len(operations))
    for op in operations:
        print(*op)


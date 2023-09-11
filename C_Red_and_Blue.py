t = int(input())

for _ in range(t):
    n = int(input())
    first = list(map(int, input().split()))
    m = int(input())
    second = list(map(int, input().split()))

    prefix_sum_r = [0]
    prefix_sum_b = [0]

    for i in range(len(first)):
        prefix_sum_r.append(prefix_sum_r[i] + first[i])
    prefix_sum_r.sort(reverse=True)

    for i in range(len(second)):
        prefix_sum_b.append(prefix_sum_b[i] + second[i])
    prefix_sum_b.sort(reverse=True)

    print(prefix_sum_r[0] + prefix_sum_b[0])

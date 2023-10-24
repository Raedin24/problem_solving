def small_strength(n, artifacts):
    current_sum = 0

    for artifact in artifacts:
        if artifact > current_sum + 1:
            return current_sum + 1
        current_sum += artifact

    return current_sum + 1

n = int(input())
artifacts = list(map(int, input().split()))
artifacts.sort()

result = small_strength(n, artifacts)
print(result)

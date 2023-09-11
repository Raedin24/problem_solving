def countingSort(arr):
    sortedIndex = [0] * 100
    for i in arr:
        sortedIndex[i] += 1
    # result = []
    # for j in range(len(sortedIndex)):
    #     while sortedIndex[j] > 0:
    #         result.append(j)
    #         sortedIndex[j] -= 1
    return sortedIndex

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = countingSort(arr)
    print(*result)
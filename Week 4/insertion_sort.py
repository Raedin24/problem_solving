# Probably not the best solution, but it works.

def insertionSort1(n, arr):
    unsorted = arr[-1]
    if n == 1 :
        print(*arr)
        return
    if n == 2:
        arr[-1] = arr[0]
        print(*arr)
        arr[0] = unsorted
        print(*arr)
        return
    for i in range(n - 1, -1, -1):
        if i == 0:
            arr[i] = unsorted
            print(*arr)
            break
        if arr[i-1] > unsorted:
            arr[i] = arr[i-1]
        else:
            arr[i] = unsorted
            print(*arr)
            break
        print(*arr)
        
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    insertionSort1(n, arr)
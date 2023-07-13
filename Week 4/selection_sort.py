def select(arr, i):
    return 0



def selectionSort(arr, n):
    for i in range(n):
        min = i
        for j in range(i + 1, n):
            if arr[j] < arr[min]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

print(selectionSort([4,1,3,9,7], 5))
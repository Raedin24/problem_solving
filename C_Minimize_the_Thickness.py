"""
max_split_window
min_split_array

"""
for i in range(int(input())):
    n = int(input())
    array = list(map(int, input().split()))
    p_sum = array.copy()
    for i in range(1, len(p_sum)):
        p_sum[i] += p_sum[i-1]

    max_split_window = 0
    min_split_array = float('inf')

    for sum_ in p_sum:
        start = 0
        i = 0
        curr_sum = 0
        thickness = 0
        while i < len(array):
            curr_sum += array[i]
            if curr_sum == sum_:
                thickness = max(thickness, i - start + 1)
                start = i + 1
                curr_sum = 0
            elif curr_sum > sum_ or (i == len(array) - 1 and curr_sum < sum_):
                thickness = float('inf')
                break
            i += 1
        min_split_array = min(min_split_array, thickness)
        
    print(min_split_array)


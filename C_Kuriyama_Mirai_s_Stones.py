n = int(input())
v = list(map(int, input().split()))
m = int(input())

prefix_arr = []
prefix_arr.append(0)
for i in range(n):
    prefix_arr.append(prefix_arr[i] + v[i] )

v.sort()
prefix_arr_sorted = []
prefix_arr_sorted.append(0)
for i in range(n):
    prefix_arr_sorted.append(prefix_arr_sorted[i] + v[i] )

for _ in range(m):
    question = list(map(int, input().split()))

    if question[0] == 1:
        print(prefix_arr[question[2]] - prefix_arr[question[1] - 1])

    else:
        print(prefix_arr_sorted[question[2]] - prefix_arr_sorted[question[1] - 1])
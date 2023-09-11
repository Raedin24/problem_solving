"""
n items. price of i-th is pi
purchase at least x, get y cheapest free

given x and y, find max y, if x = 1

n = int
p = list(prices)
"""

n, q = map(int, input().split())
p = list(map(int, input().split()))
p.sort()

prefix_arr = [0]
for i in range(len(p)):
    prefix_arr.append(prefix_arr[i]+ p[i])
# print(prefix_arr)

for _ in range(q):
    question = list(map(int, input().split()))   
    print(prefix_arr[n - question[0] + question[1]] - prefix_arr[n- question[0]])

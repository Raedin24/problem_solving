from collections import Counter

x = int(input())
size = list(map(int, input().split()))
cust = int(input())
purchase = []
for _ in range(cust):
    purchase.append(map(int, input().split()))

available = Counter(size)
total_earned = 0

for desired_size, price in purchase:
    if desired_size in available and available[desired_size] > 0:
        total_earned += price
        available[desired_size] -= 1 

print(total_earned)
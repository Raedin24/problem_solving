# n, m = map(int, input().split())
# a = list(map(int, input().split()))


# count, amount, t = 0, 0, 0
# while count < m and t < n:
#     for i in a:
#         if i < 0:
#             amount += abs(i)
#             count += 1
#         t += 1

# print(amount)

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

count, amount = 0, 0
while m > 0 and count < n:
    for t in a:
        if t < 0:  # Only consider negative prices
            amount += abs(t)
            m -= 1
        count += 1

print(amount)


# def bob_and_tv_sets(n, m, a):
#   """Returns the maximum sum of money that Bob can earn."""
#   count = 0
#   amount = 0
#   max_price = -float("inf")
#   for i in range(n):
#     if a[i] < 0 and a[i] > max_price:
#       max_price = a[i]
#   for i in range(n):
#     if a[i] == max_price:
#       amount += abs(a[i])
#       count += 1
#       if count == m:
#         break
#   return amount

# def main():
#   """Reads input and prints output."""
#   n, m = map(int, input().split())
#   a = list(map(int, input().split()))
#   print(bob_and_tv_sets(n, m, a))

# if __name__ == "__main__":
#   main()

from collections import OrderedDict
order = OrderedDict()

n = int(input)
for _ in range(n):
    name, price = input().rsplit(' ', 1)
    price = int(price)

    if name in order:
        order[name] += price
    else:
        order[name] = price

for name, price in order.items():
    print(name, price)
# n = int(input())
# l = list(map(int, input().split()))
# b = l.copy()

# i = n - 1
# for i in range(n - 1, 0, -1):
#     for j in range(l[i], 0, -1):
#         b[i-1] = -1
#         i -= 1
#         if i == 0:
#             break

# alive = 0
# for k in b:
#     if k > -1:
#         alive += 1
# print(alive)

def alive_after_bell(n, claws):
  """
  Returns the number of people alive after the bell rings.

  Args:
    n: The number of people.
    claws: The lengths of the claws.

  Returns:
    The number of people alive after the bell rings.
  """
  alive = [True] * n
  for i in range(n - 1, 0, -1):
    j = bisect.bisect_left(claws, i - claws[i])
    if j < n:
      alive[j] = False

  return sum(alive)


def main():
  n = int(input())
  claws = list(map(int, input().split()))
  print(alive_after_bell(n, claws))


if __name__ == "__main__":
  main()


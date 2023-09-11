def is_beautiful(a):
  """Returns True if a is beautiful, False otherwise."""
  n = len(a)
  for i in range(2, n + 1):
    if not gcd(a[:i]) <= i:
      return False
  return True

def can_become_beautiful(a):
  """Returns True if a can become beautiful by reordering the elements, False otherwise."""
  n = len(a)
  if n < 2:
    return True

  for i in range(n):
    b = a[:i] + a[i + 1:]
    if is_beautiful(b):
      return True
  return False

def main():
  """Reads input and prints output."""
  t = int(input())
  for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print("Yes" if can_become_beautiful(a) else "No")

if __name__ == "__main__":
  main()

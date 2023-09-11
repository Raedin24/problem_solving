# t = int(input())


# def palindrome(s: str):
#     inverted = []
#     for i in range(n):
#         for j in range(i):
#             if s[j] == "0":
#                 inverted.append("1")
#             else:
#                 inverted.append("0")
#     # inverted = "".join(inverted)
#         # l, r = 0, n - 1
#         # # m = l + 1
#         # while l <= r:
#         #     if l == r:
#         #         print("Yes")
#         #         return
#         #     elif inverted[l] != inverted[r]:
#         #         print("No")
#         #         return
#         #     i += 1
#         #     j -= 1
#         # print("Yes")
#         # return

# for _ in range(t):
#     n = int(input())
#     s = input()
#     palindrome(s)

def is_palindrome(s):
  """Returns True if s is a palindrome, False otherwise."""
  for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
      return False
  return True

def solve(s):
  """Returns Yes if s can be made a palindrome after performing Inversion Magic once, No otherwise."""
  mid = len(s) // 2
  if s[:mid] == s[mid:][::-1]:
    return "Yes"
  else:
    return "No"

def main():
  """Reads input and prints output."""
  t = int(input())
  for _ in range(t):
    n = int(input())
    s = input()
    print(solve(s))

if __name__ == "__main__":
  main()

# # import time

# # t = int(input())

# # def first(n,s):

# #     diff_list = []
# #     for i in range(n):
# #         if i == 0:
# #             other_max = max(s[1:])
# #         elif i == n-1:
# #             other_max = max(s[:i])
# #         else:
# #             first_max = max(s[:i])
# #             second_max = max(s[i+1:])
# #             other_max = max(first_max, second_max)
# #         diff = s[i] - other_max
# #         diff_list.append(diff)
# #     for i in diff_list:
# #         print(i, end=" ")
# #     print()
# #     return

# # def second(n,s):

# #     diff_list = []
# #     for i in range(n):
# #         b = s.copy()
# #         b.remove(s[i])
# #         other_max = max(b)
# #         diff = s[i] - other_max
# #         diff_list.append(diff)
# #     for i in diff_list:
# #         print(i, end=" ")
# #     print()
# #     return




# # for _ in range(t):
# #     n = int(input())
# #     s = list(map(int, input().split()))
# #     t1 = time.time()
# #     first(n,s)
# #     t2 = time.time()
# #     second(n,s)
# #     t3 = time.time()
# #     print("first: ", t2-t1)
# #     print("second: ", t3-t2)

# # t = int(input())

# # for _ in range(t):
# #     n = int(input())
# #     s = list(map(int, input().split()))

# #     max_val = max(s)
# #     max_index = s.index(max_val)

# #     diff_list = []
# #     for i in range(n):
# #         if i != max_index:
# #             diff = s[i] - max_val
# #             diff_list.append(diff)

# #     for i in diff_list:
# #         print(i, end=" ")
# #     print()

# # def competition(strengths):
# #     best_other_strength = max(strengths)
# #     differences = []
# #     for i, strength in enumerate(strengths):
# #         if i == strengths.index(best_other_strength):
# #             differences.append(0)
# #         else:
# #             differences.append(strength - best_other_strength)
# #     return differences


# # t = int(input())
# # for _ in range(t):
# #     n = int(input())
# #     strengths = list(map(int, input().split()))
# #     differences = competition(strengths)
# #     for difference in differences:
# #         print(difference, end=" ")
# #     print()

# def competition(strengths):
#     best_other_strengths = [0] * len(strengths)
#     for i, strength in enumerate(strengths):
#         for j in range(i + 1, len(strengths)):
#             if strengths[j] > best_other_strengths[i]:
#                 best_other_strengths[i] = strengths[j]
#     differences = []
#     for i, strength in enumerate(strengths):
#         differences.append(best_other_strengths[i] - strength)
#     return differences


# t = int(input())
# for _ in range(t):
#     n = int(input())
#     strengths = list(map(int, input().split()))
#     differences = competition(strengths)
#     for difference in differences:
#         print(difference, end=" ")
#     print()

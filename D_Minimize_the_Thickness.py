# def check_feasible(a, target_sum, max_thickness):
#     current_sum = 0
#     segments = 1
    
#     for num in a:
#         if num > target_sum:
#             return False
        
#         if current_sum + num > target_sum:
#             current_sum = num
#             segments += 1
#         else:
#             current_sum += num
        
#         if segments > max_thickness:
#             return False
    
#     return True

# def minimum_thickness(a):
#     total_sum = sum(a)
#     left = max(a)
#     right = total_sum
    
#     while left < right:
#         mid = (left + right) // 2
#         if check_feasible(a, total_sum // mid, mid):
#             right = mid
#         else:
#             left = mid + 1
    
#     return right

# # Read the number of test cases
# t = int(input())

# for _ in range(t):
#     n = int(input())
#     a = list(map(int, input().split()))
#     result = minimum_thickness(a)
#     print(result)


t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    
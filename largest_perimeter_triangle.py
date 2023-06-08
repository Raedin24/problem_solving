def largestPerimeter(nums: list[int]):
    nums.sort()
    output = [0]

    for i in range(len(nums)):
        if i + 2 >= len(nums):
            break
        if sum(nums[i:i+2]) > nums[i+2]:
            output.append(sum(nums[i:i+3]))
        else:
            continue
            
    return output[-1]

def largestPerimeter2(nums: list[int]):
    nums.sort(reverse=True)

    for i in range(len(nums) - 2):
        if nums[i] < nums[i+1] + nums[i+2]:
            return sum(nums[i:i+3])
    
    return 0
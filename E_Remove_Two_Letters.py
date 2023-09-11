# Read the number of test cases
t = int(input())

# Iterate through each test case
for _ in range(t):
    # Read the input for each test case
    n = int(input())
    s = input()

    # Initialize variables
    count_consecutive = 0
    total_distinct_strings = n

    # Iterate through the string using a sliding window
    for i in range(1, n):
        if s[i] == s[i - 1]:
            count_consecutive += 1
        else:
            total_distinct_strings -= count_consecutive

            # Reset the consecutive count for the new window
            count_consecutive = 0

    # Subtract the last counted consecutive pairs
    total_distinct_strings -= count_consecutive

    # Print the result for the current test case
    print(total_distinct_strings)

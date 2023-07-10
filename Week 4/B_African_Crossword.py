n, m = map(int, input().split())
arr = []
for i in range(n):
	arr.append(input())

def inCol(current_char):
    count = 0
    for k in range(len(arr)):
        if arr[k][j] == current_char:
            count += 1
            if count > 1:
                return 1
            else:
                continue

    return 0
    
answer = []
for i in range(len(arr) ):
    for j in range(len(arr[i]) ):
        current_char = arr[i][j]
        in_row = arr[i].count(current_char)
        if in_row > 1:
            pass    	
        elif inCol(current_char) == 1:
            pass
        else:
            answer.append(current_char)

print(*answer, sep = "")
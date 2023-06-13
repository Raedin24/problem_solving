n, x = map(int, input().split())
scores = []
for _ in range(x):
    scores.append(list(map(float, input().split())))
    
transposed_scores = zip(*scores)
averages = [sum(student_scores) / x for student_scores in transposed_scores]

for average in averages:
    print(average)

# 1 try, 8 mins
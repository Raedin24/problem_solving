n, m = map(int, input().split())
list1 = list(map(int, input().split()))
list2 = list(map(int, input().split()))

def numberOfSmaller(list1, list2):
    count = []
    a = 0

    for i in list2:
        while a < len(list1) and list1[a] < i:
            a += 1
        count.append(a)
    return count

print(*numberOfSmaller(list1, list2), sep = " ")

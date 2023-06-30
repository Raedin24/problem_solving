def sortPeople(names: list[str], heights: list[int]) -> list[str]:
    a = {}
    for i in range(len(heights)):
        a[heights[i]] = i 

    for i in range(len(heights)):
        max_id = i
        for j in range(i+1, len(heights)):
            if heights[j] > heights[max_id]:
                max_id = j
        heights[i], heights[max_id] = heights[max_id], heights[i]

    result = []
    for i in heights:
        result.append(names[a[i]])
    
    return result
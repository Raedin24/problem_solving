def nearestValidPoint1(x: int, y: int, points: list[list[int]]) -> int:

    valid_points =[]
    for i in range(len(points)):
        if points[i][0] == x or points[i][1] == y:
            valid_points.append(points[i])

    smallest_distance = None
    smallest_index = -1

    for j in range(len(valid_points)):
        distance = abs(valid_points[j][0] - x) + abs(valid_points[j][1] - y)
        if smallest_distance is None or distance < smallest_distance:
            smallest_distance = distance
            smallest_index = points.index(valid_points[j])
    
    return smallest_index



def nearestValidPoint2(x: int, y: int, points: list[list[int]]) -> int:

    min_distance = float("inf")
    min_index = -1

    for i, (x1, y1) in enumerate(points):
        if x1 == x or y1 == y:
            distance = abs(x1 - x) + abs(y1 - y)
            if distance < min_distance:
                min_distance = distance
                min_index = i
                
    return min_index
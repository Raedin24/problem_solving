def checkIfExist(arr: list[int]) -> bool:
    for i in arr:
        for j in arr:
            if i != j and i == j * 2:
                return True
            elif i == j == 0 and arr.count(0) > 1:
                return True
    return False
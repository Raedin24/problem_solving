def findTheDifference(s: str, t: str) -> str:
    output = ""
    if s == "":
        return t
    for i in t:
        if t.count(i) > s.count(i):
            output = i
            

    return output
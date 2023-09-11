for _ in range(int(input())):
    n, s = int(input()), input()

    l, r = 0, len(s)-1
    while l <= r:
        if s[l] != s[r]:
            pass    
        elif s[l] == s[r]:
            print(r-l+1)
            break
        l += 1
        r -= 1

    if l > r:
        print(0)
x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    l = []
    i = 0
    j = 0
    k = 0
    while i <= x:
        j = 0
        while j <= y:
            k = 0
            while k <= z:
                if i + j + k != n:
                    temp = [i, j, k]
                    l.append(temp)
                k += 1
            j += 1
        i += 1
    print(l)
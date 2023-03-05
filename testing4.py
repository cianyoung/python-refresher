def persistence(n):
    count = 0
    n = str(n)
    while len(n) > 1:
        p = 1
        for i in n:
            p = p * int(i)
        n = str(p)
        count = count + 1
    return count



print(persistence(39))
from collections import Counter

def persistence(n):
    count = 0
    n = str(n)
    while len(n) > 1:
        p = 1
        print('here')
        for i in n:
            print(i, p)
            p = p * int(i)
            print(p, 'p result')
        n = str(p)
        count = count + 1
    return count


print(persistence(39))
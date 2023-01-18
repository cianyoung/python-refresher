"""https://www.codewars.com/kata/5526fc09a1bbd946250002dc/python"""

a = [160, 3, 1719, 19, 11, 13, -21]
aa = [2, 4, 0, 100, 4, 11, 2602, 36]

def find_outlier(b):
    odds = [x for x in b if x % 2 != 0]
    evens = [x for x in b if x % 2 == 0]
    return odds[0] if len(odds)<len(evens) else evens[0]

print(find_outlier(a))
print(find_outlier(aa))
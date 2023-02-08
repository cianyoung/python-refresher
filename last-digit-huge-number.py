"""https://www.codewars.com/kata/5518a860a73e708c0a000027/train/python"""

def last_digit(lst):
    num = 1
    for i in range(-1, -len(lst)-1, -1):
        print(i)
        num = lst[i] ** num
        print(num % 10)
    return(num)




print(last_digit([3, 4, 2]))

"""lst = [3, 4, 2]
print(range(-1, -len(lst)-1))"""
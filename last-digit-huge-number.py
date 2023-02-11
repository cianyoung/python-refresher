"""https://www.codewars.com/kata/5518a860a73e708c0a000027/train/python"""

def last_digit(lst):
    # Your Code Here
    n = 1
    for x in reversed(lst):
        n = x ** (n if n < 4 else n % 4 + 4)
        print('x:', x)
        print('n', n)
    print('n before return', n)
    return n % 10

print(last_digit([3, 4, 2, 10, 123]))
"""https://www.codewars.com/kata/52597aa56021e91c93000cb0/train/python"""

def move_zeros(lst):
    new = []
    for i in lst:
        if i == 0:
            new.append(i)
            lst.remove(i)
    nlst = lst + new
   # nlst.append(new)
    print(nlst)
    #print(','.join())

print(move_zeros(
        [1, 2, 0, 1, 0, 1, 0, 3, 0, 1]))

print(move_zeros(
        [9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]))
""" https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/python """
from itertools import groupby

def group_consecutives(lst):
    for k, g in groupby(enumerate(lst), lambda i_x : i_x[0] - i_x[1]):
        # print('keys', k)
        # print('groups', list(g))
        # create a new list r of elements of the group g with a difference of 1
        r = [x for k, x in g]
        print(f"Key: {k}, Group: {r}")
        if len(r) > 2:
            yield f"{r[0]}-{r[-1]}"
        else:
            yield from map(str, r)

def range_extraction(lst):
    return ','.join(group_consecutives(lst))


print(range_extraction([-6,-3,-2,-1,0,1,3,4,5,7,8,9,10,11,14,15,17,18,19,20]))
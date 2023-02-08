"""https://www.codewars.com/kata/51ba717bb08c1cd60f00002f/train/python"""

def solution(args):
    end = beg = args[0]
    out = []
    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append( str(beg) )
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append(str(beg) + '-' + str(end))
            beg = n
        end = n
    print(out)




solution([1, 2, 3, 4, 5, 7, 8, 11])
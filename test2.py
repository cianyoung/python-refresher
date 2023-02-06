def solution(args):
    out = []
    # assign first integer to beg & end
    beg = end = args[0]
    print('beg', beg)
    print('end', end)
    print(args[1:] + [""])

    for n in args[1:] + [""]:
        if n != end + 1:
            if end == beg:
                out.append(str(beg))
            elif end == beg + 1:
                out.extend( [str(beg), str(end)] )
            else:
                out.append( str(beg) + "-" + str(end) )
                print(f"beg {beg} + end {end}")
            beg = n
            print('beg', beg)
        end = n
    return ",".join(out)



print(solution([1, 2, 3, 5, 6, 7, 8]))
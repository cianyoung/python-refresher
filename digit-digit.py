def square_digits(num):
    empty = []
    for i in str(num):
        a = int(i) ** 2
        empty.append(str(a))
        print(empty)
    return "".join(empty)



print(square_digits(9119))
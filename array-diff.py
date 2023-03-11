def array_diff(a, b):
    temp = []
    for element in a:
        if element not in b:
            temp.append(element)
    return temp




print(array_diff([1,2,3], [1,2]))
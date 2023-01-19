"""You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even numbers at their original positions.
[7, 1]  =>  [1, 7]"""

#array = [5, 8, 6, 3, 4]
array = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

def sort_array(source_array):
    new = []
    a = 0
    odds = [x for x in source_array if x % 2 != 0]
    evens = [x for x in source_array if x % 2 == 0]
    odds.sort()
    for i in source_array:
        if i % 2 == 0:
            new.append(i)
        else:
            new.append(odds[a])
            a = a + 1
    print(new)



sort_array(array)

#return odds[0] if len(odds) < len(evens) else evens[0]
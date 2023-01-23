"""In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!
Examples:
With input 'a':  Your function should return: ['a']
With input 'ab': Your function should return ['ab', 'ba']
With input 'abc': Your function should return ['abc','acb','bac','bca','cab','cba']
With input 'aabb': Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
"""
def permutations(s):
    print(f'String {s}')
    # Case for empty string. If the string is empty; return true for empty list ("collections" evaluate to False when they are empty)
    if not s:
        return []

    # create empty list
    permutations_list = []
    def permute(data, i, length):
        print("permute -- inside, start of function")
        if i == length:
            permutations_list.append(''.join(data))
            print(f'appending now: {permutations_list}')
        else:
            for j in range(i, length):
                print('starting the loop')
                print(f'{j} is j -- here1')
                print(f'{i} is i -- here2')
                data[i], data[j] = data[j], data[i]
                print(f'{i} = i and {j} = j -- here3')
                print(f'data i :: {data[i]} and data j :: {data[j]}')
                print('here -- about to call function')
                permute(data, i + 1, length)
                print("after function")
                data[i], data[j] = data[j], data[i]
                print(f'zdata i :: {data[i]} and zdata j :: {data[j]}')
                print(f'{i} = i and {j} = j --here4')
                print('moving on')
    print('about to call permute function')
    permute(list(s), 0, len(s))
    # Sets cannot have two items with the same value.
    return list(set(permutations_list))

print(permutations("abc"))
#print(list("aabb"))
#print(len("aabb"))
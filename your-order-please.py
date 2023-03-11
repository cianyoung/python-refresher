"""https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python"""

def order(sentence):
    my_dict={}
    x = sentence.split()
    for num in x:
        for i in num:
            if i.isdigit():
                my_dict[num] = int(i)
                print(my_dict)
                break
    sorted_items = sorted(my_dict.keys())
    return ' '.join(my_dict.keys())





print(order("is2 Thi1s T4est 3a"))
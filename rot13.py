""" https://www.codewars.com/kata/530e15517bc88ac656000716/train/python """
import string

def rot13(message):
    # convert to list
    message = list(message)
    # empty array
    ciphered = []
    # create dict of lowercase ascii
    insert_dict = dict(enumerate(string.ascii_lowercase))
    for t in message:
        if t.isalpha():
            if t.isupper():
                new_value = (list(insert_dict.keys())[list(insert_dict.values()).index(t.lower())] + 13) % 26
                ciphered.append(list(insert_dict.values())[new_value].upper())
            else:
                new_value = (list(insert_dict.keys())[list(insert_dict.values()).index(t)] + 13) % 26
                ciphered.append(list(insert_dict.values())[new_value])
        else:
            ciphered.append(t)
    print(''.join(ciphered))

rot13('test')

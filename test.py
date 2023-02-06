""" https://www.codewars.com/kata/530e15517bc88ac656000716/train/python """
import string

insert_dict = dict(enumerate(string.ascii_lowercase))
print(insert_dict)
ciphered = []

print(list(insert_dict.keys())[list(insert_dict.values()).index('h')] + 11 )
print(list(insert_dict.values())[2].upper())

print(insert_dict.keys())
print(list(insert_dict.keys()))
print(insert_dict.values())
print(list(insert_dict.values())[24])

#new_value = (list(insert_dict.keys())[list(insert_dict.values()).index(t.lower())] + 13) % 26
#ciphered.append(list(insert_dict.values())[new_value].upper())

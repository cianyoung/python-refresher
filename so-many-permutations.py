"""In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.

Create as many "shufflings" as you can!
Examples:
With input 'a':  Your function should return: ['a']
With input 'ab': Your function should return ['ab', 'ba']
With input 'abc': Your function should return ['abc','acb','bac','bca','cab','cba']
With input 'aabb': Your function should return ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']
"""
from itertools import permutations
a = 'ab'

def permutations_l(s):
    permutations_list = list(set([''.join(p) for p in permutations(s)]))
    print(permutations_list)


permutations_l(a)
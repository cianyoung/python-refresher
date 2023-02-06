"""https://www.codewars.com/kata/5263c6999e0f40dee200059d/python"""
import itertools

def get_pins(observed):
    neighbours = {'1': ['1', '2', '4'],
                  '2': ['1', '2', '3', '5'],
                  '3': ['2', '3', '6'],
                  '4': ['1', '4', '5', '7'],
                  '5': ['2', '4', '5', '6', '8'],
                  '6': ['3', '5', '6', '9'],
                  '7': ['4', '7', '8'],
                  '8': ['5', '7', '8', '9', '0'],
                  '9': ['6', '8', '9'],
                  '0': ['0', '8']}
    x = [neighbours[n] for n in observed] # [] access value in dict, new_list = [expression for item in old_list]
    xx = (list(itertools.product(*x)))
    print(xx)
    print([''.join(b) for b in xx])

get_pins('109')

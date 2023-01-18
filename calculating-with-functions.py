"""https://www.codewars.com/kata/525f3eda17c7cd9f9e000b39/train/python
def zero(): #your code here
def one(): #your code here
def two(): #your code here
def three(): #your code here
def four(): #your code here
def five(): #your code here
def six(): #your code here
def seven(): #your code here
def eight(): #your code here
def nine(): #your code here
def plus(): #your code here
def minus(): #your code here
def times(): #your code here
def divided_by(): #your code here"""

def perform_operation(operations, number):
    if not operations: return number
    if operations["sign"] == "*":
        return operations["value"] * number
    if operations["sign"] == "+":
        return operations["value"] + number
    if operations["sign"] == "-":
        return number - operations["value"]
    if operations["sign"] == "/":
        return  number // operations["value"]

zero = lambda operations=None : perform_operation(operations, 0)
one = lambda operations=None : perform_operation(operations, 1)
two = lambda operations=None : perform_operation(operations, 2)
three = lambda operations=None : perform_operation(operations, 3)
four = lambda operations=None : perform_operation(operations, 4)
five = lambda operations=None : perform_operation(operations, 5)
six = lambda operations=None : perform_operation(operations, 6)
seven = lambda operations=None : perform_operation(operations, 7)
eight = lambda operations=None : perform_operation(operations, 8)
nine = lambda operations=None : perform_operation(operations, 9)

get_operation = lambda operation, num : {"sign": operation, "value": num}
plus = lambda num : get_operation("+", num)
minus = lambda num : get_operation("-", num)
times = lambda num : get_operation("*", num)
divided_by = lambda num : get_operation("/", num)

print(seven(times(five())))

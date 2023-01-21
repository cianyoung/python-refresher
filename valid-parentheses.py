"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""
a = "(())((()())())"
b = "()"

def valid_parentheses(string):
    stack = []
    for char in string:
        if char in '()':
            if char == '(' :
                stack.append(char)
            elif char == ')' and (not stack or stack[-1] != '('):
                return False
            else:
                stack.pop()
    return not stack

print(valid_parentheses(a))
print(valid_parentheses(b))

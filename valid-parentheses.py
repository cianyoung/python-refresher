"""
Write a function that takes a string of parentheses, and determines if the order of the parentheses is valid.
The function should return true if the string is valid, and false if it's invalid.
"()"              =>  true
")(()))"          =>  false
"("               =>  false
"(())((()())())"  =>  true
"""
a = "(())((()())())"

def valid_parentheses(string):
    stack = []
    for char in string:
        if char in '(':
            stack.append(char)
        elif char in ')':
            if not stack or char == ')' and stack[-1] != '(':
                return False
            stack.pop

    return not stack


valid_parentheses(a)

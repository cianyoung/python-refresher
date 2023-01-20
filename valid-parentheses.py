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
    odds = [x for x in string if x == '(']
    evens = [x for x in string if x == ')']
    print(odds)
    print(evens)
    for i in string:
        if i == evens[0]:
            print(i)


valid_parentheses(a)

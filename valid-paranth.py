from collections import OrderedDict

def valid_parentheses(string):
    slen = 0
    dict = OrderedDict.fromkeys(string)
    for k, v in dict.items():
        if (k == '()'[slen]):
            slen = slen + slen


        if (slen == (len(string))):
            return True
        
    return False
        
(valid_parentheses("()"))
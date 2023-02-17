s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"

def mix(s1, s2):
    history = {}
    alpha = 'abcdefghijklmnopqrstuvwxyz'
    for char in alpha:
        val1, val2 = s1.count(char), s2.count(char)
        if max(val1, val2) > 1:
            vart = "1" if val1 > val2 else "2" if val2 > val1 else ":"
            history[char] = (max(val1, val2), vart + ":" + char * max(val1, val2))
            




mix(s1, s2)

"""mix(s1, s2) --> "2:nnnnn/1:aaaa/1:hhh/2:mmm/2:yyy/2:dd/2:ff/2:ii/2:rr/=:ee/=:ss"
"""
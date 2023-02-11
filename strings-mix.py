from collections import Counter

s1 = "my&friend&Paul has heavy hats! &"
s2 = "my friend John has many many friends &"

def mix(s1, s2):
    a = Counter(s1)
    print(a)
    b = Counter(s2)
    print(b)
    d = {k: v for k,v in a.items() if v > 1}
    print(d)
    e = {k: v for k,v in b.items() if v > 1}
    print(e)

    sorted_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
    sorted_e = sorted(e.items(), key=lambda x: x[1], reverse=True)

    for i, (k, v) in enumerate(sorted_d):
        print(f"1: {i + 1}. {k}: {v}")
    for i, (k, v) in enumerate(sorted_e):
        print(f"2: {i + 1}. {k}: {v}")

mix(s1, s2)
def likes(names):
    n = len(names)
    return{
        0 : "no one likes this",
        1 : "{} likes this",
        2 : "{} and {} like this",
        3 : "{}, {} and {} like this",
        4 : "{}, {} and 2 others like this"
    }[min(4, n)].format(*names[:3], others=n-3)


print(likes(['Peter']))
print(likes(['Alex', 'Jacob', 'Mark', 'Max']))
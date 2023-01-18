"""Build a pyramid-shaped tower, as an array/list of strings, given a positive integer number of floors. A tower block is represented with "*" character.

For example, a tower with 3 floors looks like this:"""

def tower_builder(n_floors):
    # build here
    tower = []
    floor = ''
    for i in range(n_floors):
        stars = '*' * (i*2 + 1)
        print(i)
        print(stars)
        spaces = ' ' * (n_floors - i - 1)
        floor = spaces + stars + spaces
        tower.append(floor)
    print(tower)

tower_builder(n_floors=5)


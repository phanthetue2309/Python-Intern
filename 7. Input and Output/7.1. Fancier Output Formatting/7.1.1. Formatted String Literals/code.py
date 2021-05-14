import math
print(f'The value of pi is approximately {math.pi:.3f}.')

table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 76785}
for name, phone in table.items():
    print(f'{name:10} ==> {phone:10d}')

animals = 'eels'
print(f'My hovercraft is full of {animals!a}.') # conert to ASCII
print(f'My hovercraft is full of {animals!s}.') # conert to str
print(f'My hovercraft is full of {animals!r}.') # convert to repr
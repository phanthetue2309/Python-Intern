import re
x = re.findall(r'\bf[a-z]*', 'which foot or hand fell fastest')
print(x)
y = re.sub(r'(\b[a-z]+) \1', r'\1', 'cat in the the hat')
print(y)

print( 'tea for too'.replace('too', 'two') )
import math

print( format(math.pi, '.12g')  ) # give 12 significant digits


print( format(math.pi, '.2f') )   # give 2 digits after the point


print( repr(math.pi) )

x = 3.14159
print(x.as_integer_ratio())

print(x == 3537115888337719 / 1125899906842624)
print(2 + 2)
print(50 - 5*6)
print((50 - 5*6) / 4)
print(8 / 5 ) # division always returns a floating point number

print(17 / 3 )  # classic division returns a float
print(17 // 3) 
print(17 % 3)
print(5*3+2)

print(5 ** 2) # 5 squared
print(2 ** 7) # 2 to the power of 7

width = 20
height = 5 * 9
print(width * height)

print(4 * 3.75 - 1)

tax = 12.5 / 100
price = 100.50 
_ = price * tax

# In interactive mode, the last printed expression is assigned to the variable _. 
# This means that when you are using Python as a desk calculator, 
# it is somewhat easier to continue calculations, for example:
print(price * tax) 
print(price + _)
print(round(_, 2))
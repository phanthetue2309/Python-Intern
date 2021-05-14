basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed

print('orange' in basket   )             # fast membership testing

print('crabgrass' in basket )

# Demonstrate set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
a                                  # unique letters in a
print(a)
a - b                              # letters in a but not in b
print(a-b)
a | b                              # letters in a or b or both
print(a|b)
a & b                              # letters in both a and b
print(a&b)
a ^ b                              # letters in a or b but not both
print(a ^ b)

list = [1,2,1,3,4,1,5,6,7,2]
x = set(list)
print(x)
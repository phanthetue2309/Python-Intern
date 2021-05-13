print('spam eggs')
print('doesn\'t')  # use \' to escape the single quote...
print("doesn't")  # ...or use double quotes instead
print('"Yes," they said.')
print("\"Yes,\" they said.")
print('"Isn\'t," they said.')

print('"Isn\'t," they said.')

s = 'First line.\nSecond line.'
print(s)

print('C:\some\name')  # here \n means newline!
print(r'C:\some\name')  # note the r before the quote


print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print(3 * 'un' + 'ium')
text = ('Put several strings within parentheses ''to have them joined together.')
print(text)

prefix = 'Py'
print(prefix + 'thon')

word = 'Python'
print(word[0] )
print(word[-1])
print(word[-2])
print(word[-6])
print(word[0:2])
print(word[2:5])
print(word[:2] + word[2:])
print(word[:4] + word[4:])

s = 'supercalifragilisticexpialidocious'
print(len(s))
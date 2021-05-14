import json
f = open(r'G:\_School_\CODE\WORKING PARADOX\Python-Intern\7. Input and Output\7.2. Reading and Writing Files\7.2.2. Saving structured data with json\workfile', 'rb+')
f.write(b'0123456789abcdef')
f.seek(5)
f.read(1)
f.seek(-3, 2)  # Go to the 3rd byte before the end
f.read(1)

x = json.dumps([1, 'simple', 'list'])
print(x)
json.dump(x, f)

x = json.load(f)
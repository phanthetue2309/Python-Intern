import os
x = os.getcwd() 
print(x)
os.system('mkdir today')

print(dir(os))
print(help(os)) 

import shutil
shutil.copyfile('text.txt', 'text_copy_by_code.txt')
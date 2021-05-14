try : 
    for line in open("myfile.txt"):
        print(line, end="")
except : 
    print("NO file FOUND")
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
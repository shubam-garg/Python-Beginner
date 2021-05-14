# write a program to make the copy of any text file

with open("rendom.txt") as f:
    original=f.read()

with open("copy.txt", "w") as f:
    copy=f.write(original)

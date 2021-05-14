# Write a program to find out whether a file is identical & the content of another file.

with open("rendom.txt") as f:
    f1=f.read()

with open("copy.txt") as f:
    f2=f.read()

if f1==f2 :
    print("files are identical")
else:
    print("files are not identical")
# write a python program to rename a file

import os

with open("test.txt", "w") as f:   # created a new file to show remove function import through os
    f.write("Hello everyone!")

with open("test.txt") as f:
    f1=f.read()

with open("rename.txt", "w") as f:
    f.write(f1)

os.remove("test.txt") 
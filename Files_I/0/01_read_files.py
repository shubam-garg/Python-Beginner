import os
root_dir=os.path.dirname(os.path.abspath(__file__)) # To check root directory
f=open("rendom.txt","r")# in case if u will not define mode, it will be read by default
# out = f.read() this will read whole file
#out=f.read(6) # write the no. of letters u want to fetch from file

# it will read first line along with \n space
out=f.readline()
print(root_dir)
print(out)
# this will read second line
out=f.readline()
print(out)
f.close()
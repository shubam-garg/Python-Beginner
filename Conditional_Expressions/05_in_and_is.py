# is operator
a=None
if(a is None):
    print("Yes")  
else:
    print("No")

# in operator
b=[34,67.7,"roni"]
if("roni" in b):
    print("roni is here")
else:
    print("roni is not here")

# or direct method can be used

print(34 in b)
print(49 in b)
print(a is None)
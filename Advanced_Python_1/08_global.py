a=10 #global variable
def localVariable ():
    global a  # to change the value of global variable
    global b  # new global variable
    b=15
    print(b)
    a=5 # local variable if global keyword is not used
    print(a)

localVariable()
print(a)
print(b)
x = 50
if(x>3):
    print("The value of x is greater than 3") 
    # if first statement is true condition directly jump to else statement
elif(x>45):
    print("The value of x is greater than 45")
else:
    print("The value of x is not greater than 3 and 45")

# all the coditions will check and run all the true statements 
# else statement only work with last if statement
y = 50
if(y>3):
    print("The value of y is greater than 3") 
if(y>54):
    print("The value of y is greater than 45")
if(y>7):
    print("The value of y is greater than 7")
if(y>49):
    print("The value of y is greater than 49")
else:
    print("The value of y is not greater than 50")
    print("Done")# this print command come under else condition
# this print come out of if else condition becuse there is no space front of print
print("out of condition")
# write a program to print a/b value where a and  is integer 
# if b=0 print infinity by ZerodivisionError.
a=int(input("Enter the num1: "))
b=int(input("Enter the num2: "))
try:
    c=a/b
    print(c)
except ZeroDivisionError:
    print("Infinity")
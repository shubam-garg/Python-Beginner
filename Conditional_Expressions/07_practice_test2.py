''' Write a program to find whether a student is pass or fail,
    if it requires total 40% and at least 33% in each subject
    to pass. Assume 3 subjects and take marks as an input from
    the user. '''
a=int(input("Enter the marks of first subject :"))
b=int(input("Enter the marks of second subject :"))
c=int(input("Enter the marks of third subject :"))
    # if (a<=33 or b<=33 or c<=33)
    # or
if(a>=33 and b>=33 and c>=33): 
    print("You have cleared all the exams") 
else:  
    print("You are fail in atleast one exam")  
if((a+b+c)/3>=40):
    print("You have passed the class")
else:
    print("You are fail!You are unable to gain 40% percent overall")